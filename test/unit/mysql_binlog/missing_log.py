# Classification (U)

"""Program:  missing_log.py

    Description:  Unit testing of missing_log in mysql_binlog.py.

    Usage:
        test/unit/mysql_binlog/missing_log.py

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


class ArgParser(object):

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
        self.args_array = dict()


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.current_log = "Log3"

    def fetch_log(self):

        """Method:  fetch_log

        Description:  fetch_log function.

        Arguments:

        """

        return self.current_log


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_all_missing
        test_one_missing
        test_no_missing

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.args.args_array = {"-o": True}
        self.miss_logs = ["Log1", "Log2"]
        self.miss_logs2 = ["Log1"]
        self.miss_logs3 = []

    @mock.patch("mysql_binlog.fetch_miss_logs")
    def test_all_missing(self, mock_fetch):

        """Function:  test_all_missing

        Description:  Test with all missing logs.

        Arguments:

        """

        mock_fetch.return_value = self.miss_logs

        with gen_libs.no_std_out():
            self.assertFalse(mysql_binlog.missing_log(self.args, self.server))

    @mock.patch("mysql_binlog.fetch_miss_logs")
    def test_one_missing(self, mock_fetch):

        """Function:  test_one_missing

        Description:  Test with one missing log.

        Arguments:

        """

        mock_fetch.return_value = self.miss_logs2

        with gen_libs.no_std_out():
            self.assertFalse(mysql_binlog.missing_log(self.args, self.server))

    @mock.patch("mysql_binlog.fetch_miss_logs")
    def test_no_missing(self, mock_fetch):

        """Function:  test_no_missing

        Description:  Test with no missing logs.

        Arguments:

        """

        mock_fetch.return_value = self.miss_logs3

        self.assertFalse(mysql_binlog.missing_log(self.args, self.server))


if __name__ == "__main__":
    unittest.main()
