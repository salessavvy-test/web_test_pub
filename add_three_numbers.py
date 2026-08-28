#!/usr/bin/env python3
"""
Program to add three numbers together.
Co-authored with Glean
"""

def add_three_numbers(num1, num2, num3):
    """
    Add three numbers together and return the sum.

    Args:
        num1: First number
        num2: Second number
        num3: Third number

    Returns:
        The sum of all three numbers
    """
    return num1 + num2 + num3


def main():
    """Main function to demonstrate adding three numbers."""
    print("Welcome to the Three Number Addition Program!")
    print("=" * 50)

    try:
        # Get input from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        # Calculate the sum
        result = add_three_numbers(num1, num2, num3)

        # Display the result
        print(f"\nResult: {num1} + {num2} + {num3} = {result}")

    except ValueError:
        print("\nError: Please enter valid numbers!")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")


if __name__ == "__main__":
    main()
