# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [3.2.0] - 2023-06-26
- Upgraded python-lib to v2.10.1
- Replace arg_parser.arg_parse2 with gen_class.ArgParser.

### Fixed
- main: Fixed when programs fails if -l option is not passed and binary_log is set to none or not available.

### Changed
- Multiple functions: Replaced the arg_parser code with gen_class.ArgParser code.
- main: Removed gen_libs.get_inst call.


## [3.1.2] - 2022-12-15
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4
- Upgraded mysql-lib to v5.3.2
 
### Changed
- Converted imports to use Python 2.7 or Python 3.
- main: Changed viewkeys() to set(dict.keys()).


## [3.1.1] - 2022-05-31
- Upgrade mysql-connector to v8.0.22.
- Upgraded mysql-libs to v5.3.1.

### Changed
- main: Gets binary_log entry and inserts into args_array if -l option is not passed for certain options.
- config/mysql_cfg.py.TEMPLATE: Added TLS and binary_log entries to configuration.
- Documentation updates.


## [3.1.0] - 2021-07-21
- Updated to work in a SSL environment.
- Updated to use the mysql_libs v5.2.1 library.
- Updated to work in MySQL 8.0 and 5.7 environments.

### Changed
- run_program:  Capture and process status from connect method call.
- run_program:  Replaced cmds_gen.disconect call with mysql_libs.disconnect call.
- config/mysql_cfg.py.TEMPLATE: Added SSL configuration entries.
- Removed unnecessary \*\*kwargs in function argument list.
- Documentation updates.


## [3.0.4] - 2020-11-09
- Updated to use the mysql_libs v5.0.0 library.

### Fixed
- config/mysql.cfg.TEMPLATE:  Point to correct socket file.

### Changed
- config/mysql_cfg.py.TEMPLATE:  Changed entry name.
- Documentation updates.


## [3.0.3] - 2020-04-22
### Added
- Added -y option to allow a flavor ID for the program lock.

### Fixed
- main:  Fixed handling command line arguments.
- Fixed problem with mutable default arguments issue in a number of functions.

### Changed
- flush_log_bkp:  Replaced sys.exit() with print() and changed message to Warning message.
- main:  Added program lock functionality to program.
- run_program:  Replaced crt_srv_inst call with create_instance call.
- main:  Refactored "if" statements in function.
- Changed variable names to standard naming convention in a number of functions.
- Added \*\*kwargs to argument list to all functions.
- config/mysql_cfg.py.TEMPLATE:  Change to generic template.
- Documentation updates.


## [3.0.2] - 2018-12-06
### Changed
- Documentation updates.


## [3.0.1] - 2018-05-25
### Fixed
- cp_zip_file:  Changed "gen_libs.cp_file" to "gen_libs.cp_file2".
- bkp_log_all:  Corrected argument list order and format for "gen_libs.rename_file" call.


## [3.0.0] - 2018-05-23
Breaking Change

### Changed
- Changed "mysql_libs" calls to new naming schema.
- Changed "cmds_gen" calls to new naming schema.
- Changed "gen_libs" calls to new naming schema.
- Changed "arg_parser" calls to new naming schema.
- Changed function names from uppercase to lowercase.
- Setup single-source version control.


## [2.3.0] - 2018-05-04
### Changed
- Changed "commands" to "mysql_libs" module reference.

### Added
- Added single-source version control.


## [2.2.0] - 2017-08-17
### Changed
- Convert program to use local libraries from ./lib directory.
- Change single quotes to double quotes.
- Help_Message:  Replace docstring with printing the programs \_\_doc\_\_.


## [2.1.0] - 2016-09-15
### Changed
- main:  Changed the argument option for main functions to uppercase to be inline with the other programs.
- Purge_Log_Name:  Changed -r to -R.
- Purge_Log_Day:  Changed -s to -S.
- main:  Replaced Arg_Parse with Arg_Parse2, reorganized the main 'if' statements, and streamlined the check process.
- Run_Program:  Added connect and disconect commands to the database.


## [2.0.0] - 2015-12-09
### Changed
- Extensive updates to the program to modularize and streamline the program and also replace the current database connection mechanism with a class based database connection mechanism.


## [1.0.0] - 2015-10-09
- Initial creation.

