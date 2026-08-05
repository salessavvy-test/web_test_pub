#!/usr/bin/env python3
"""
Unit tests for the add_numbers module.
"""

import unittest
from add_numbers import add_three_numbers


class TestAddThreeNumbers(unittest.TestCase):
    """Test cases for add_three_numbers function."""

    def test_positive_numbers(self):
        """Test adding positive numbers."""
        self.assertEqual(add_three_numbers(1, 2, 3), 6)
        self.assertEqual(add_three_numbers(10, 20, 30), 60)

    def test_negative_numbers(self):
        """Test adding negative numbers."""
        self.assertEqual(add_three_numbers(-1, -2, -3), -6)
        self.assertEqual(add_three_numbers(-10, -20, -30), -60)

    def test_mixed_numbers(self):
        """Test adding mixed positive and negative numbers."""
        self.assertEqual(add_three_numbers(10, -5, 3), 8)
        self.assertEqual(add_three_numbers(-10, 20, -5), 5)

    def test_zero(self):
        """Test adding with zero."""
        self.assertEqual(add_three_numbers(0, 0, 0), 0)
        self.assertEqual(add_three_numbers(5, 0, -5), 0)

    def test_floats(self):
        """Test adding floating point numbers."""
        self.assertAlmostEqual(add_three_numbers(1.5, 2.5, 3.0), 7.0)
        self.assertAlmostEqual(add_three_numbers(0.1, 0.2, 0.3), 0.6, places=5)


if __name__ == "__main__":
    unittest.main()
