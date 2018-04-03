import requests
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import date
import datetime
import json
import sys

# Default values
host_es = 'localhost'
port_es = 9200
currency = 'EUR'
start_date = '2010-07-17'
end_date = str(datetime.date.today())

# Input values
# host and port of elastic search database
if (len(sys.argv) >= 3):
	host_es = sys.argv[1]
	port_es = sys.argv[2]
# currency needed
if (len(sys.argv) >= 4):
	currency = sys.argv[3]
# start and ending date for search
if (len(sys.argv) >= 6):
	start_date = sys.argv[4]
	end_date = sys.argv[5]

# Fonction adding data in elastic search database
def add_elastic(data):
	for i in data["bpi"]:
		date_event = datetime.datetime.strptime(i, "%Y-%m-%d").date()
		value_event = data["bpi"][i]
		yield {
			'_index' : 'cours_btc_idx_test',
			'_type': 'cours_btc_test',
			'_id': date_event,
			'_source': {
				'date': date_event,
				'rate': value_event,
				'devise': currency,
				'data_type': 'historique'
			}
		}

# Retrieve data from CoinDesk API
def get_historique_data(host_es, port_es, currency, start_date, end_date):	
	url_cours_bitcoin = 'https://api.coindesk.com/v1/bpi/historical/close.json?currency='+currency+'&start='+start_date+'&end='+end_date
	res = requests.get(url_cours_bitcoin)
	if res.ok:
		return res
	else:
		return None
		
def main():
	# Retrieve data from CoinDesk API	
	res = get_historique_data(host_es, port_es, currency, start_date, end_date)
	data = res.json()
	# Connect to elastic search
	es = Elasticsearch([{'host': host_es, 'port': port_es}])
	# Add data in elastic search in bulk
	helpers.bulk(es, add_elastic(data))

if __name__ == '__main__':
	main()
