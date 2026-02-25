"""
tests_1b.py

Contains unit tests for the max_subarray_sum function defined in lab_1c.py
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_example_case(): # Test for the example case provided
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_single_element(): # Test for only one element in list
    assert max_subarray_sum([5]) == 5

def test_positive(): # Test for all positive integers in the list
    assert max_subarray_sum([1, 2, 3, 4]) == 10

def test_negative(): # Test for negative integers in the list
    assert max_subarray_sum([-1, -3, -4, -2]) == -1

def test_regular(): # For regular inputs
    assert max_subarray_sum([3, -2, 5, -1]) == 6
    assert max_subarray_sum([1, -2, 3]) == 3

def test_zero(): # Test for list with 0s
    assert max_subarray_sum([0]) == 0 # Test for only 0
    assert max_subarray_sum([0, -3, 5, -2, 0, 3]) == 6 # Test for list with 2 0s

def test_empty_list():
    with pytest.raises(ValueError, match="List is empty"):
        max_subarray_sum([])