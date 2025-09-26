#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0

import argparse
from datetime import datetime
from importlib.metadata import version
import os
import re
import xml.etree.ElementTree as ET


__version__ = version("mlx-unity2junit")


class Unity2Junit:
    """Converts a Unity test output log to a JUnit XML report."""
    def __init__(self, log_file, output_file, tc_prefix=""):
        self.log_file = log_file
        self.output_file = output_file
        self.test_cases = []
        self.default_suite_name = "EMPTY"
        self.total_tests = 0
        self.failures = 0
        self.skipped = 0
        self.test_case_prefix = tc_prefix

    def parse_unity_output(self):
        """Parses the Unity log file and populates test case data."""
        with open(self.log_file, "r") as f:
            for line in f:
                match = re.match(r"(.+):(\d+):(.+):(PASS|FAIL|SKIP)(?:(.+))?", line)
                if match:
                    file_path, line_number, test_name, result, reason = match.groups()
                    self.total_tests += 1

                    # Extract filename without extension
                    filename = os.path.basename(file_path).replace("utest_", "").split('.')[0].upper()
                    self.default_suite_name = filename  # Set the default testsuite name

                    if not self.test_case_prefix:
                        self.test_case_prefix = f"SWUTEST_{filename}-"

                    # Modify the test name: replace the underscore between SWUTEST_ and the next part with a hyphen
                    formatted_test_name = f"{self.test_case_prefix}{test_name.upper()}"

                    test_case = {
                        "name": formatted_test_name,
                        "classname": f"{filename}.{formatted_test_name}",
                        "file": file_path.strip(),
                        "line": line_number.strip(),
                        "result": result.strip(),
                        "suite": filename
                    }
                    if result.strip() == "FAIL":
                        self.failures += 1
                    elif result.strip() == "SKIP":
                        self.skipped += 1
                    self.test_cases.append(test_case)

    def generate_junit_xml(self):
        """Generates the JUnit XML report from the parsed test cases."""
        testsuites = ET.Element("testsuites")
        timestamp = datetime.now(datetime.timezone.utc).isoformat()

        # Create a default testsuite using extracted filename
        ET.SubElement(testsuites, "testsuite", name=self.default_suite_name, errors="0", tests=str(self.total_tests),
                      failures=str(self.failures), skipped=str(self.skipped), timestamp=timestamp)

        for case in self.test_cases:
            testsuite = ET.SubElement(
                testsuites, "testsuite",
                name=case["classname"],
                timestamp=timestamp,
                time="0.0",
                errors="0",
                tests="1",
                failures="1" if case["result"] != "PASS" else "0",
                skipped="0"
            )

            ET.SubElement(
                testsuite, "testcase",
                name=case["name"],
                classname=case["classname"],
                time="0.0"
            )

        tree = ET.ElementTree(testsuites)
        ET.indent(tree, space="    ", level=0)
        tree.write(self.output_file, encoding="utf-8", xml_declaration=True)
        print(f"JUnit XML report generated: {self.output_file}")

    def convert(self):
        """Runs the conversion from Unity log to JUnit XML."""
        self.parse_unity_output()
        self.generate_junit_xml()


def main():
    parser = argparse.ArgumentParser(description="Convert Unity test output to JUnit XML.")
    parser.add_argument("log_file", help="Path to the Unity test output log file.")
    parser.add_argument("output_file", help="Path to the output JUnit XML file.")
    parser.add_argument("--version", "-v", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("--tc-prefix", help="Prefix to add to each test case name.", default="")
    args = parser.parse_args()

    converter = Unity2Junit(args.log_file, args.output_file, tc_prefix=args.tc_prefix)
    converter.convert()


if __name__ == "__main__":
    main()
