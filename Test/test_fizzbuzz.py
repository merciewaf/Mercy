import unittest
import fizzbuz


class FizzBuzzTest(unittest.TestCase):
	"""Testing FizzBuzzTest
	"""

	def test_returns_fizz_when_divisible_by_three(self):
	    self.assertEqual(fizz_buzz(3), 'fizz')	

	def test_returns_fizz_when_divisible_by_five(self):
	    self.assertEqual(fizz_buzz(5), 'buzz')	