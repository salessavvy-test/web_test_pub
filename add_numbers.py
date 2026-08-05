def add_three_numbers(a, b, c):
    """
    Add three numbers together and return the sum.

    Args:
        a: First number
        b: Second number
        c: Third number

    Returns:
        The sum of a, b, and c
    """
    return a + b + c


if __name__ == "__main__":
    # Example usage
    result = add_three_numbers(5, 10, 15)
    print(f"5 + 10 + 15 = {result}")

    # Interactive mode
    print("\nEnter three numbers to add:")
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        num3 = float(input("Third number: "))
        total = add_three_numbers(num1, num2, num3)
        print(f"\nResult: {num1} + {num2} + {num3} = {total}")
    except ValueError:
        print("Please enter valid numbers!")
