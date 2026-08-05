#!/usr/bin/env python3
"""
Simple utility to add three numbers together.
"""


def add_three_numbers(a, b, c):
    """
    Add three numbers together.

    Args:
        a: First number
        b: Second number
        c: Third number

    Returns:
        The sum of the three numbers
    """
    return a + b + c


def main():
    """Main function to demonstrate adding three numbers."""
    # Example usage
    num1 = 10
    num2 = 20
    num3 = 30

    result = add_three_numbers(num1, num2, num3)
    print(f"Adding {num1} + {num2} + {num3} = {result}")


if __name__ == "__main__":
    main()
