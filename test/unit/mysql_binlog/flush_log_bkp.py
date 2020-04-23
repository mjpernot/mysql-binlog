#!/usr/bin/python
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
        fetch_log -> fetch_log function.
        flush_logs -> flush_logs function.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.call_return = True

    def fetch_log(self):

        """Method:  fetch_log

        Description:  fetch_log function.

        Arguments:

        """

        if self.call_return:
            self.call_return = False

            return "Binlog1"

        else:
            return "Binlog2"

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
        setUp -> Initialize testing environment.
        test_flush_successful -> Test with successful flush.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-l": True, "-o": "./"}
        self.server = Server()

    @mock.patch("mysql_binlog.cp_zip_file", mock.Mock(return_value=True))
    def test_flush_successful(self):

        """Function:  test_flush_successful

        Description:  Test with successful flush.

        Arguments:

        """

        self.assertFalse(mysql_binlog.flush_log_bkp(self.args_array,
                                                    self.server))


if __name__ == "__main__":
    unittest.main()
