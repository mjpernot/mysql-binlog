#!/usr/bin/python
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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_compress_file -> Test with compression option.
        test_copy_file -> Test with default configuration.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-l": True, "-o": "./"}
        self.args_array2 = {"-l": True, "-o": "./", "-z": True}
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

        self.assertFalse(mysql_binlog.cp_zip_file(self.args_array2,
                                                  self.fname))

    @mock.patch("mysql_binlog.gen_libs.cp_file2",
                mock.Mock(return_value=True))
    def test_copy_file(self):

        """Function:  test_copy_file

        Description:  Test with default configuration.

        Arguments:

        """

        self.assertFalse(mysql_binlog.cp_zip_file(self.args_array, self.fname))


if __name__ == "__main__":
    unittest.main()
