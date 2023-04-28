# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in mysql_binlog.py.

    Usage:
        test/unit/mysql_binlog/main.py

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


class Cfg(object):

    """Class:  Cfg

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the Cfg class.

        Arguments:

        """

        self.binary_log = "/opt/mysql/data"


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class stub holder for gen_class.ProgramLock class.

    Methods:
        __init__

    """

    def __init__(self, cmdline, flavor):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            (input) cmdline
            (input) flavor

        """

        self.cmdline = cmdline
        self.flavor = flavor


class CmdLine(object):

    """Class:  CmdLine

    Description:  Class which is a representation of a command line.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.argv = ["Program", "-c", "CfgFile", "-d", "CfgDir"]


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_binary_log2
        test_binary_log
        test_l_opt_req_options3
        test_l_opt_req_options2
        test_l_opt_req_options
        test_help_true
        test_help_false
        test_arg_req_true
        test_arg_req_false
        test_arg_noreq_xor_false
        test_arg_noreq_xor_true
        test_arg_cond_req_false
        test_arg_cond_req_true
        test_arg_dir_chk_crt_true
        test_arg_dir_chk_crt_false
        test_run_program
        test_programlock_id
        test_programlock_fail

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cmd_line = CmdLine()
        self.args_array = {"-c": "CfgFile", "-d": "CfgDir"}
        self.args_array2 = {"-c": "CfgFile", "-d": "CfgDir", "-l": "/path"}
        self.args_array3 = {"-c": "CfgFile", "-d": "CfgDir", "-M": True}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")
        self.cfg = Cfg()

    @mock.patch("mysql_binlog.gen_libs.load_module")
    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser.arg_parse2")
    def test_binary_log2(self, mock_arg, mock_help, mock_inst, mock_cfg):

        """Function:  test_binary_log2

        Description:  Test with test_binary_log not set.

        Arguments:

        """

        self.cfg.binary_log = None

        mock_arg.return_value = self.args_array3
        mock_help.return_value = True
        mock_inst.return_value = self.cmd_line
        mock_cfg.return_value = self.cfg

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.load_module")
    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser.arg_parse2")
    def test_binary_log(self, mock_arg, mock_help, mock_inst, mock_cfg):

        """Function:  test_binary_log

        Description:  Test with test_binary_log set.

        Arguments:

        """

        mock_arg.return_value = self.args_array3
        mock_help.return_value = True
        mock_inst.return_value = self.cmd_line
        mock_cfg.return_value = self.cfg

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.load_module")
    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser.arg_parse2")
    def test_l_opt_req_options3(self, mock_arg, mock_help, mock_inst,
                                mock_cfg):

        """Function:  test_l_opt_req_options3

        Description:  Test with no -l option, but with required options passed.

        Arguments:

        """

        mock_arg.return_value = self.args_array3
        mock_help.return_value = True
        mock_inst.return_value = self.cmd_line
        mock_cfg.return_value = self.cfg

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser.arg_parse2")
    def test_l_opt_req_options2(self, mock_arg, mock_help, mock_inst):

        """Function:  test_l_opt_req_options2

        Description:  Test with -l option and no required options passed.

        Arguments:

        """

        mock_arg.return_value = self.args_array2
        mock_help.return_value = True
        mock_inst.return_value = self.cmd_line

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser.arg_parse2")
    def test_l_opt_req_options(self, mock_arg, mock_help, mock_inst):

        """Function:  test_l_opt_req_options

        Description:  Test with no -l option and no required options passed.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = True
        mock_inst.return_value = self.cmd_line

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg, mock_help, mock_inst):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = True
        mock_inst.return_value = self.cmd_line

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.arg_parser.arg_require")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser.arg_parse2")
    def test_help_false(self, mock_arg, mock_help, mock_req, mock_inst):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = True
        mock_inst.return_value = self.cmd_line

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.arg_parser.arg_require")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser.arg_parse2")
    def test_arg_req_true(self, mock_arg, mock_help, mock_req, mock_inst):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = True
        mock_inst.return_value = self.cmd_line

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.arg_parser.arg_noreq_xor")
    @mock.patch("mysql_binlog.arg_parser.arg_require")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser.arg_parse2")
    def test_arg_req_false(self, mock_arg, mock_help, mock_req, mock_xor,
                           mock_inst):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = False
        mock_req.return_value = False
        mock_xor.return_value = False
        mock_inst.return_value = self.cmd_line

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser")
    def test_arg_noreq_xor_false(self, mock_arg, mock_help, mock_inst):

        """Function:  test_arg_noreq_xor_false

        Description:  Test arg_noreq_xor if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_noreq_xor.return_value = False
        mock_inst.return_value = self.cmd_line

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser")
    def test_arg_noreq_xor_true(self, mock_arg, mock_help, mock_inst):

        """Function:  test_arg_noreq_xor_true

        Description:  Test arg_noreq_xor if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = False
        mock_inst.return_value = self.cmd_line

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser")
    def test_arg_cond_req_false(self, mock_arg, mock_help, mock_inst):

        """Function:  test_arg_cond_req_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = False
        mock_inst.return_value = self.cmd_line

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser")
    def test_arg_cond_req_true(self, mock_arg, mock_help, mock_inst):

        """Function:  test_arg_cond_req_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = True
        mock_inst.return_value = self.cmd_line

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser")
    def test_arg_dir_chk_crt_true(self, mock_arg, mock_help, mock_inst):

        """Function:  test_arg_dir_chk_crt_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = True
        mock_inst.return_value = self.cmd_line

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_class.ProgramLock")
    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.run_program")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser")
    def test_arg_dir_chk_crt_false(self, mock_arg, mock_help, mock_run,
                                   mock_inst, mock_lock):

        """Function:  test_arg_dir_chk_crt_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True
        mock_inst.return_value = self.cmd_line
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_class.ProgramLock")
    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.run_program")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser")
    def test_run_program(self, mock_arg, mock_help, mock_run, mock_inst,
                         mock_lock):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True
        mock_inst.return_value = self.cmd_line
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_class.ProgramLock")
    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.run_program")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser")
    def test_programlock_id(self, mock_arg, mock_help, mock_run, mock_inst,
                            mock_lock):

        """Function:  test_programlock_id

        Description:  Test run_program function.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True
        mock_inst.return_value = self.cmd_line
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_class.ProgramLock")
    @mock.patch("mysql_binlog.gen_libs.get_inst")
    @mock.patch("mysql_binlog.run_program")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.arg_parser")
    def test_programlock_fail(self, mock_arg, mock_help, mock_run, mock_inst,
                              mock_lock):

        """Function:  test_programlock_fail

        Description:  Test ProgramLock fails to lock.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_noreq_xor.return_value = True
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True
        mock_inst.return_value = self.cmd_line
        mock_lock.side_effect = mysql_binlog.gen_class.SingleInstanceException

        with gen_libs.no_std_out():
            self.assertFalse(mysql_binlog.main())


if __name__ == "__main__":
    unittest.main()
