#!/usr/bin/env python3
"""
Program to add 10 numbers together.
"""

def add_ten_numbers(numbers):
    """
    Add 10 numbers together and return the sum.

    Args:
        numbers: List of 10 numbers to add

    Returns:
        The sum of all 10 numbers
    """
    if len(numbers) != 10:
        raise ValueError("Please provide exactly 10 numbers")

    return sum(numbers)


def main():
    """Main function to demonstrate adding 10 numbers."""
    # Example: Adding numbers 1 through 10
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = add_ten_numbers(numbers)

    print(f"Numbers: {numbers}")
    print(f"Sum of 10 numbers: {result}")

    # You can also input your own numbers
    print("\nEnter 10 numbers to add:")
    user_numbers = []
    for i in range(10):
        while True:
            try:
                num = float(input(f"Number {i+1}: "))
                user_numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid number")

    user_result = add_ten_numbers(user_numbers)
    print(f"\nSum of your 10 numbers: {user_result}")


if __name__ == "__main__":
    main()
