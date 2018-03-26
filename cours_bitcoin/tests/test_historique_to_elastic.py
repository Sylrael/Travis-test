import unittest
from mock import patch
from cours_bitcoin.src.historique_to_elastic import get_historique_data

class HistoriqueTests(unittest.TestCase):

	def test_get_historique_data(self):
		mock_get_patcher = patch('cours_bitcoin.src.historique_to_elastic.requests.get')
		expected_data = [{'bpi': {'2011-01-01': 0.2243, '2011-01-02': 0.2243}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index. BPI value data returned as EUR.', 'time': {'updated': 'Jan 3, 2011 00:03:00 UTC', 'updatedISO': '2011-01-03T00:03:00+00:00'}}]
		
		mock_get = mock_get_patcher.start()
		
		mock_get.return_value.status_code = 200
		mock_get.return_value.json.return_value = expected_data
		
		response = get_historique_data('localhost', 9200, 'EUR', '2011-01-01', '2011-01-02')
		
		mock_get_patcher.stop()
		expected_status_code = 200
		
		self.assertEqual(response.status_code, expected_status_code)
		self.assertEqual(response.json(), expected_data)
		
	
if __name__ == "__main__":
	unittest.main()