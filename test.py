from BowlingScoreGenerator import *
import unittest

class TestBowlingScoreMethods(unittest.TestCase):

	def test_non_numeric_roll(self):
		self.assertRaises(AssertionError, generate_score, 'John', ['5', '5', 'ac', '4', '6'])

	def test_negative_roll(self):
		self.assertRaises(AssertionError, generate_score, 'John', ['10', '5', '2', '-4', '-6'])

	def test_double_digit_roll(self):
		self.assertRaises(AssertionError, generate_score, 'John', ['10', '20', '200', '-45', '-6'])

	def test_impossible_frame(self):
		self.assertRaises(AssertionError, generate_score, 'John', ['6', '2', '7', '4', '10', '9', '0', '8', '2', '10', '10', '3', '5', '7', '2', '5', '5', '8'])

	def test_not_enough_rolls(self):
		self.assertRaises(AssertionError, generate_score, 'John', ['6', '2', '7', '1', '10', '9', '0', '8', '2', '10', '10', '3', '5', '7', '2'])

	def test_too_many_rolls(self):
		self.assertRaises(AssertionError, generate_score, 'John', ['6', '2', '7', '1', '10', '9', '0', '8', '2', '10', '10', '3', '5', '7', '2', '5', '2', '2', '2', '5', '2', '2'])

	def test_strike_frame_ten_num_pins(self):
		self.assertRaises(AssertionError, generate_score, 'John', ['6', '2', '7', '1', '10', '9', '0', '8', '2', '10', '10', '3', '5', '7', '2', '10', '2'])

	def test_spare_frame_ten_num_pins(self):
		self.assertRaises(AssertionError, generate_score, 'John', ['6', '2', '7', '1', '10', '9', '0', '8', '2', '10', '10', '3', '5', '7', '2', '5', '5'])

	def test_strike_frame_ten_impossible_bonus(self):
		self.assertRaises(AssertionError, generate_score, 'John', ['6', '2', '7', '1', '10', '9', '0', '8', '2', '10', '10', '3', '5', '7', '2', '10', '8', '8'])

	def test_perfect_score(self):
		self.assertEqual(generate_score('John', ['10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10'])[0], 300)

	def test_normal_game(self):
		self.assertEqual(generate_score('John', ['6', '2', '7', '1', '10', '9', '0', '8', '2', '10', '10', '3', '5', '7', '2', '5', '5', '8'])[0], 140)

	def test_zero_score(self):
		self.assertEqual(generate_score('John', ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])[0], 0)

if __name__ == '__main__':
	unittest.main()