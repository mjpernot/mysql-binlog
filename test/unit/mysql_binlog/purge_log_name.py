#!/usr/bin/python
# Classification (U)

"""Program:  purge_log_name.py

    Description:  Unit testing of purge_log_name in mysql_binlog.py.

    Usage:
        test/unit/mysql_binlog/purge_log_name.py

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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.current_log = "Log3"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_no_log -> Test with no log to purge.
        test_purge -> Test with purging a file.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.log_list = ["Log1", "Log2", "Log3"]
        self.args_array = {"-R": "Log1"}
        self.args_array2 = {"-R": "Log4"}

    @mock.patch("mysql_binlog.mysql_libs.purge_bin_logs",
                mock.Mock(return_value=True))
    @mock.patch("mysql_binlog.fetch_all_logs")
    def test_no_log(self, mock_fetch):

        """Function:  test_no_log

        Description:  Test with no log to purge.

        Arguments:

        """

        mock_fetch.return_value = self.log_list

        with gen_libs.no_std_out():
            self.assertFalse(mysql_binlog.purge_log_name(self.args_array2,
                                                         self.server))

    @mock.patch("mysql_binlog.mysql_libs.purge_bin_logs",
                mock.Mock(return_value=True))
    @mock.patch("mysql_binlog.fetch_all_logs")
    def test_purge(self, mock_fetch):

        """Function:  test_purge

        Description:  Test with purging a file.

        Arguments:

        """

        mock_fetch.return_value = self.log_list

        self.assertFalse(mysql_binlog.purge_log_name(self.args_array,
                                                     self.server))


if __name__ == "__main__":
    unittest.main()
