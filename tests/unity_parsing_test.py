#!/usr/bin/env python3
''' Test suite for functions that set the prefix and prefix_set variables '''
import unittest
from pathlib import Path

from mlx.unity2junit import unity2junit as dut

TEST_IN_DIR = Path(__file__).parent / 'test_in'


class TestUnityParsing(unittest.TestCase):

    def test_parsing_unity_log_and_building_testcases(self):
        ''' Use default prefix for unit test reports '''
        test_cases, default_suite_name = dut.parse_unity_output(TEST_IN_DIR / 'utest_Init_Runner.log')

        for tc in test_cases:
            # Find some smart way to check the test case class name
            # self.assertEqual(tc['classname'], 'INIT.SWUTEST_INIT-TEST_INIT_SUCCESS')
            self.assertEqual(tc['file'], 'unit_test/utest_Init.c')
            # Find some smart way to check the line number
            # self.assertEqual(tc['line'], '1')
            self.assertEqual(tc['result'], 'PASS')
            # Find some smart way to check for the test name
            # self.assertEqual(tc['name'], 'SWUTEST_INIT-TEST_INIT_SUCCESS')
            self.assertEqual(tc['suite'], 'INIT')

        self.assertEqual(default_suite_name, 'INIT')


if __name__ == '__main__':
    unittest.main()
