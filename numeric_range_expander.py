class NumericRangeExpander:
    """
    Expands numeric string ranges into a list of unique integers.
    For example, '1-3,5' becomes [1, 2, 3, 5].
    Duplicate values are removed from the output.
    Supports custom delimiters and jump values.
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
                        # Try converting both parts to integers
                        return int(parts[0].strip()), int(parts[1].strip())
                    except ValueError:
                        # Raise a clear error if either part is not an integer
                        raise ValueError(f"Invalid range: '{token}'")
        # Return None if no delimiter matches
        return None
    
    def expand(self, input):
        """
        Expands a string containing numbers and ranges into a list of unique integers.
        Supports custom delimiters and jump values.
        Duplicate values are removed from the output.

        Args:
            input (str): A string containing numbers and ranges separated by commas (e.g., '1-3,5').

        Returns:
            numbers (list): A list of unique integers expanded from the input string.
        """
        numbers = []
        seen = set()
        ranges = input.split(',')
        for token in ranges:
            token = token.strip()
            if not token:
                continue  # Skip empty tokens

            jump = 1
            # Check for jump value syntax
            if ':' in token:
                parts = token.split(':')
                if len(parts) != 2:
                    # Invalid jump syntax (e.g., multiple colons)
                    raise ValueError(f"Invalid jump syntax in token: '{token}'")
                token, jump_part = parts
                try:
                    jump = int(jump_part.strip())
                    if jump <= 0:
                        raise ValueError("Jump must be a positive integer.")
                except ValueError:
                    # Invalid jump value (not an integer)
                    raise ValueError(f"Invalid jump value: '{jump_part}'")

            parsed = self.process_range(token)
            if parsed:
                start, end = parsed
                direction = 1 if start <= end else -1  # Determine direction
                jump = abs(jump)  # Always use positive jump for range
                # Generate range values, skipping duplicates
                for value in range(start, end + direction, direction * jump):
                    if value not in seen:
                        numbers.append(value)
                        seen.add(value)
            else:
                try:
                    # Try to parse as a standalone integer
                    value = int(token)
                    if value not in seen:
                        numbers.append(value)
                        seen.add(value)
                except ValueError:
                    raise ValueError(f"Invalid standalone value: '{token}'")
        return numbers
