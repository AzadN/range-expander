# NumericRangeExpander

A simple Python utility to expand numeric string ranges into a list of integers.

## Overview

The `NumericRangeExpander` class takes a string containing numbers and numeric ranges (e.g., `"1-3,5,7-9"`) and expands it into a list of integers (e.g., `[1, 2, 3, 5, 7, 8, 9]`).

## Features
- Supports comma-separated numbers and ranges (e.g., `"1-3,5"`)
- Easy to use and extend

## Usage

```
from numeric_range_expander import NumericRangeExpander

expander = NumericRangeExpander()
result = expander.expand("1-3,5,7-9")
print(result)  # Output: [1, 2, 3, 5, 7, 8, 9]
```

## Installation
No installation required. Just include `numeric_range_expander.py` in your project.

## Testing

Unit tests are provided in `test_numeric_range_expander.py`. To run the tests:

```
python -m pytest test_numeric_range_expander.py
```

## License
MIT License
