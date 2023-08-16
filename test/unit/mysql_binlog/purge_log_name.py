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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_log
        test_purge

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args.args_array = {"-R": "Log1"}
        self.args2.args_array = {"-R": "Log4"}
        self.log_list = ["Log1", "Log2", "Log3"]

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
            self.assertFalse(
                mysql_binlog.purge_log_name(self.args2, self.server))

    @mock.patch("mysql_binlog.mysql_libs.purge_bin_logs",
                mock.Mock(return_value=True))
    @mock.patch("mysql_binlog.fetch_all_logs")
    def test_purge(self, mock_fetch):

        """Function:  test_purge

        Description:  Test with purging a file.

        Arguments:

        """

        mock_fetch.return_value = self.log_list

        self.assertFalse(mysql_binlog.purge_log_name(self.args, self.server))


if __name__ == "__main__":
    unittest.main()
