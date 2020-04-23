#!/usr/bin/python
# Classification (U)

"""Program:  fetch_bkp_logs.py

    Description:  Unit testing of fetch_bkp_logs in mysql_binlog.py.

    Usage:
        test/unit/mysql_binlog/fetch_bkp_logs.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_file_list -> Test with default file list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dir_path = "/dir/path"
        self.file_list = ["File1.txt", "File2.txt"]
        self.file_list2 = ["File1.txt", "File2.txt.gz"]
        self.results = self.file_list

    @mock.patch("mysql_binlog.gen_libs.list_files")
    def test_gz_file(self, mock_list):

        """Function:  test_gz_file

        Description:  Test with gz in file list.

        Arguments:

        """

        mock_list.return_value = self.file_list2

        self.assertEqual(mysql_binlog.fetch_bkp_logs(self.dir_path),
                         self.results)

    @mock.patch("mysql_binlog.gen_libs.list_files")
    def test_file_list(self, mock_list):

        """Function:  test_file_list

        Description:  Test with default file list.

        Arguments:

        """

        mock_list.return_value = self.file_list

        self.assertEqual(mysql_binlog.fetch_bkp_logs(self.dir_path),
                         self.results)


if __name__ == "__main__":
    unittest.main()
