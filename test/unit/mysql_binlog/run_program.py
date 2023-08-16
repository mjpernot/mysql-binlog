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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mysql_binlog
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def flush_log_bkp(args_array, server):

    """Function:  flush_log_bkp

    Description:  flush_log_bkp function.

    Arguments:
        (input) args_array
        (input) server

    """

    status = True

    if args_array and server:
        status = True

    return status


def missing_log(args_array, server):

    """Function:  missing_log

    Description:  missing_log function.

    Arguments:
        (input) args_array
        (input) server

    """

    status = True

    if args_array and server:
        status = True

    return status


def bkp_log_miss(args_array, server):

    """Function:  bkp_log_miss

    Description:  bkp_log_miss function.

    Arguments:
        (input) args_array
        (input) server

    """

    status = True

    if args_array and server:
        status = True

    return status


def bkp_log_all(args_array, server):

    """Function:  bkp_log_all

    Description:  bkp_log_all function.

    Arguments:
        (input) args_array
        (input) server

    """

    status = True

    if args_array and server:
        status = True

    return status


def purge_log_day(args_array, server):

    """Function:  purge_log_day

    Description:  purge_log_day function.

    Arguments:
        (input) args_array
        (input) server

    """

    status = True

    if args_array and server:
        status = True

    return status


def purge_log_name(args_array, server):

    """Function:  purge_log_name

    Description:  purge_log_name function.

    Arguments:
        (input) args_array
        (input) server

    """

    status = True

    if args_array and server:
        status = True

    return status


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val
        arg_exist

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return True if arg in self.args_array else False


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__
        connect

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.current_log = "Log3"
        self.name = "ServerName"
        self.conn_msg = None

    def connect(self, silent=False):

        """Method:  connect

        Description:  connect method.

        Arguments:

        """

        status = True

        if silent:
            status = True

        return status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_connect_failure
        test_connect_success
        test_two_functions
        test_one_function

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args.args_array = {"-c": "mysql_cfg", "-d": "config", "-F": True}
        self.args2.args_array = {
            "-c": "mysql_cfg", "-d": "config", "-R": True, "-F": True}
        self.ord_prec_list = ["-F", "-K", "-M", "-A", "-S", "-R"]
        self.func_names = {"-F": flush_log_bkp, "-K": missing_log,
                           "-M": bkp_log_miss, "-A": bkp_log_all,
                           "-S": purge_log_day, "-R": purge_log_name}

    @mock.patch("mysql_binlog.mysql_libs.create_instance")
    def test_connect_failure(self, mock_inst):

        """Function:  test_connect_failure

        Description:  Test with failed connection.

        Arguments:

        """

        self.server.conn_msg = "Error connection message"

        mock_inst.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(mysql_binlog.run_program(
                self.args, self.func_names, self.ord_prec_list))

    @mock.patch("mysql_binlog.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_binlog.mysql_libs.create_instance")
    def test_connect_success(self, mock_inst):

        """Function:  test_connect_success

        Description:  Test with successful connection.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(mysql_binlog.run_program(
            self.args, self.func_names, self.ord_prec_list))

    @mock.patch("mysql_binlog.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_binlog.mysql_libs.create_instance")
    def test_two_functions(self, mock_inst):

        """Function:  test_two_functions

        Description:  Test with two function call.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(mysql_binlog.run_program(
            self.args2, self.func_names, self.ord_prec_list))

    @mock.patch("mysql_binlog.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_binlog.mysql_libs.create_instance")
    def test_one_function(self, mock_inst):

        """Function:  test_one_function

        Description:  Test with one function call.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(mysql_binlog.run_program(
            self.args, self.func_names, self.ord_prec_list))


if __name__ == "__main__":
    unittest.main()
