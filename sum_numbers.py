#!/usr/bin/env python3
"""
Simple script to add 10 numbers together.
Co-authored with Glean
"""

def add_ten_numbers(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    """
    Adds 10 numbers together and returns the sum.

    Args:
        num1 through num10: The ten numbers to add

    Returns:
        The sum of all 10 numbers
    """
    return num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10


def add_number_list(numbers):
    """
    Adds numbers from a list together.

    Args:
        numbers: List of numbers to add (should contain 10 numbers)

    Returns:
        The sum of all numbers in the list
    """
    if len(numbers) != 10:
        raise ValueError("Please provide exactly 10 numbers")
    return sum(numbers)


if __name__ == "__main__":
    # Example 1: Using individual parameters
    result1 = add_ten_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f"Sum of 1-10: {result1}")

    # Example 2: Using a list
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result2 = add_number_list(numbers)
    print(f"Sum of {numbers}: {result2}")

    # Example 3: Using decimals
    decimals = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
    result3 = add_number_list(decimals)
    print(f"Sum of {decimals}: {result3}")
