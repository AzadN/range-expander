# NumericRangeExpander

A simple Python utility to expand numeric string ranges into a list of integers.

## Overview

The `NumericRangeExpander` class takes a string containing numbers and numeric ranges (e.g., `"1-3,5,7-9"`) and expands it into a list of integers (e.g., `[1, 2, 3, 5, 7, 8, 9]`).

## Features
- Supports comma-separated numbers and ranges (e.g., `"1-3,5"`)
- Supports custom range delimiters (e.g., `..`, `to`, `~`)
- Supports jump values for ranges (e.g., `1-5:2` → `[1, 3, 5]`)
- Removes duplicate values from the output (e.g., `1-3,2,3` → `[1, 2, 3]`)
- Supports multiple output formats: list, csv, set
- Easy to use and extend


## Usage

### Basic usage
```python
from numeric_range_expander import NumericRangeExpander

expander = NumericRangeExpander()
result = expander.expand("1-3,5,7-9")
print(result)  
# Output: [1, 2, 3, 5, 7, 8, 9]
```


### Using custom delimiters
You can specify your own range delimiters (e.g., `..`, `to`, `~`):
```python
from numeric_range_expander import NumericRangeExpander

expander = NumericRangeExpander(delimiters=["..", "~", "to"])
result = expander.expand("1..3,4~5,6 to 7,8")
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
```

### Using jump values in ranges
You can specify a jump value after a colon to control the step size in a range:
```python
from numeric_range_expander import NumericRangeExpander

expander = NumericRangeExpander()
result = expander.expand("1-5:2,10-2:4")
print(result)  
# Output: [1, 3, 5, 10, 6, 2]
```

### Output formats
You can specify the output format using the `output_format` argument:
```python
expander = NumericRangeExpander()
result_list = expander.expand("1-3,5")
print(result_list)  
# Output: [1, 2, 3, 5]
result_csv = expander.expand("1-3,5", output_format="csv")
print(result_csv)  
# Output: "1,2,3,5"
result_set = expander.expand("1-3,5", output_format="set")
print(result_set)  
# Output: {1, 2, 3, 5}
```

### CLI Usage

You can also use NumericRangeExpander directly from the command line:

```sh
python numeric_range_expander.py "1-5,7,10-2:2" --format csv --delims - .. to
# Output: 1,2,3,4,5,7,10,8,6,4,2
```

Arguments:
- The first argument is the range string to expand (e.g., '1-5,7,10-2:2').
- `--format` specifies the output format ('list', 'csv', 'set'). Default is 'list'.
- `--delims` allows you to specify custom delimiters (e.g., `--delims - .. to`).

## Docstring Summary (Quick Command)

To quickly view all docstrings for the main file or test file, use the built-in `pydoc` command:

```sh
python -m pydoc numeric_range_expander
python -m pydoc test_numeric_range_expander
```

This will display the module, class, and function docstrings in your terminal for easy review.


> **Note:**  
> - Supported formats: "list" (default), "csv", "set".
> - An unsupported format will raise a `ValueError`.
> - The jump value must be a nonzero integer. If omitted, the default is 1.
> - Reversed ranges (e.g., `10-2:4`) are supported.
> - Duplicate values from overlapping ranges or repeated numbers are removed.
> - Invalid jump values (e.g., `1-5:a` or `1-5:0`) will raise a `ValueError`.


## Installation

### Python
Make sure you have Python 3.7 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

### Required Libraries
This project does not require any third-party libraries for basic usage. However, to run the tests, you need `pytest`:

```sh
pip install pytest
```

Just include `numeric_range_expander.py` in your project to use the expander.

## Testing

Unit tests are provided in `test_numeric_range_expander.py`. To run the tests:

```
python -m pytest test_numeric_range_expander.py
```
