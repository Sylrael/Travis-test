import unittest
from mock import patch
from montants_transactions.src.transactions_to_elastic import get_single_block
from montants_transactions.src.transactions_to_elastic import get_blocks_for_day
from montants_transactions.src.transactions_to_elastic import convert_date_in_ms
from datetime import date, timedelta
import datetime
import time

class TransactionsTests(unittest.TestCase):

	def test_convert_date_in_ms(self):
		date_to_test = "2011-01-01"
		formatted_test_date = datetime.datetime.strptime(date_to_test, "%Y-%m-%d")
		expected_date_in_ms = 1293836400000
		self.assertEqual(convert_date_in_ms(formatted_test_date), expected_date_in_ms)
		
	def test_get_blocks_for_day(self):
		mock_get_patcher = patch('montants_transactions.src.transactions_to_elastic.requests.get')
		expected_data = []
		
		mock_get = mock_get_patcher.start()
		
		mock_get.return_value.status_code = 200
		mock_get.return_value.json.return_value = expected_data
		
		response = get_blocks_for_day(1293836400000)
		mock_get_patcher.stop()
		expected_status_code = 200
		
		self.assertEqual(response.status_code, expected_status_code)
		self.assertEqual(response.json(), expected_data)
		
	def test_get_single_block(self):
		mock_get_patcher = patch('montants_transactions.src.transactions_to_elastic.requests.get')
		expected_data = []
		
		mock_get = mock_get_patcher.start()
		
		mock_get.return_value.status_code = 200
		mock_get.return_value.json.return_value = expected_data
		
		response = get_single_block('000000000000996cab6a4b0a0a48d278ca361b03a25bcdc71496ee6bacbd757e')
		mock_get_patcher.stop()
		expected_status_code = 200
		
		self.assertEqual(response.status_code, expected_status_code)
		self.assertEqual(response.json(), expected_data)
		
	
if __name__ == "__main__":
	unittest.main()