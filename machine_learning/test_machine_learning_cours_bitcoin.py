import unittest
# from machine_learning_cours_bitcoin import convert, get_next_day, filter_text, get_aggregated_text, format_data, retrieve_data_day
from machine_learning_cours_bitcoin import get_next_day

class TestMachineLearningCoursBitcoin(unittest.TestCase):
	'''def test_convert(self):
		self.assertEqual(True, True)'''

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
		
	'''def test_filter_text(self):
		input = ""
		expected_output = ""
		self.assertEqual(filter_text(input), expected_output)
	
	def test_get_aggregated_text(self):
		input = ""
		expected_output = ""
		self.assertEqual(get_aggregated_text(input), expected_output)
	
	def test_format_data(self):
		input = ""
		expected_output = ""
		self.assertEqual(format_data(input), expected_output)'''
		
	'''def test_retrieve_bitcoin_cours(self):
		mock_get_patcher = patch('montants_transactions.src.transactions_to_elastic.requests.get')
		expected_data = []
		
		mock_get = mock_get_patcher.start()
		
		mock_get.return_value.status_code = 200
		mock_get.return_value.json.return_value = expected_data
		
		response = get_blocks_for_day(1293836400000)
		mock_get_patcher.stop()
		expected_status_code = 200
		
		self.assertEqual(response.status_code, expected_status_code)
		self.assertEqual(response.json(), expected_data)'''
		
	'''def test_retrieve_data_day(self):
		mock_get_patcher = patch('montants_transactions.src.transactions_to_elastic.requests.get')
		expected_data = []
		
		mock_get = mock_get_patcher.start()
		
		mock_get.return_value.status_code = 200
		mock_get.return_value.json.return_value = expected_data
		
		response = get_blocks_for_day(1293836400000)
		mock_get_patcher.stop()
		expected_status_code = 200
		
		self.assertEqual(response.status_code, expected_status_code)
		self.assertEqual(response.json(), expected_data)'''
		
		
		
if __name__ == '__main__':
	unittest.main()