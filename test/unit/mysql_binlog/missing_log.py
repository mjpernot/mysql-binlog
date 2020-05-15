#!/usr/bin/python
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
        setUp -> Initialize testing environment.
        test_all_missing -> Test with all missing logs.
        test_one_missing -> Test with one missing log.
        test_no_missing -> Test with no missing logs.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-o": True}
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
            self.assertFalse(mysql_binlog.missing_log(self.args_array,
                                                      self.server))

    @mock.patch("mysql_binlog.fetch_miss_logs")
    def test_one_missing(self, mock_fetch):

        """Function:  test_one_missing

        Description:  Test with one missing log.

        Arguments:

        """

        mock_fetch.return_value = self.miss_logs2

        with gen_libs.no_std_out():
            self.assertFalse(mysql_binlog.missing_log(self.args_array,
                                                      self.server))

    @mock.patch("mysql_binlog.fetch_miss_logs")
    def test_no_missing(self, mock_fetch):

        """Function:  test_no_missing

        Description:  Test with no missing logs.

        Arguments:

        """

        mock_fetch.return_value = self.miss_logs3

        self.assertFalse(mysql_binlog.missing_log(self.args_array,
                                                  self.server))


if __name__ == "__main__":
    unittest.main()
