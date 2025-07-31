# NumericRangeExpander

A simple Python utility to expand numeric string ranges into a list of integers.

## Overview

The `NumericRangeExpander` class takes a string containing numbers and numeric ranges (e.g., `"1-3,5,7-9"`) and expands it into a list of integers (e.g., `[1, 2, 3, 5, 7, 8, 9]`).

## Features
- Supports comma-separated numbers and ranges (e.g., `"1-3,5"`)
- Supports custom range delimiters (e.g., `..`, `to`, `~`)
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
print(result)  
# Output: [1, 2, 3, 4, 5, 6, 7, 8]
```


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
