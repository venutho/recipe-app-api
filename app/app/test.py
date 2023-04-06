"""
Sample Tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(10, 20)

        self.assertEqual(res, 30)


    def test_subtract_numbers(self):
        """Test subtracting one numbers from another"""
        res = calc.subtract(20, 10)

        self.assertEqual(res, 10)
