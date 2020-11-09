#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in mysql_binlog.py.

    Usage:
        test/unit/mysql_binlog/run_program.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mysql_binlog
import version

__version__ = version.__version__


def flush_log_bkp(args_array, server):

    """Function:  flush_log_bkp

    Description:  flush_log_bkp function.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) server -> Database server instance.

    """

    status = True

    if args_array and server:
        status = True

    return status


def missing_log(args_array, server):

    """Function:  missing_log

    Description:  missing_log function.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) server -> Database server instance.

    """

    status = True

    if args_array and server:
        status = True

    return status


def bkp_log_miss(args_array, server):

    """Function:  bkp_log_miss

    Description:  bkp_log_miss function.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) server -> Database server instance.

    """

    status = True

    if args_array and server:
        status = True

    return status


def bkp_log_all(args_array, server):

    """Function:  bkp_log_all

    Description:  bkp_log_all function.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) server -> Database server instance.

    """

    status = True

    if args_array and server:
        status = True

    return status


def purge_log_day(args_array, server):

    """Function:  purge_log_day

    Description:  purge_log_day function.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) server -> Database server instance.

    """

    status = True

    if args_array and server:
        status = True

    return status


def purge_log_name(args_array, server):

    """Function:  purge_log_name

    Description:  purge_log_name function.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) server -> Database server instance.

    """

    status = True

    if args_array and server:
        status = True

    return status


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__ -> Class initialization.
        connect -> connect method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.current_log = "Log3"

    def connect(self):

        """Method:  connect

        Description:  connect method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_two_functions -> Test with two function call.
        test_one_function -> Test with one function call.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-c": "mysql_cfg", "-d": "config", "-F": True}
        self.args_array2 = {"-c": "mysql_cfg", "-d": "config", "-R": True,
                            "-F": True}
        self.ord_prec_list = ["-F", "-K", "-M", "-A", "-S", "-R"]
        self.func_dict = {"-F": flush_log_bkp, "-K": missing_log,
                          "-M": bkp_log_miss, "-A": bkp_log_all,
                          "-S": purge_log_day, "-R": purge_log_name}

    @mock.patch("mysql_binlog.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_binlog.mysql_libs.create_instance")
    def test_two_functions(self, mock_inst):

        """Function:  test_two_functions

        Description:  Test with two function call.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(mysql_binlog.run_program(
            self.args_array2, self.func_dict, self.ord_prec_list))

    @mock.patch("mysql_binlog.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_binlog.mysql_libs.create_instance")
    def test_one_function(self, mock_inst):

        """Function:  test_one_function

        Description:  Test with one function call.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(mysql_binlog.run_program(
            self.args_array, self.func_dict, self.ord_prec_list))


if __name__ == "__main__":
    unittest.main()
