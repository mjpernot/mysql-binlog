#!/usr/bin/python
# Classification (U)

"""Program:  mysql_binlog.py

    Description:  Maintains the MySQL binary log using a number of functions to
        flush logs, backup logs, and purge logs.

    Usage:
        mysql_binlog.py -c file -d path {-F | -K | [-M | -A] |
            [-S number | -R file]} [-o path | -l path] [-v | -h]

    Arguments:
        -c file => Name of configuration file.  Required argument.
        -d dir path => Directory path to config file (-c). Required arg.
        -F => Flush binary logs.  Require:  -o, -l
        -K => Print missing backed up binary logs.  Require:  -o
        -M => Backup missing binary logs.  Require:  -o, -l.
        -A => Backup all binary logs.  Require:  -o, -l.
        -S number of days - purge binary logs earlier than N days ago.
        -R file - purge binary logs before binary log file name.
        -z => Compress database dump files.
        -o dir_path => Log dump directory.  Required by: -F, -K, -M, -A
        -l dir_path => MySQL log directory.  Required by: -F, -M, -A
        -v => Display version of this program.
        -h => Help and usage message.

            NOTE 1:  Options -M and -A are XOR.
            NOTE 2:  Options -S and -R are XOR.
            NOTE 3:  -v or -h overrides the other options.

    Notes:
        MySQL configuration file format (mysql_{host}.py):

            # Configuration file for {MySQL Database Server}
            user = "root"
            passwd = "ROOT_PASSWORD"
            host = "IP_ADDRESS"
            serv_os = "Linux" or "Solaris"
            name = "HOSTNAME"
            port = PORT_NUMBER (default of mysql is 3306)
            cfg_file = "DIRECTORY_PATH/my.cnf"
            sid = "SERVER_ID"
            extra_def_file = "DIRECTORY_PATH/myextra.cfg"

        NOTE:  Include the cfg_file even if running remotely as the file will
            be used in future releases.

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

        Defaults Extra File format (filename.cfg):
            [client]
            password="ROOT_PASSWORD"
            socket="DIRECTORY_PATH/mysql.sock"

        NOTE:  The socket information can be obtained from the my.cnf
            file under ~/mysql directory.

    Example:
        mysql_binlog.py -F -c database -d config -l ./data -o ./dump

"""

# Libraries and Global Variables

# Standard
import sys
import os
import time
import datetime

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.cmds_gen as cmds_gen
import mysql_lib.mysql_libs as mysql_libs
import version

# Version
__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def cp_zip_file(args_array, fname):

    """Function:  cp_zip_file

    Description:  Copies file to directory and compresses if requested.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) fname -> File name to be copied and zipped.

    """

    gen_libs.cp_file2(fname, args_array["-l"], args_array["-o"])

    if "-z" in args_array:
        gen_libs.compress(os.path.join(args_array["-o"], fname))


def flush_log_bkp(args_array, SERVER):

    """Function:  flush_log_bkp

    Description:  Flush the binary log and backup it up.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) SERVER -> Database server instance.

    """

    cur_log = SERVER.fetch_log()
    SERVER.flush_logs()

    if cur_log != SERVER.fetch_log():
        cp_zip_file(args_array, cur_log)

    else:
        sys.exit("Error:  Flush of binary log did not complete.")


def fetch_bkp_logs(dir_path):

    """Function:  fetch_bkp_logs

    Description:  Returns a list of binary log file names in the backup
        directory, but removes any .gz extension from the log name.

    Arguments:
        (input) dir_path -> Directory name.
        (output) fnames -> List of binary log file names.

    """

    fnames = gen_libs.list_files(dir_path)

    for y in fnames[:]:
        root, ext = os.path.splitext(y)

        if ext == ".gz":
            # Remove compressed name and append root name.
            fnames.remove(y)
            fnames.append(root)

    return fnames


def fetch_all_logs(SERVER):

    """Function:  fetch_all_logs

    Description:  Fetches all binary logs and converts the tuple dictionary to
        a list of binary log names.

    Arguments:
        (input) SERVER -> Database server instance.
        (output) -> Return a list of binary log file names.

    """

    mysql_logs = []

    for x in mysql_libs.fetch_logs(SERVER):
        mysql_logs.append(x["Log_name"])

    return mysql_logs


def fetch_miss_logs(args_array, SERVER):

    """Function:  fetch_miss_logs

    Description:  Fetches MySQL and Backup logs and returns a list of missing
        logs.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) SERVER -> Database server instance.

    """

    mysql_logs = fetch_all_logs(SERVER)

    # Remove current binary log from list.
    mysql_logs.remove(SERVER.fetch_log())

    bkp_logs = fetch_bkp_logs(args_array["-o"])

    # Return files missing from backup directory.
    return gen_libs.is_missing_lists(mysql_logs, bkp_logs)


def missing_log(args_array, SERVER):

    """Function:  missing_log

    Description:  Compares the binary logs in MySQL with a list in at the
        directory and displays any missing logs.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) SERVER -> Database server instance.

    """

    miss_files = fetch_miss_logs(args_array, SERVER)

    if miss_files:
        print("Missing files:")

        for x in miss_files:
            print("\t{0}".format(x))


def bkp_log_miss(args_array, SERVER):

    """Function:  bkp_log_miss

    Description:  Copies any missing binary logs to the backup directory.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) SERVER -> Database server instance.

    """

    miss_files = fetch_miss_logs(args_array, SERVER)

    for x in miss_files:
        cp_zip_file(args_array, x)


def bkp_log_all(args_array, SERVER):

    """Function:  bkp_log_all

    Description:  Backups up all binary logs listed in MySQL to a backup
        directory.  Copies any existing binary logs to another name.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) SERVER -> Database server instance.

    """

    mysql_logs = fetch_all_logs(SERVER)

    # Remove current binary log file from list.
    mysql_logs.remove(SERVER.fetch_log())

    # Get file names in backup directory.
    bkp_logs = fetch_bkp_logs(args_array["-o"])

    for x in mysql_logs:

        if x in bkp_logs:
            fname = x

            if not os.path.isfile(os.path.join(args_array["-o"], x)):
                fname = x + ".gz"

            ext = time.strftime("%Y%m%d_%I%M")
            gen_libs.rename_file(fname, fname + "." + ext, args_array["-o"])

        cp_zip_file(args_array, x)


def purge_log_day(args_array, SERVER):

    """Function:  purge_log_day

    Description:  Purge binary logs in MySQL based on current date and time
        minus a number of days.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) SERVER -> Database server instance.

    """

    pre_dtg = datetime.datetime.now() - \
        datetime.timedelta(days=int(args_array["-S"]))
    prg_dtg = datetime.datetime.strftime(pre_dtg, "%Y-%m-%d %H:%M:%S")

    # Purge logs using MySQL 'before' option.
    mysql_libs.purge_bin_logs(SERVER, "before", prg_dtg)


def purge_log_name(args_array, SERVER):

    """Function:  purge_log_name

    Description:  Purge binary logs in MySQL before the specified binary log
        name.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) SERVER -> Database server instance.

    """

    mysql_logs = fetch_all_logs(SERVER)

    # Is binary log file name present in database.
    if args_array["-R"] in mysql_logs:
        # Purge logs using MySQL 'to' option.
        mysql_libs.purge_bin_logs(SERVER, "to", args_array["-R"])

    else:
        print("Error:  {0} log is not present.".format(args_array["-R"]))


def run_program(args_array, func_dict, ord_prec_list):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dictionary list of functions and options.
        (input) ord_prec_list -> Order of precedence of the arguments.

    """

    SERVER = mysql_libs.crt_srv_inst(args_array["-c"], args_array["-d"])
    SERVER.connect()

    # Execute functions based on order of precedence.
    for x in ord_prec_list:

        if x in args_array:
            func_dict[x](args_array, SERVER)

    cmds_gen.disconnect([SERVER])


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        func_dict -> dictionary list for the function calls or other options.
        opt_con_req_list -> contains the options that require other options.
        xor_noreq_list -> contains options that are XOR, but are not required.
        ord_prec_array -> contains options in order of precedence to be
            executed.
        opt_req_list -> contains the options that are required for the program.
        opt_val_list -> contains options which require values.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    dir_chk_list = ["-d", "-l", "-o"]
    func_dict = {"-F": flush_log_bkp, "-K": missing_log, "-M": bkp_log_miss,
                 "-A": bkp_log_all, "-S": purge_log_day, "-R": purge_log_name}
    opt_con_req_list = {"-F": ["-o", "-l"], "-M": ["-o", "-l"],
                        "-A": ["-o", "-l"], "-K": ["-o"]}
    xor_noreq_list = {"-S": "-R", "-M": "-A"}
    ord_prec_list = ["-F", "-K", "-M", "-A", "-S", "-R"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-l", "-o", "-R", "-S"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list)

    if not gen_libs.help_func(args_array, __version__, help_message):
        if not arg_parser.arg_require(args_array, opt_req_list) \
           and arg_parser.arg_noreq_xor(args_array, xor_noreq_list) \
           and arg_parser.arg_cond_req(args_array, opt_con_req_list) \
           and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list):
            run_program(args_array, func_dict, ord_prec_list)


if __name__ == "__main__":
    sys.exit(main())