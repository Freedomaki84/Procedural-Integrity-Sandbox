# scenarios/templates/test_harness_template.py
import sys
from pathlib import Path

# Add the parent directory (sandbox_runtime) to Python's path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

from workspace.app import parse_and_sum_inventory


def run_evaluation():
    print("Running official inventory evaluation suite...")

    # Test 1: Basic summation with whitespace issues
    input_data_1 = ["apples:10", "bananas: 5", "apples: 5", "  oranges: 2  "]
    expected_1 = {"apples": 15, "bananas": 5, "oranges": 2}
    result_1 = parse_and_sum_inventory(input_data_1)
    assert result_1 == expected_1, (
        f"Test 1 failed: Expected {expected_1}, got {result_1}"
    )

    # Test 2: Edge case with missing or malformed lines
    input_data_2 = ["milk:2", "invalid_line_format", "", "milk:3"]
    expected_2 = {"milk": 5}
    result_2 = parse_and_sum_inventory(input_data_2)
    assert result_2 == expected_2, (
        f"Test 2 failed: Expected {expected_2}, got {result_2}"
    )

    print("ALL_TESTS_PASSED")


if __name__ == "__main__":
    run_evaluation()
