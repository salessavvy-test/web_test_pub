def add_three_numbers(a, b, c):
    """
    Add three numbers together.

    Args:
        a: First number
        b: Second number
        c: Third number

    Returns:
        The sum of a, b, and c
    """
    return a + b + c


if __name__ == "__main__":
    result = add_three_numbers(5, 10, 15)
    print(f"5 + 10 + 15 = {result}")

    result = add_three_numbers(1.5, 2.5, 3.0)
    print(f"1.5 + 2.5 + 3.0 = {result}")
