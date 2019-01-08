# Python project for maintaining binary logs in a MySQL database.
# Classification (U)

# Description:
  This program is used to maintain binary logs in a MySQL database to include flushing, backing up, and purging logs.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Flush binary logs.
  * Backup missing binary logs.
  * Backup all binary logs.
  * Purge binary logs earlier than N days ago.
  * Purge binary logs before binary log file name.
  * Print missing backed up binary logs.


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/cmds_gen
    - lib/arg_parser
    - lib/gen_libs
    - mysql_lib/mysql_libs


# Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-binlog.git
```

Install/upgrade system modules.

```
cd mysql-binlog
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:
  * Replace **{Python_Project}** with the baseline path of the python program.

Create MySQL configuration file.

```
cd config
cp mysql_cfg.py.TEMPLATE mysql_cfg.py
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - passwd = "ROOT_PASSWORD"
    - host = "SERVER_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "{Python_Project}/config/mysql.cfg"

```
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.

```
cp mysql.cfg.TEMPLATE mysql.cfg
```
Make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
    - password="ROOT_PASSWORD"
    - socket={BASE_DIR}/mysql/tmp/mysql.sock

```
vim mysql.cfg
chmod 600 mysql.cfg
```


# Program Descriptions:
### Program: mysql_binlog.py
##### Description: Administration program for the MySQL binary log system.


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/mysql-binlog/mysql_binlog.py -h
```


# Help Message:
  Below is the help message for the program the program.  Run the program with the -h option get the latest help message for the program.

    Program:  mysql_binlog.py

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


# Testing:


# Unit Testing:

### Description: Testing consists of unit testing for the functions in the mysql_binlog.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-binlog.git
```

Install/upgrade system modules.

```
cd mysql-binlog
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Unit test runs for mysql_binlog.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mysql-binlog
```

### Unit:  help_message
```
test/unit/mysql_binlog/help_message.py
```

### Unit:  
```
test/unit/mysql_binlog/
```

### Unit:  
```
test/unit/mysql_binlog/
```

### Unit:  run_program
```
test/unit/mysql_binlog/run_program.py
```

### Unit:  main
```
test/unit/mysql_binlog/main.py
```

### All unit testing
```
test/unit/mysql_binlog/unit_test_run.sh
```

### Code coverage program
```
test/unit/mysql_binlog/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the mysql_binlog.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-binlog.git
```

Install/upgrade system modules.

```
cd mysql-binlog
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create MySQL configuration file.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd test/integration/mysql_binlog/config
cp ../../../../config/mysql_cfg.py.TEMPLATE mysql_cfg.py
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup.
    - passwd = "ROOT_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"
    - sid = SERVER_ID
    - extra_def_file = '{Python_Project}/config/mysql.cfg'

```
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.

```
cp ../../../../config/mysql.cfg.TEMPLATE mysql.cfg
```

Make the appropriate change to the MySQL definition setup.
  * Change these entries in the MySQL configuration file:
    - password="ROOT_PASSWORD"
    - socket={BASE_DIR}/mysql/tmp/mysql.sock

```
vim mysql.cfg
chmod 600 mysql.cfg
```


# Integration test runs for mysql_binlog.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mysql-binlog
```

### Integration:  
```
test/integration/mysql_binlog/
```

### All integration testing
```
test/integration/mysql_binlog/integration_test_run.sh
```

### Code coverage program
```
test/integration/mysql_binlog/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the mysql_binlog.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-binlog.git
```

Install/upgrade system modules.

```
cd mysql-binlog
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:
  * Replace **{Python_Project}** with the baseline path of the python program.

Create MySQL configuration file.

```
cd test/blackbox/mysql_binlog/config
cp ../../../../config/mysql_cfg.py.TEMPLATE mysql_cfg.py
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - passwd = "ROOT_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"
    - sid = SERVER_ID
    - extra_def_file = '{Python_Project}/config/mysql.cfg'

```
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.
```
cp ../../../../config/mysql.cfg.TEMPLATE mysql.cfg
```

Make the appropriate change to the MySQL definition setup.
  * Change these entries in the MySQL configuration file:
    - password="ROOT_PASSWORD"
    - socket={BASE_DIR}/mysql/tmp/mysql.sock

```
vim mysql.cfg
chmod 600 mysql.cfg
```

# Blackbox test run for mysql_binlog.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mysql-binlog
```

### Blackbox:  
```
test/blackbox/mysql_binlog/blackbox_test.sh
```

