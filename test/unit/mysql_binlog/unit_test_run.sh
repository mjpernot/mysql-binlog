#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
test/unit/mysql_binlog/bkp_log_all.py
test/unit/mysql_binlog/bkp_log_miss.py
test/unit/mysql_binlog/cp_zip_file.py
test/unit/mysql_binlog/fetch_all_logs.py
test/unit/mysql_binlog/fetch_bkp_logs.py
test/unit/mysql_binlog/fetch_miss_logs.py
test/unit/mysql_binlog/flush_log_bkp.py
test/unit/mysql_binlog/help_message.py
test/unit/mysql_binlog/main.py
test/unit/mysql_binlog/missing_log.py
test/unit/mysql_binlog/purge_log_day.py
test/unit/mysql_binlog/purge_log_name.py
test/unit/mysql_binlog/run_program.py
