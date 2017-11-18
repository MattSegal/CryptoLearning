"""
Tests for euclid.py
"""

import unittest
from euclid import extended_euclid

class Tests(unittest.TestCase):

    def test_euclid_1(self):
        gcd, x, y = extended_euclid(274, 63)
        self.assertEqual(gcd, 1)
        self.assertEqual(x, -20)
        self.assertEqual(y, 87)

    def test_euclid_2(self):
        gcd, x, y = extended_euclid(421, 111)
        self.assertEqual(gcd, 1)
        self.assertEqual(x, -29)
        self.assertEqual(y, 110)