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
import mysql_binlog                             # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_cond_req
        arg_dir_chk
        arg_exist
        arg_require
        get_args_keys
        arg_noreq_xor
        get_val
        insert_arg

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = {}
        self.opt_con_req = None
        self.opt_con_req2 = True
        self.opt_req = None
        self.opt_req2 = True
        self.dir_perms_chk = None
        self.dir_perms_chk2 = True
        self.xor_noreq = None
        self.xor_noreq2 = True

    def arg_cond_req(self, opt_con_req):

        """Method:  arg_cond_req

        Description:  Method stub holder for gen_class.ArgParser.arg_cond_req.

        Arguments:

        """

        self.opt_con_req = opt_con_req

        return self.opt_con_req2

    def arg_dir_chk(self, dir_perms_chk):

        """Method:  arg_dir_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_chk.

        Arguments:

        """

        self.dir_perms_chk = dir_perms_chk

        return self.dir_perms_chk2

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return arg in self.args_array

    def arg_require(self, opt_req):

        """Method:  arg_require

        Description:  Method stub holder for gen_class.ArgParser.arg_require.

        Arguments:

        """

        self.opt_req = opt_req

        return self.opt_req2

    def get_args_keys(self):

        """Method:  get_args_keys

        Description:  Method stub holder for gen_class.ArgParser.get_args_keys.

        Arguments:

        """

        return list(self.args_array.keys())

    def arg_noreq_xor(self, xor_noreq):

        """Method:  arg_noreq_xor

        Description:  Method stub holder for gen_class.ArgParser.arg_noreq_xor.

        Arguments:

        """

        self.xor_noreq = xor_noreq

        return self.xor_noreq2

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def insert_arg(self, arg_key, arg_val):

        """Method:  insert_arg

        Description:  Method stub holder for gen_class.ArgParser.insert_arg.

        Arguments:

        """

        self.args_array[arg_key] = arg_val


class Cfg():                                            # pylint:disable=R0903

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


class ProgramLock():                                    # pylint:disable=R0903

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
        test_arg_req_false
        test_arg_req_true
        test_arg_noreq_xor_false
        test_arg_noreq_xor_true
        test_arg_cond_req_false
        test_arg_cond_req_true
        test_arg_dir_chk_crt_false
        test_arg_dir_chk_crt_true
        test_run_program
        test_programlock_id
        test_programlock_fail

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args.args_array = {"-c": "CfgFile", "-d": "CfgDir"}
        self.args2.args_array = {
            "-c": "CfgFile", "-d": "CfgDir", "-l": "/path"}
        self.args3.args_array = {"-c": "CfgFile", "-d": "CfgDir", "-M": True}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")
        self.cfg = Cfg()

    @mock.patch("mysql_binlog.gen_libs.load_module")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_binary_log2(self, mock_arg, mock_help, mock_cfg):

        """Function:  test_binary_log2

        Description:  Test with test_binary_log not set and no -l option
            passed.

        Arguments:

        """

        self.cfg.binary_log = None

        mock_arg.return_value = self.args3
        mock_help.return_value = True
        mock_cfg.return_value = self.cfg

        with gen_libs.no_std_out():
            self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.load_module")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_binary_log(self, mock_arg, mock_help, mock_cfg):

        """Function:  test_binary_log

        Description:  Test with test_binary_log set.

        Arguments:

        """

        mock_arg.return_value = self.args3
        mock_help.return_value = True
        mock_cfg.return_value = self.cfg

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.load_module")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_l_opt_req_options3(self, mock_arg, mock_help, mock_cfg):

        """Function:  test_l_opt_req_options3

        Description:  Test with no -l option, but with required options passed.

        Arguments:

        """

        mock_arg.return_value = self.args3
        mock_help.return_value = True
        mock_cfg.return_value = self.cfg

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_l_opt_req_options2(self, mock_arg, mock_help):

        """Function:  test_l_opt_req_options2

        Description:  Test with -l option and no required options passed.

        Arguments:

        """

        mock_arg.return_value = self.args2
        mock_help.return_value = True

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_l_opt_req_options(self, mock_arg, mock_help):

        """Function:  test_l_opt_req_options

        Description:  Test with no -l option and no required options passed.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_arg_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_arg_req_true(self, mock_arg, mock_help):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        self.args.xor_noreq2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_arg_noreq_xor_false(self, mock_arg, mock_help):

        """Function:  test_arg_noreq_xor_false

        Description:  Test arg_noreq_xor if returns false.

        Arguments:

        """

        self.args.xor_noreq2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_arg_noreq_xor_true(self, mock_arg, mock_help):

        """Function:  test_arg_noreq_xor_true

        Description:  Test arg_noreq_xor if returns true.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_arg_cond_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_cond_req_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_arg_cond_req_true(self, mock_arg, mock_help):

        """Function:  test_arg_cond_req_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_arg_dir_chk_crt_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_chk_crt_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_class.ProgramLock")
    @mock.patch("mysql_binlog.run_program")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_arg_dir_chk_crt_true(self, mock_arg, mock_help, mock_run,
                                  mock_lock):

        """Function:  test_arg_dir_chk_crt_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_run.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_class.ProgramLock")
    @mock.patch("mysql_binlog.run_program")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_run_program(self, mock_arg, mock_help, mock_run, mock_lock):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_run.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_class.ProgramLock")
    @mock.patch("mysql_binlog.run_program")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_programlock_id(self, mock_arg, mock_help, mock_run, mock_lock):

        """Function:  test_programlock_id

        Description:  Test run_program function.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_run.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(mysql_binlog.main())

    @mock.patch("mysql_binlog.gen_class.ProgramLock")
    @mock.patch("mysql_binlog.run_program")
    @mock.patch("mysql_binlog.gen_libs.help_func")
    @mock.patch("mysql_binlog.gen_class.ArgParser")
    def test_programlock_fail(self, mock_arg, mock_help, mock_run, mock_lock):

        """Function:  test_programlock_fail

        Description:  Test ProgramLock fails to lock.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_run.return_value = True
        mock_lock.side_effect = mysql_binlog.gen_class.SingleInstanceException

        with gen_libs.no_std_out():
            self.assertFalse(mysql_binlog.main())


if __name__ == "__main__":
    unittest.main()
