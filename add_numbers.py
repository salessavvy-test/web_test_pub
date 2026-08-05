#!/usr/bin/env python3
"""
Simple module to add three numbers together.
"""


def add_three_numbers(num1, num2, num3):
    """
    Add three numbers together and return the sum.

    Args:
        num1: First number
        num2: Second number
        num3: Third number

    Returns:
        The sum of the three numbers
    """
    return num1 + num2 + num3


def main():
    """Example usage of add_three_numbers function."""
    result = add_three_numbers(10, 20, 30)
    print(f"Adding 10 + 20 + 30 = {result}")

    result = add_three_numbers(5.5, 2.3, 1.2)
    print(f"Adding 5.5 + 2.3 + 1.2 = {result}")

    result = add_three_numbers(-5, 10, 3)
    print(f"Adding -5 + 10 + 3 = {result}")


if __name__ == "__main__":
    main()
