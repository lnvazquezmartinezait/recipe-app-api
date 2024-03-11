"""
sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """test the calc module"""
    def test_add_nubers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtract number"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)

