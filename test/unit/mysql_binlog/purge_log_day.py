#!/usr/bin/python
# Classification (U)

"""Program:  purge_log_day.py

    Description:  Unit testing of purge_log_day in mysql_binlog.py.

    Usage:
        test/unit/mysql_binlog/purge_log_day.py

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
        test_purge -> Test with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-S": "5"}

    @mock.patch("mysql_binlog.mysql_libs.purge_bin_logs",
                mock.Mock(return_value=True))
    def test_purge(self):

        """Function:  test_purge

        Description:  Test with default settings.

        Arguments:

        """

        self.assertFalse(mysql_binlog.purge_log_day(self.args_array,
                                                    self.server))


if __name__ == "__main__":
    unittest.main()
