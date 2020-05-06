# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [3.0.3] - 2020-04-22
### Fixed
- bkp_log_all:  Changed function parameter mutable argument default to immutable argument default.
- purge_log_day:  Changed function parameter mutable argument default to immutable argument default.
- purge_log_name:  Changed function parameter mutable argument default to immutable argument default.
- run_program:  Changed function parameter mutable argument default to immutable argument default.

### Changed
- Added \*\*kwargs to argument list to all functions.
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

