class NumericRangeExpander:
    """
    Expands numeric string ranges into a list of integers.
    For example, '1-3,5' becomes [1, 2, 3, 5].
    """

    def __init__(self, delimiters=None):
        """
        Initializes the NumericRangeExpander with default or custom range delimiters.
        """
        self.range_delimiters = delimiters or ['-', '..', 'to', '~']

    def process_range(self, token):
        """
        Parses a token to extract a numeric range using the configured delimiters.

        Args:
            token (str): A string potentially containing a numeric range (e.g., '1-3', '4..6').

        Returns:
            tuple or None: A tuple (start, end) if a valid range is found, otherwise None.
        """
        for delimiter in self.range_delimiters:
            if delimiter in token:
                parts = token.split(delimiter)
                if len(parts) == 2:  # Expect exactly two parts for a valid range
                    try:
                        return int(parts[0].strip()), int(parts[1].strip())
                    except ValueError:  # Handle non-integer values
                        raise ValueError(f"Invalid range: '{token}'")
        return None  # No delimiter match
    
    def expand(self, input):
        """
        Expands a string containing numbers and ranges into a list of integers.

        Args:
            input (str): A string containing numbers and ranges separated by commas (e.g., '1-3,5').

        Returns:
            numbers (list): A list of integers expanded from the input string.
        """
        numbers = []
        ranges = input.split(',')
        for token in ranges:
            token = token.strip()
            if not token:
                continue # Skip empty tokens

            jump = 1
            # Check for jump value
            if ':' in token:
                token, jump_part = token.split(':', 1)
                try:
                    jump = int(jump_part.strip())
                except ValueError:
                    raise ValueError(f"Invalid jump value: {jump_part.strip()}")
                if jump == 0:
                    raise ValueError("Jump value must not be zero")
            parsed = self.process_range(token)
            if parsed:
                start, end = parsed
                jump = abs(jump)
                if start > end:
                    numbers.extend(range(start, end - 1, -jump))
                else:
                    numbers.extend(range(start, end + 1, jump))
            else:
                if not token.isdigit():
                    raise ValueError(f"Invalid number or unsupported range: '{token}'")
                numbers.append(int(token))
        return numbers
