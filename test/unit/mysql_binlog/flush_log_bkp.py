# Classification (U)

"""Program:  flush_log_bkp.py

    Description:  Unit testing of flush_log_bkp in mysql_binlog.py.

    Usage:
        test/unit/mysql_binlog/flush_log_bkp.py

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
import mysql_binlog                             # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = {}


class Server():

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__
        fetch_log
        flush_logs

    """

    def __init__(self, change=True):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            (input) change

        """

        self.call_return = change
        self.log = "Binlog1"

    def fetch_log(self):

        """Method:  fetch_log

        Description:  fetch_log function.

        Arguments:

        """

        data = self.log

        if self.call_return:
            self.log = "Binlog2"

        return data

    def flush_logs(self):

        """Method:  flush_logs

        Description:  flush_logs function.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_flush_fails
        test_flush_successful

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args.args_array = {"-l": True, "-o": "./"}
        self.server = Server()
        self.server2 = Server(False)

    def test_flush_fails(self):

        """Function:  test_flush_fails

        Description:  Test with failed flush.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_binlog.flush_log_bkp(self.args, self.server2))

    @mock.patch("mysql_binlog.cp_zip_file", mock.Mock(return_value=True))
    def test_flush_successful(self):

        """Function:  test_flush_successful

        Description:  Test with successful flush.

        Arguments:

        """

        self.assertFalse(mysql_binlog.flush_log_bkp(self.args, self.server))


if __name__ == "__main__":
    unittest.main()
