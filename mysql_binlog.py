#!/usr/bin/python
# Classification (U)

"""Program:  mysql_binlog.py

    Description:  Maintains the MySQL binary logs using a number of functions
        to flush logs, backup logs, search for missing logs, and purge logs.

    Usage:
        mysql_binlog.py -c file -d path
            {-F -o path [-l path] [-z] |
             -K -o path |
             -M -o path [-l path] [-z] |
             -A -o path [-l path] [-z] |
             -S number |
             -R file]}
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c file -> Name of configuration file.  Required argument.
        -d dir path -> Directory path to config file (-c). Required arg.

        -F -> Flush and backup current binary log.  Require:  -o
            -o dir_path -> Log dump directory.
            -l dir_path -> MySQL binary log directory.  Overrides the
                configuration file binary_log entry.
            -z -> Compress binary log file during backup process.

        -K -> Print missing backed up binary logs.  Require:  -o
            -o dir_path -> Log dump directory.

        -M -> Backup missing binary logs.  Require:  -o
            -o dir_path -> Log dump directory.
            -l dir_path -> MySQL binary log directory.  Overrides the
                configuration file binary_log entry.
            -z -> Compress binary log file during backup process.

        -A -> Backup all binary logs.  Require:  -o
            -o dir_path -> Log dump directory.
            -l dir_path -> MySQL binary log directory.  Overrides the
                configuration file binary_log entry.
            -z -> Compress binary log file during backup process.

        -S number of days -> purge binary logs earlier than N days ago.

        -R file -> purge binary logs before binary log file name.

        -y value -> A flavor id for the program lock.  To create unique lock.
        -v -> Display version of this program.
        -h -> Help and usage message.

            NOTE 1: Options -M and -A are XOR.
            NOTE 2: Options -S and -R are XOR.
            NOTE 3: -v or -h overrides the other options.
            NOTE 4: If binary_log is not set in the configuration file, then
                will require -l option for -M, -F, and -A options.

    Notes:
        MySQL configuration file format (config/mysql_cfg.py.TEMPLATE):
            # Configuration file for MySQL Database:
            user = "USER"
            japd = "PSWORD"
            host = "HOST_IP"
            name = "HOST_NAME"
            sid = SERVER_ID
            extra_def_file = "PATH/config/mysql.cfg"
            serv_os = "Linux"
            port = 3306
            cfg_file = "MYSQL_DIRECTORY/mysqld.cnf"
            binary_log = None

            # If SSL connections are being used, configure one or more of these
                entries:
            ssl_client_ca = None
            ssl_client_key = None
            ssl_client_cert = None

            # Only changes these if necessary and have knowledge in MySQL
                SSL configuration setup:
            ssl_client_flag = None
            ssl_disabled = False
            ssl_verify_id = False
            ssl_verify_cert = False

        NOTE:  Include the cfg_file even if running remotely as the file will
            be used in future releases.

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

        Defaults Extra File format (config/mysql.cfg.TEMPLATE):
            [client]
            password="PASSWORD"
            socket="DIRECTORY_PATH/mysqld.sock"

        NOTE 1:  The socket information can be obtained from the my.cnf
            file under ~/mysql directory.
        NOTE 2:  Socket use is only required to be set in certain conditions
            when connecting using localhost.

    Example:
        mysql_binlog.py -c database -d config -F -l /mysql/binlogs -o /dump

"""

# Libraries and Global Variables

# Standard
import sys
import os
import time
import datetime

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from .mysql_lib import mysql_libs
    from .mysql_lib import mysql_class
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import lib.gen_class as gen_class                   # pylint:disable=R0402
    import mysql_lib.mysql_libs as mysql_libs           # pylint:disable=R0402
    import mysql_lib.mysql_class as mysql_class         # pylint:disable=R0402
    import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def cp_zip_file(args, fname):

    """Function:  cp_zip_file

    Description:  Copies file to directory and compresses if requested.

    Arguments:
        (input) args -> ArgParser class instance
        (input) fname -> File name to be copied and zipped

    """

    gen_libs.cp_file2(fname, args.get_val("-l"), args.get_val("-o"))

    if args.arg_exist("-z"):
        gen_libs.compress(os.path.join(args.get_val("-o"), fname))


def flush_log_bkp(args, server):

    """Function:  flush_log_bkp

    Description:  Flush the binary log and backup it up.

    Arguments:
        (input) args -> ArgParser class instance
        (input) server -> Database server instance

    """

    cur_log = server.fetch_log()
    server.flush_logs()

    if cur_log != server.fetch_log():
        cp_zip_file(args, cur_log)

    else:
        print(f"Warning: Flush of binary log: {cur_log} did not complete.")


def fetch_bkp_logs(dir_path):

    """Function:  fetch_bkp_logs

    Description:  Returns a list of binary log file names in the backup
        directory, but removes any .gz extension from the log name.

    Arguments:
        (input) dir_path -> Directory name
        (output) fnames -> List of binary log file names

    """

    fnames = gen_libs.list_files(dir_path)

    for item in fnames[:]:
        root, ext = os.path.splitext(item)

        if ext == ".gz":
            # Remove compressed name and append root name.
            fnames.remove(item)
            fnames.append(root)

    return fnames


def fetch_all_logs(server):

    """Function:  fetch_all_logs

    Description:  Fetches all binary logs and converts the tuple dictionary to
        a list of binary log names.

    Arguments:
        (input) server -> Database server instance
        (output) mysql_logs -> A list of binary log file names

    """

    mysql_logs = []

    for item in mysql_libs.fetch_logs(server):
        mysql_logs.append(item["Log_name"])

    return mysql_logs


def fetch_miss_logs(args, server):

    """Function:  fetch_miss_logs

    Description:  Fetches MySQL and Backup logs and returns a list of missing
        logs.

    Arguments:
        (input) args -> ArgParser class instance
        (input) server -> Database server instance
        (output) List of missing MySQL binary logs

    """

    mysql_logs = fetch_all_logs(server)

    # Remove current binary log from list.
    mysql_logs.remove(server.fetch_log())

    bkp_logs = fetch_bkp_logs(args.get_val("-o"))

    # Return files missing from backup directory.
    return gen_libs.is_missing_lists(mysql_logs, bkp_logs)


def missing_log(args, server):

    """Function:  missing_log

    Description:  Compares the binary logs in MySQL with a list in at the
        directory and displays any missing logs.

    Arguments:
        (input) args -> ArgParser class instance
        (input) server -> Database server instance

    """

    miss_files = fetch_miss_logs(args, server)

    if miss_files:
        print("Missing files:")

        for item in miss_files:
            print(f"\t{item}")


def bkp_log_miss(args, server):

    """Function:  bkp_log_miss

    Description:  Copies any missing binary logs to the backup directory.

    Arguments:
        (input) args -> ArgParser class instance
        (input) server -> Database server instance

    """

    miss_files = fetch_miss_logs(args, server)

    for item in miss_files:
        cp_zip_file(args, item)


def bkp_log_all(args, server):

    """Function:  bkp_log_all

    Description:  Backups up all binary logs listed in MySQL to a backup
        directory.  Copies any existing binary logs to another name.

    Arguments:
        (input) args -> ArgParser class instance
        (input) server -> Database server instance

    """

    mysql_logs = fetch_all_logs(server)

    # Remove current binary log file from list.
    mysql_logs.remove(server.fetch_log())

    # Get file names in backup directory.
    bkp_logs = fetch_bkp_logs(args.get_val("-o"))

    for item in mysql_logs:

        if item in bkp_logs:
            fname = item

            if not os.path.isfile(os.path.join(args.get_val("-o"), item)):
                fname = item + ".gz"

            ext = time.strftime("%Y%m%d_%I%M")
            gen_libs.rename_file(fname, fname + "." + ext, args.get_val("-o"))

        cp_zip_file(args, item)


def purge_log_day(args, server):

    """Function:  purge_log_day

    Description:  Purge binary logs in MySQL based on current date and time
        minus a number of days.

    Arguments:
        (input) args -> ArgParser class instance
        (input) server -> Database server instance

    """

    pre_dtg = datetime.datetime.now() - \
        datetime.timedelta(days=int(args.get_val("-S")))
    prg_dtg = datetime.datetime.strftime(pre_dtg, "%Y-%m-%d %H:%M:%S")

    # Purge logs using MySQL 'before' option.
    mysql_libs.purge_bin_logs(server, "before", prg_dtg)


def purge_log_name(args, server):

    """Function:  purge_log_name

    Description:  Purge binary logs in MySQL before the specified binary log
        name.

    Arguments:
        (input) args -> ArgParser class instance
        (input) server -> Database server instance

    """

    mysql_logs = fetch_all_logs(server)

    if args.get_val("-R") in mysql_logs:

        # Purge logs using MySQL 'to' option.
        mysql_libs.purge_bin_logs(server, "to", args.get_val("-R"))

    else:
        print(f'Error:  {args.get_val("-R")} log is not present.')


def run_program(args, func_dict, ord_prec_list):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args -> ArgParser class instance
        (input) func_dict -> Dictionary list of functions and options
        (input) ord_prec_list -> Order of precedence of the arguments

    """

    func_dict = dict(func_dict)
    ord_prec_list = list(ord_prec_list)
    server = mysql_libs.create_instance(
        args.get_val("-c"), args.get_val("-d"), mysql_class.Server)
    server.connect(silent=True)

    if server.conn_msg:
        print(f"run_program:  Error encountered on server {server.name}:"
              f" {server.conn_msg}")

    else:
        # Execute functions based on order of precedence.
        for item in ord_prec_list:

            if args.arg_exist(item):
                func_dict[item](args, server)

        mysql_libs.disconnect([server])


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> contains directories and their octal permissions
        func_dict -> dictionary list for the function calls or other options
        opt_con_req_list -> contains the options that require other options
        xor_noreq -> contains options that are XOR, but are not required
        ord_prec_array -> holds options in order of precedence to be executed
        opt_req_list -> contains the options that are required for the program
        opt_val_list -> contains options which require values
        req_option -> contains options which require -l option

    Arguments:
        (input) argv -> Arguments from the command line

    """

    dir_perms_chk = {"-d": 5, "-l": 5, "-o": 7}
    func_dict = {
        "-F": flush_log_bkp, "-K": missing_log, "-M": bkp_log_miss,
        "-A": bkp_log_all, "-S": purge_log_day, "-R": purge_log_name}
    opt_con_req_list = {
        "-F": ["-o", "-l"], "-M": ["-o", "-l"], "-A": ["-o", "-l"],
        "-K": ["-o"]}
    xor_noreq = {"-S": "-R", "-M": "-A"}
    ord_prec_list = ["-F", "-K", "-M", "-A", "-S", "-R"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-l", "-o", "-R", "-S", "-y"]
    req_option = {"-F", "-M", "-A"}

    # Process argument list from command line.
    args = gen_class.ArgParser(sys.argv, opt_val=opt_val_list, do_parse=True)

    # Get binary_log entry if -l option is not passed for certain options
    if not args.arg_exist("-l") and (set(args.get_args_keys()) & req_option):
        cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))

        if hasattr(cfg, "binary_log") and cfg.binary_log:
            args.insert_arg("-l", cfg.binary_log)

        else:
            print("ERROR: Require either -l option or binary_log filled in.")
            return

    if not gen_libs.help_func(args, __version__, help_message)  \
       and args.arg_require(opt_req=opt_req_list)               \
       and args.arg_noreq_xor(xor_noreq=xor_noreq)              \
       and args.arg_cond_req(opt_con_req=opt_con_req_list)      \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk):

        try:
            prog_lock = gen_class.ProgramLock(
                sys.argv, args.get_val("-y", def_val=""))
            run_program(args, func_dict, ord_prec_list)

            del prog_lock

        except gen_class.SingleInstanceException:
            print(f'WARNING:  lock in place for mysql_binlog with id of:'
                  f' {args.get_val("-y", def_val="")}')


if __name__ == "__main__":
    sys.exit(main())
