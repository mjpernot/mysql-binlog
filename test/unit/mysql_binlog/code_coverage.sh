#!/bin/bash
# Unit test code coverage for program module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#   that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/bkp_log_all.py
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/bkp_log_miss.py
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/cp_zip_file.py
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/fetch_all_logs.py
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/fetch_bkp_logs.py
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/fetch_miss_logs.py
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/flush_log_bkp.py
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/help_message.py
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/main.py
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/missing_log.py
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/purge_log_day.py
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/purge_log_name.py
coverage run -a --source=mysql_binlog test/unit/mysql_binlog/run_program.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
