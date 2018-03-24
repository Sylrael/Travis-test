import requests
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import date
import datetime
import json
import sys

# Fonction adding data in elastic search database
def add_elastic():
	for i in data["bpi"]:
		date_event = datetime.datetime.strptime(i, "%Y-%m-%d").date()
		value_event = data["bpi"][i]
		yield {
			'_index' : 'cours_btc_idx',
			'_type': 'cours_btc',
			'_source': {
				'date': date_event,
				'rate': value_event,
				'devise': currency,
				'data_type': 'historique'
			}
		}

		
def main():
	# Default values
	host_es = 'localhost'
	port_es = 9200
	currency = 'EUR'
	start_date = '2011-01-01'
	end_date = '2018-03-23'

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

	# Retrieve data from CoinDesk API
	url_cours_bitcoin = 'https://api.coindesk.com/v1/bpi/historical/close.json?currency='+currency+'&start='+start_date+'&end='+end_date
	res = requests.get(url_cours_bitcoin)
	data = res.json()
	# Connect to elastic search
	es = Elasticsearch([{'host': host_es, 'port': port_es}])
	# Add data in elastic search in bulk
	helpers.bulk(es, add_elastic())

if __name__ == '__main__':
	main()
