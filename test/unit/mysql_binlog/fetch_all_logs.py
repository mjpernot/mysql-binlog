# Classification (U)

"""Program:  fetch_all_logs.py

    Description:  Unit testing of fetch_all_logs in mysql_binlog.py.

    Usage:
        test/unit/mysql_binlog/fetch_all_logs.py

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
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():                                         # pylint:disable=R0903

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_single_item
        test_empty_list
        test_log_return

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.log_dict = [{"Log1": True, "Log_name": "BinLog1"},
                         {"Log2": True, "Log_name": "BinLog2"}]
        self.log_dict2 = [{"Log1": True, "Log_name": "BinLog1"}]
        self.server = Server()
        self.results = ["BinLog1", "BinLog2"]
        self.results2 = ["BinLog1"]

    @mock.patch("mysql_binlog.mysql_libs.fetch_logs")
    def test_single_item(self, mock_fetch):

        """Function:  test_single_item

        Description:  Test with single item in list.

        Arguments:

        """

        mock_fetch.return_value = self.log_dict2

        self.assertEqual(mysql_binlog.fetch_all_logs(self.server),
                         self.results2)

    @mock.patch("mysql_binlog.mysql_libs.fetch_logs")
    def test_empty_list(self, mock_fetch):

        """Function:  test_empty_list

        Description:  Test with no logs.

        Arguments:

        """

        mock_fetch.return_value = []

        self.assertEqual(mysql_binlog.fetch_all_logs(self.server), [])

    @mock.patch("mysql_binlog.mysql_libs.fetch_logs")
    def test_log_return(self, mock_fetch):

        """Function:  test_log_return

        Description:  Test with successful log return.

        Arguments:

        """

        mock_fetch.return_value = self.log_dict

        self.assertEqual(mysql_binlog.fetch_all_logs(self.server),
                         self.results)


if __name__ == "__main__":
    unittest.main()
