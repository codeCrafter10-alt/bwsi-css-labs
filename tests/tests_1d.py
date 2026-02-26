"""
tests_1d.py

Contains unit tests for two_sum function in lab_1d.py
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_example_case(): # Tests example case provided
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_middle(): # Test for answer in the middle of the list
    assert two_sum([3, 2, 4, 8], 6) == [1, 2]

def test_negative(): # Test for list with negative integers
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_zero(): # Test for solution with 0
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]

def test_two_elements(): # Test for only two integers in the list
    assert two_sum([4, 6], 10) == [0, 1]

def test_duplicate():# Test for duplicate integers being the answer
    assert two_sum([1, 3, 3, 4, 8, 10], 6) == [1, 2]

if __name__ == "__main__":
    pytest.main()