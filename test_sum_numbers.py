#!/usr/bin/env python3
"""
Unit tests for sum_numbers.py
"""

import unittest
from sum_numbers import add_ten_numbers


class TestSumNumbers(unittest.TestCase):
    """Test cases for the add_ten_numbers function."""

    def test_add_positive_numbers(self):
        """Test adding 10 positive numbers."""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = add_ten_numbers(numbers)
        self.assertEqual(result, 55)

    def test_add_negative_numbers(self):
        """Test adding 10 negative numbers."""
        numbers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        result = add_ten_numbers(numbers)
        self.assertEqual(result, -55)

    def test_add_mixed_numbers(self):
        """Test adding 10 mixed positive and negative numbers."""
        numbers = [10, -5, 3, -2, 8, -1, 4, -3, 6, -4]
        result = add_ten_numbers(numbers)
        self.assertEqual(result, 16)

    def test_add_zeros(self):
        """Test adding 10 zeros."""
        numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = add_ten_numbers(numbers)
        self.assertEqual(result, 0)

    def test_add_floats(self):
        """Test adding 10 floating point numbers."""
        numbers = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
        result = add_ten_numbers(numbers)
        self.assertAlmostEqual(result, 60.0)

    def test_invalid_count_too_few(self):
        """Test that providing fewer than 10 numbers raises ValueError."""
        numbers = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            add_ten_numbers(numbers)

    def test_invalid_count_too_many(self):
        """Test that providing more than 10 numbers raises ValueError."""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        with self.assertRaises(ValueError):
            add_ten_numbers(numbers)


if __name__ == "__main__":
    unittest.main()
