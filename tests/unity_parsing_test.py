#!/usr/bin/env python3
''' Test suite for functions that set the prefix and prefix_set variables '''
import unittest
import tempfile
from unittest.mock import patch
from pathlib import Path
from datetime import datetime, timezone
from mlx.unity2junit.unity2junit import Unity2Junit

TEST_IN_DIR = Path(__file__).parent / 'test_in'


class TestUnityParsing(unittest.TestCase):
    """Test suite for the Unity log parsing functionality."""

    def test_parsing_unity_log_and_building_testcases(self):
        '''Verify that a Unity log file is parsed correctly into test case objects when utest_Something.c is used and
        that Something is used as the default testsuite name.'''

        with tempfile.NamedTemporaryFile(mode='w', delete=True) as tmp_output_file:
            converter = Unity2Junit(TEST_IN_DIR / 'utest_Init_Runner.log', tmp_output_file.name)
            converter.parse_unity_output()
            test_cases = converter.test_cases

            expected_test_cases_Init_Runner = {}
            expected_test_cases_Init_Runner['classname'] = [
                'INIT.SWUTEST_INIT-TEST_INIT_SUCCESS', 'INIT.SWUTEST_INIT-TEST_INIT_WRONG_EEPROM_VERSION',
                'INIT.SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS', 'INIT.SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS2',
                'INIT.SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS3']
            expected_test_cases_Init_Runner['line'] = ['49', '124', '135', '145', '163']
            expected_test_cases_Init_Runner['name'] = ['SWUTEST_INIT-TEST_INIT_SUCCESS',
                                                       'SWUTEST_INIT-TEST_INIT_WRONG_EEPROM_VERSION',
                                                       'SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS',
                                                       'SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS2',
                                                       'SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS3']

            for tc in test_cases:
                # Find some smart way to check the test case class, name and line number
                self.assertEqual(tc['classname'], expected_test_cases_Init_Runner['classname'].pop(0))
                self.assertEqual(tc['line'], expected_test_cases_Init_Runner['line'].pop(0))
                self.assertEqual(tc['name'], expected_test_cases_Init_Runner['name'].pop(0))

                self.assertEqual(tc['file'], 'unit_test/utest_Init.c')
                self.assertEqual(tc['result'], 'PASS')
                self.assertEqual(tc['suite'], 'INIT')

            self.assertEqual(converter.default_suite_name, 'INIT')
            self.assertEqual(converter.total_tests, 5)
            self.assertEqual(converter.failures, 0)
            self.assertEqual(converter.skipped, 0)

    def test_parsing_unity_log_and_building_testcases_no_name(self):
        '''Verify that a Unity log file is parsed correctly into test case objects when utest.c is used and that the
        default testsuite name is UTEST instead of empty.'''

        with tempfile.NamedTemporaryFile(mode='w', delete=True) as tmp_output_file:
            converter = Unity2Junit(TEST_IN_DIR / 'utest_Noname_Runner.log', tmp_output_file.name)
            converter.parse_unity_output()
            test_cases = converter.test_cases

            expected_test_cases_Noname_Runner = {}
            expected_test_cases_Noname_Runner['classname'] = [
                'UTEST.SWUTEST_UTEST-TEST_INIT_SUCCESS', 'UTEST.SWUTEST_UTEST-TEST_INIT_WRONG_EEPROM_VERSION',
                'UTEST.SWUTEST_UTEST-TEST_INIT_I2C_READ_FAILS', 'UTEST.SWUTEST_UTEST-TEST_INIT_I2C_READ_FAILS2',
                'UTEST.SWUTEST_UTEST-TEST_INIT_I2C_READ_FAILS3']
            expected_test_cases_Noname_Runner['line'] = ['49', '124', '135', '145', '163']
            expected_test_cases_Noname_Runner['name'] = ['SWUTEST_UTEST-TEST_INIT_SUCCESS',
                                                         'SWUTEST_UTEST-TEST_INIT_WRONG_EEPROM_VERSION',
                                                         'SWUTEST_UTEST-TEST_INIT_I2C_READ_FAILS',
                                                         'SWUTEST_UTEST-TEST_INIT_I2C_READ_FAILS2',
                                                         'SWUTEST_UTEST-TEST_INIT_I2C_READ_FAILS3']

            for tc in test_cases:
                # Find some smart way to check the test case class name
                self.assertEqual(tc['classname'], expected_test_cases_Noname_Runner['classname'].pop(0))
                self.assertEqual(tc['line'], expected_test_cases_Noname_Runner['line'].pop(0))
                self.assertEqual(tc['name'], expected_test_cases_Noname_Runner['name'].pop(0))

                self.assertEqual(tc['file'], 'unit_test/utest.c')
                self.assertEqual(tc['result'], 'PASS')
                self.assertEqual(tc['suite'], 'UTEST')

            self.assertEqual(converter.default_suite_name, 'UTEST')
            self.assertEqual(converter.total_tests, 5)
            self.assertEqual(converter.failures, 0)
            self.assertEqual(converter.skipped, 0)

    def test_parsing_unity_log_and_building_testcases_failed(self):
        '''Verify that a Unity log file is parsed correctly into test case objects when utest_Something.c is used and
        that Something is used as the default testsuite name.'''

        with tempfile.NamedTemporaryFile(mode='w', delete=True) as tmp_output_file:
            converter = Unity2Junit(TEST_IN_DIR / 'utest_Failed_Runner.log', tmp_output_file.name)
            converter.parse_unity_output()
            test_cases = converter.test_cases

            expected_test_cases_Failed_Runner = {}
            expected_test_cases_Failed_Runner['classname'] = [
                'INIT.SWUTEST_INIT-TEST_INIT_SUCCESS', 'INIT.SWUTEST_INIT-TEST_INIT_WRONG_EEPROM_VERSION',
                'INIT.SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS', 'INIT.SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS2',
                'INIT.SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS3']
            expected_test_cases_Failed_Runner['line'] = ['49', '124', '135', '145', '163']
            expected_test_cases_Failed_Runner['name'] = ['SWUTEST_INIT-TEST_INIT_SUCCESS',
                                                         'SWUTEST_INIT-TEST_INIT_WRONG_EEPROM_VERSION',
                                                         'SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS',
                                                         'SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS2',
                                                         'SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS3']
            expected_test_cases_Failed_Runner['result'] = ['PASS', 'PASS', 'FAIL', 'PASS', 'PASS']

            for tc in test_cases:
                # Find some smart way to check the test case class, name and line number
                self.assertEqual(tc['classname'], expected_test_cases_Failed_Runner['classname'].pop(0))
                self.assertEqual(tc['line'], expected_test_cases_Failed_Runner['line'].pop(0))
                self.assertEqual(tc['name'], expected_test_cases_Failed_Runner['name'].pop(0))
                self.assertEqual(tc['result'], expected_test_cases_Failed_Runner['result'].pop(0))

                self.assertEqual(tc['file'], 'unit_test/utest_Init.c')

                self.assertEqual(tc['suite'], 'INIT')

            self.assertEqual(converter.default_suite_name, 'INIT')
            self.assertEqual(converter.total_tests, 5)
            self.assertEqual(converter.failures, 1)
            self.assertEqual(converter.skipped, 0)

    def test_init_runner_output(self):
        '''Verify that utest_Init_Runner.log is converted to utest_Init_Runner.xml on a fixed timestamp of
        2025-09-25T13:40:24.403458+00:00'''
        fixed_timestamp_str = "2025-09-25T13:40:24.403458"  # Taken from utest_Init_Runner.xml
        fixed_datetime = datetime.fromisoformat(fixed_timestamp_str).replace(tzinfo=timezone.utc)
        expected_xml = ''

        with open(TEST_IN_DIR / 'utest_Init_Runner.xml', 'r', encoding='utf-8') as f:
            expected_xml = f.readlines()

        with tempfile.NamedTemporaryFile(mode='w+', delete=True, encoding='utf-8') as tmp_output_file:
            with patch('mlx.unity2junit.unity2junit.datetime') as mock_dt:
                mock_dt.now.return_value = fixed_datetime
                converter = Unity2Junit(TEST_IN_DIR / 'utest_Init_Runner.log', tmp_output_file.name)
                converter.convert()
                tmp_output_file.seek(0)
                generated_xml = tmp_output_file.readlines()
                self.assertListEqual(generated_xml, expected_xml)

    def test_force_test_case_prefix(self):
        ''' Verify that when a prefix is forced, it is used as the testsuite name.'''
        with tempfile.NamedTemporaryFile(mode='w', delete=True) as tmp_output_file:
            converter = Unity2Junit(TEST_IN_DIR / 'utest_Init_Runner.log', tmp_output_file.name,
                                    tc_prefix="FORCED_PREFIX-")
            converter.parse_unity_output()
            test_cases = converter.test_cases

            expected_test_cases_Init_Runner = {}
            expected_test_cases_Init_Runner['classname'] = [
                'INIT.FORCED_PREFIX-TEST_INIT_SUCCESS', 'INIT.FORCED_PREFIX-TEST_INIT_WRONG_EEPROM_VERSION',
                'INIT.FORCED_PREFIX-TEST_INIT_I2C_READ_FAILS', 'INIT.FORCED_PREFIX-TEST_INIT_I2C_READ_FAILS2',
                'INIT.FORCED_PREFIX-TEST_INIT_I2C_READ_FAILS3']
            expected_test_cases_Init_Runner['line'] = ['49', '124', '135', '145', '163']
            expected_test_cases_Init_Runner['name'] = ['FORCED_PREFIX-TEST_INIT_SUCCESS',
                                                       'FORCED_PREFIX-TEST_INIT_WRONG_EEPROM_VERSION',
                                                       'FORCED_PREFIX-TEST_INIT_I2C_READ_FAILS',
                                                       'FORCED_PREFIX-TEST_INIT_I2C_READ_FAILS2',
                                                       'FORCED_PREFIX-TEST_INIT_I2C_READ_FAILS3']

            for tc in test_cases:
                # Find some smart way to check the test case class, name and line number
                self.assertEqual(tc['classname'], expected_test_cases_Init_Runner['classname'].pop(0))
                self.assertEqual(tc['line'], expected_test_cases_Init_Runner['line'].pop(0))
                self.assertEqual(tc['name'], expected_test_cases_Init_Runner['name'].pop(0))
                self.assertEqual(tc['result'], 'PASS')

                self.assertEqual(tc['file'], 'unit_test/utest_Init.c')
                self.assertEqual(tc['suite'], 'INIT')  # The suite in test cases remains the same

    def test_force_test_case_prefix_noname(self):
        ''' Verify that when a prefix is forced, it is used as the testsuite name even when utest.c is used.'''
        with tempfile.NamedTemporaryFile(mode='w', delete=True) as tmp_output_file:
            converter = Unity2Junit(TEST_IN_DIR / 'utest_Noname_Runner.log', tmp_output_file.name,
                                    tc_prefix="FORCED_PREFIX-")
            converter.parse_unity_output()
            test_cases = converter.test_cases

            expected_test_cases_Noname_Runner = {}
            expected_test_cases_Noname_Runner['classname'] = [
                'UTEST.FORCED_PREFIX-TEST_INIT_SUCCESS', 'UTEST.FORCED_PREFIX-TEST_INIT_WRONG_EEPROM_VERSION',
                'UTEST.FORCED_PREFIX-TEST_INIT_I2C_READ_FAILS', 'UTEST.FORCED_PREFIX-TEST_INIT_I2C_READ_FAILS2',
                'UTEST.FORCED_PREFIX-TEST_INIT_I2C_READ_FAILS3']
            expected_test_cases_Noname_Runner['line'] = ['49', '124', '135', '145', '163']
            expected_test_cases_Noname_Runner['name'] = ['FORCED_PREFIX-TEST_INIT_SUCCESS',
                                                         'FORCED_PREFIX-TEST_INIT_WRONG_EEPROM_VERSION',
                                                         'FORCED_PREFIX-TEST_INIT_I2C_READ_FAILS',
                                                         'FORCED_PREFIX-TEST_INIT_I2C_READ_FAILS2',
                                                         'FORCED_PREFIX-TEST_INIT_I2C_READ_FAILS3']

            for tc in test_cases:
                # Find some smart way to check the test case class, name and line number
                self.assertEqual(tc['classname'], expected_test_cases_Noname_Runner['classname'].pop(0))
                self.assertEqual(tc['line'], expected_test_cases_Noname_Runner['line'].pop(0))
                self.assertEqual(tc['name'], expected_test_cases_Noname_Runner['name'].pop(0))
                self.assertEqual(tc['result'], 'PASS')

                self.assertEqual(tc['file'], 'unit_test/utest.c')
                self.assertEqual(tc['suite'], 'UTEST')  # The suite in test cases remains the same

    def test_force_test_case_prefix_empty(self):
        ''' Verify that when an empty prefix is forced, the default prefix is used as the testsuite name.'''
        with tempfile.NamedTemporaryFile(mode='w', delete=True) as tmp_output_file:
            converter = Unity2Junit(TEST_IN_DIR / 'utest_Init_Runner.log', tmp_output_file.name,
                                    tc_prefix="")
            converter.parse_unity_output()
            test_cases = converter.test_cases

            expected_test_cases_Init_Runner = {}
            expected_test_cases_Init_Runner['classname'] = [
                'INIT.TEST_INIT_SUCCESS', 'INIT.TEST_INIT_WRONG_EEPROM_VERSION',
                'INIT.TEST_INIT_I2C_READ_FAILS', 'INIT.TEST_INIT_I2C_READ_FAILS2',
                'INIT.TEST_INIT_I2C_READ_FAILS3']
            expected_test_cases_Init_Runner['line'] = ['49', '124', '135', '145', '163']
            expected_test_cases_Init_Runner['name'] = ['TEST_INIT_SUCCESS',
                                                       'TEST_INIT_WRONG_EEPROM_VERSION',
                                                       'TEST_INIT_I2C_READ_FAILS',
                                                       'TEST_INIT_I2C_READ_FAILS2',
                                                       'TEST_INIT_I2C_READ_FAILS3']

            for tc in test_cases:
                # Find some smart way to check the test case class, name and line number
                self.assertEqual(tc['classname'], expected_test_cases_Init_Runner['classname'].pop(0))
                self.assertEqual(tc['line'], expected_test_cases_Init_Runner['line'].pop(0))
                self.assertEqual(tc['name'], expected_test_cases_Init_Runner['name'].pop(0))
                self.assertEqual(tc['result'], 'PASS')

                self.assertEqual(tc['file'], 'unit_test/utest_Init.c')
                self.assertEqual(tc['suite'], 'INIT')  # The suite in test cases remains the same

    def test_force_test_case_prefix_empty_noname(self):
        ''' Verify that when an empty prefix is forced, the default prefix is used as the testsuite name even when
        utest.c is used.'''
        with tempfile.NamedTemporaryFile(mode='w', delete=True) as tmp_output_file:
            converter = Unity2Junit(TEST_IN_DIR / 'utest_Noname_Runner.log', tmp_output_file.name,
                                    tc_prefix="")
            converter.parse_unity_output()
            test_cases = converter.test_cases

            expected_test_cases_Noname_Runner = {}
            expected_test_cases_Noname_Runner['classname'] = [
                'UTEST.TEST_INIT_SUCCESS', 'UTEST.TEST_INIT_WRONG_EEPROM_VERSION',
                'UTEST.TEST_INIT_I2C_READ_FAILS', 'UTEST.TEST_INIT_I2C_READ_FAILS2',
                'UTEST.TEST_INIT_I2C_READ_FAILS3']
            expected_test_cases_Noname_Runner['line'] = ['49', '124', '135', '145', '163']
            expected_test_cases_Noname_Runner['name'] = ['TEST_INIT_SUCCESS',
                                                         'TEST_INIT_WRONG_EEPROM_VERSION',
                                                         'TEST_INIT_I2C_READ_FAILS',
                                                         'TEST_INIT_I2C_READ_FAILS2',
                                                         'TEST_INIT_I2C_READ_FAILS3']

            for tc in test_cases:
                # Find some smart way to check the test case class, name and line number
                self.assertEqual(tc['classname'], expected_test_cases_Noname_Runner['classname'].pop(0))
                self.assertEqual(tc['line'], expected_test_cases_Noname_Runner['line'].pop(0))
                self.assertEqual(tc['name'], expected_test_cases_Noname_Runner['name'].pop(0))
                self.assertEqual(tc['result'], 'PASS')

                self.assertEqual(tc['file'], 'unit_test/utest.c')
                self.assertEqual(tc['suite'], 'UTEST')  # The suite in test cases remains the same


if __name__ == '__main__':
    unittest.main()
