class NumericRangeExpander:
    """
    Expands numeric string ranges into a list of integers.
    For example, '1-3,5' becomes [1, 2, 3, 5].
    """

    def __init__(self):
        """
        Initializes the NumericRangeExpander with default range delimiters.
        """
        self.range_delimiters = ['-']  # default delimiter

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
        for range in ranges:
            if '-' in range:
                start, end = map(int, range.split('-'))
                numbers.extend(range(start, end + 1))
            elif range:
                numbers.append(int(range))
        return numbers
