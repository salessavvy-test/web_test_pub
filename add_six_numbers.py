#!/usr/bin/env python3
"""
Program to add 6 numbers together
Co-authored with Glean
"""

def add_six_numbers(num1, num2, num3, num4, num5, num6):
    """
    Add six numbers together and return the sum.

    Args:
        num1, num2, num3, num4, num5, num6: Numbers to add

    Returns:
        The sum of all six numbers
    """
    return num1 + num2 + num3 + num4 + num5 + num6


def main():
    """Main function to demonstrate adding 6 numbers."""
    print("Add Six Numbers Program")
    print("-" * 30)

    # Example 1: Using predefined numbers
    numbers = [10, 20, 30, 40, 50, 60]
    result = add_six_numbers(*numbers)
    print(f"Example: {' + '.join(map(str, numbers))} = {result}")

    # Example 2: Interactive input
    print("\nEnter 6 numbers to add:")
    user_numbers = []
    for i in range(1, 7):
        while True:
            try:
                num = float(input(f"Number {i}: "))
                user_numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid number.")

    user_result = add_six_numbers(*user_numbers)
    print(f"\nResult: {' + '.join(map(str, user_numbers))} = {user_result}")


if __name__ == "__main__":
    main()
