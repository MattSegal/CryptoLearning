"""
Tests for gcd.py
"""

import unittest
import gcd

class Tests(unittest.TestCase):

    def test_gcd_with_big_gcd(self):
        result = gcd.gcd(42823, 6409)
        self.assertEqual(result, 17)

    def test_gcd_with_small_gcd(self):
        result = gcd.gcd(6, 3)
        self.assertEqual(result, 3)

    def test_gcd_with_no_gcd(self):
        result = gcd.gcd(5, 3)
        self.assertEqual(result, 1)

    def test_gcd_with_one(self):
        result = gcd.gcd(5, 1)
        self.assertEqual(result, 1)

    def test_divide(self):
        factor, remainder = gcd.divide(42823, 6409)
        self.assertEqual(factor, 6)
        self.assertEqual(remainder, 4369)

        factor, remainder = gcd.divide(6409, 4369)
        self.assertEqual(factor, 1)
        self.assertEqual(remainder, 2040)

        factor, remainder = gcd.divide(4369, 2040)
        self.assertEqual(factor, 2)
        self.assertEqual(remainder, 289)
