import unittest
from util_ml import convert, get_next_day, filter_text, get_aggregated_text, format_data

class TestUtilMachineLearningCoursBitcoin(unittest.TestCase):
	def test_get_next_day(self):
		date_today = '2018-01-01'
		expected_date = '2018-01-02'
		self.assertEqual(get_next_day(date_today, expected_date))
		date_today = '2017-12-31'
		expected_date = '2018-01-01'
		self.assertEqual(get_next_day(date_today, expected_date))
		date_today = '2018-02-28'
		expected_date = '2018-03-01'
		self.assertEqual(get_next_day(date_today, expected_date))

if __name__ == '__main__':
	unittest.main()