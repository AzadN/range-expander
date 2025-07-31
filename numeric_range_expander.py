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
            parsed = self.process_range(token)
            if parsed:
                start, end = parsed
                if not isinstance(start, int) or not isinstance(end, int):
                    raise ValueError(f"Invalid range: {token}")
                jump = 1 if start <= end else -1  # Determine the step direction
                numbers.extend(range(start, end + jump, jump))
            else:
                if not token.isdigit():
                    raise ValueError(f"Invalid number or unsupported range: '{token}'")
                numbers.append(int(token))
        return numbers
