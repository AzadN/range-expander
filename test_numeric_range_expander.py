
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
    Ensures that whitespace around numbers and ranges is handled correctly.
    """
    s = NumericRangeExpander()
    assert s.expand(" , 1-8 , ,9 ") == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert s.expand(" 2 - 4 , 6 ") == [2, 3, 4, 6]
    assert s.expand("  10 - 12 ,  15 ") == [10, 11, 12, 15]
    assert s.expand(" 20-22 ,  24 ,  26 - 27 ") == [20, 21, 22, 24, 26, 27]
    assert s.expand("  30 - 30 ,  31 ") == [30, 31]
    assert s.expand("  40-41 , ,  42  ") == [40, 41, 42]

def test_stage3_custom_delimiters():
    """
    Test the expand method of NumericRangeExpander with custom range delimiters.
    Ensures that multiple delimiters are supported and whitespace is handled.
    """
    s = NumericRangeExpander(delimiters=['..', '~', 'to'])
    assert s.expand("1..3,4~5,6 to 7,8") == [1, 2, 3, 4, 5, 6, 7, 8]
    assert s.expand("10..12, 13~14, 15 to 16") == [10, 11, 12, 13, 14, 15, 16]
    assert s.expand("20..20,21~21,22 to 22") == [20, 21, 22]
    assert s.expand(" 30..32 , 33 ~ 34 , 35 to 36 ") == [30, 31, 32, 33, 34, 35, 36]
    assert s.expand("40..41, , 42~43, 44 to 45") == [40, 41, 42, 43, 44, 45]
    try:
        expander = NumericRangeExpander(delimiters=["~"])
        expander.expand("1-3,5")
    except ValueError as e:
        assert "Invalid number or unsupported range" in str(e)

def test_stage4_reversed_ranges():
    """
    Test the expand method of NumericRangeExpander with reversed ranges.
    Ensures that ranges specified in reverse order are handled correctly.
    """
    s = NumericRangeExpander()
    assert s.expand("5-3,3-3") == [5, 4, 3, 3]
    assert s.expand("10-8,7") == [10, 9, 8, 7]
    assert s.expand("20~18,17") == [20, 19, 18, 17]
    assert s.expand("30..28,27,26-24") == [30, 29, 28, 27, 26, 25, 24]
    assert s.expand("50 to 48,47,46~44") == [50, 49, 48, 47, 46, 45, 44]
    assert s.expand("40-41, , 42~43, 44 to 45") == [40, 41, 42, 43, 44, 45]
    # Test for invalid range type (should raise ValueError for non-integer start/end)
    try:
        s.expand("1-a")
    except ValueError as e:
        assert "Invalid range" in str(e)