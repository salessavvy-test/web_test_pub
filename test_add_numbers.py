#!/usr/bin/env python3
"""
Unit tests for add_numbers module.
"""

import unittest
from add_numbers import add_three_numbers


class TestAddThreeNumbers(unittest.TestCase):
    """Test cases for add_three_numbers function."""

    def test_positive_integers(self):
        """Test adding three positive integers."""
        self.assertEqual(add_three_numbers(1, 2, 3), 6)
        self.assertEqual(add_three_numbers(10, 20, 30), 60)

    def test_negative_integers(self):
        """Test adding numbers including negatives."""
        self.assertEqual(add_three_numbers(-1, -2, -3), -6)
        self.assertEqual(add_three_numbers(-5, 10, 3), 8)

    def test_floats(self):
        """Test adding floating point numbers."""
        self.assertAlmostEqual(add_three_numbers(1.5, 2.5, 3.0), 7.0)
        self.assertAlmostEqual(add_three_numbers(0.1, 0.2, 0.3), 0.6, places=1)

    def test_zeros(self):
        """Test adding with zeros."""
        self.assertEqual(add_three_numbers(0, 0, 0), 0)
        self.assertEqual(add_three_numbers(5, 0, 3), 8)

    def test_mixed_types(self):
        """Test adding mixed integer and float types."""
        self.assertEqual(add_three_numbers(1, 2.5, 3), 6.5)
        self.assertEqual(add_three_numbers(10.0, 20, 30.0), 60.0)


if __name__ == "__main__":
    unittest.main()
