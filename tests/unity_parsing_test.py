#!/usr/bin/env python3
''' Test suite for functions that set the prefix and prefix_set variables '''
import unittest
import tempfile
from pathlib import Path

from mlx.unity2junit.unity2junit import Unity2Junit

TEST_IN_DIR = Path(__file__).parent / 'test_in'


class TestUnityParsing(unittest.TestCase):
    """Test suite for the Unity log parsing functionality."""

    def test_parsing_unity_log_and_building_testcases(self):
        '''Verify that a Unity log file is parsed correctly into test case objects.'''
        with tempfile.NamedTemporaryFile(mode='w', delete=True) as tmp_output_file:
            converter = Unity2Junit(TEST_IN_DIR / 'utest_Init_Runner.log', tmp_output_file.name)
            converter.parse_unity_output()
            test_cases = converter.test_cases

            expected_test_cases_Init_Runner = {}
            expected_test_cases_Init_Runner['classname'] = [
                'INIT.SWUTEST_INIT-TEST_INIT_SUCCESS', 'INIT.SWUTEST_INIT-TEST_INIT_WRONG_EEPROM_VERSION',
                'INIT.SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS', 'INIT.SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS2',
                'INIT.SWUTEST_INIT-TEST_INIT_I2C_READ_FAILS3']

            for tc in test_cases:
                # Find some smart way to check the test case class name
                self.assertEqual(tc['classname'], expected_test_cases_Init_Runner['classname'].pop(0))
                self.assertEqual(tc['file'], 'unit_test/utest_Init.c')
                # Find some smart way to check the line number
                # self.assertEqual(tc['line'], '1')
                self.assertEqual(tc['result'], 'PASS')
                # Find some smart way to check for the test name
                # self.assertEqual(tc['name'], 'SWUTEST_INIT-TEST_INIT_SUCCESS')
                self.assertEqual(tc['suite'], 'INIT')

            self.assertEqual(converter.default_suite_name, 'INIT')


if __name__ == '__main__':
    unittest.main()
