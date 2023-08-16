# Classification (U)

"""Program:  fetch_miss_logs.py

    Description:  Unit testing of fetch_miss_logs in mysql_binlog.py.

    Usage:
        test/unit/mysql_binlog/fetch_miss_logs.py

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
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

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
        self.bkp_logs = ["Log1", "Log2"]
        self.bkp_logs2 = ["Log1"]
        self.bkp_logs3 = []
        self.log_list = ["Log1", "Log2", "Log3"]
        self.results = ["Log2"]
        self.results2 = self.bkp_logs

    @mock.patch("mysql_binlog.fetch_bkp_logs")
    @mock.patch("mysql_binlog.fetch_all_logs")
    def test_all_missing(self, mock_fetch, mock_bkp):

        """Function:  test_all_missing

        Description:  Test with all missing logs.

        Arguments:

        """

        mock_fetch.return_value = self.log_list
        mock_bkp.return_value = self.bkp_logs3

        self.assertEqual(
            mysql_binlog.fetch_miss_logs(
                self.args, self.server), self.results2)

    @mock.patch("mysql_binlog.fetch_bkp_logs")
    @mock.patch("mysql_binlog.fetch_all_logs")
    def test_one_missing(self, mock_fetch, mock_bkp):

        """Function:  test_one_missing

        Description:  Test with one missing log.

        Arguments:

        """

        mock_fetch.return_value = self.log_list
        mock_bkp.return_value = self.bkp_logs2

        self.assertEqual(
            mysql_binlog.fetch_miss_logs(self.args, self.server), self.results)

    @mock.patch("mysql_binlog.fetch_bkp_logs")
    @mock.patch("mysql_binlog.fetch_all_logs")
    def test_no_missing(self, mock_fetch, mock_bkp):

        """Function:  test_no_missing

        Description:  Test with no missing logs.

        Arguments:

        """

        mock_fetch.return_value = self.log_list
        mock_bkp.return_value = self.bkp_logs

        self.assertEqual(
            mysql_binlog.fetch_miss_logs(self.args, self.server), [])


if __name__ == "__main__":
    unittest.main()
