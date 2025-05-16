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
            self.assertEqual(tc['classname'], 'UTEST-Init-Runner')
            self.assertEqual(tc['file'], 'utest_Init_Runner.c')
            self.assertEqual(tc['line'], '1')
            self.assertEqual(tc['result'], 'PASS')
            self.assertEqual(tc['name'], 'SWUTEST_INIT-RUNNER-TEST')
            self.assertEqual(tc['suite'], 'Init-Runner')
        self.assertEqual(default_suite_name, 'Init-Runner')

if __name__ == '__main__':
    unittest.main()
