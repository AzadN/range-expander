
"""
Unit tests for the NumericRangeExpander class in numeric_range_expander.py.
"""

from numeric_range_expander import NumericRangeExpander


def test_stage1_basic():
    """
    Test the expand method of NumericRangeExpander with basic input cases.
    """
    s = NumericRangeExpander()
    assert s.expand("1-3,5,7-9") == [1, 2, 3, 5, 7, 8, 9]
    assert s.expand("1-2,4") == [1, 2, 4]
    assert s.expand("5") == [5]
    assert s.expand("10-12") == [10, 11, 12]
    assert s.expand("") == []
    assert s.expand("15-15") == [15]

def test_stage2_whitespaces():
    """
    Test the expand method of NumericRangeExpander with input cases containing whitespaces.
    """
    s = NumericRangeExpander()
    assert s.expand(" , 1-8 , ,9 ") == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert s.expand(" 2 - 4 , 6 ") == [2, 3, 4, 6]
    assert s.expand("  10 - 12 ,  15 ") == [10, 11, 12, 15]
    assert s.expand(" 20-22 ,  24 ,  26 - 27 ") == [20, 21, 22, 24, 26, 27]
    assert s.expand("  30 - 30 ,  31 ") == [30, 31]
    assert s.expand("  40-41 , ,  42  ") == [40, 41, 42]