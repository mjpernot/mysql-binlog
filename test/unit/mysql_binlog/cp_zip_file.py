# Classification (U)

"""Program:  cp_zip_file.py

    Description:  Unit testing of cp_zip_file in mysql_binlog.py.

    Usage:
        test/unit/mysql_binlog/cp_zip_file.py

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


class ArgParser():

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
        self.args_array = {}

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

        return arg in self.args_array


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_compress_file
        test_copy_file

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args.args_array = {"-l": True, "-o": "./"}
        self.args2.args_array = {"-l": True, "-o": "./", "-z": True}
        self.fname = "FileName"

    @mock.patch("mysql_binlog.gen_libs.compress",
                mock.Mock(return_value=True))
    @mock.patch("mysql_binlog.gen_libs.cp_file2",
                mock.Mock(return_value=True))
    def test_compress_file(self):

        """Function:  test_compress_file

        Description:  Test with compression option.

        Arguments:

        """

        self.assertFalse(mysql_binlog.cp_zip_file(self.args2, self.fname))

    @mock.patch("mysql_binlog.gen_libs.cp_file2",
                mock.Mock(return_value=True))
    def test_copy_file(self):

        """Function:  test_copy_file

        Description:  Test with default configuration.

        Arguments:

        """

        self.assertFalse(mysql_binlog.cp_zip_file(self.args, self.fname))


if __name__ == "__main__":
    unittest.main()
