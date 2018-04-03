import requests
import datetime
from datetime import date

# Retrieve data from CoinDesk API
def get_historique_data(currency, start_date, end_date):	
	url_cours_bitcoin = 'https://api.coindesk.com/v1/bpi/historical/close.json?currency='+currency+'&start='+start_date+'&end='+end_date
	res = requests.get(url_cours_bitcoin)
	if res.ok:
		return res
	else:
		return None
		
def main():
	data_historique = get_historique_data('EUR', '2018-01-01', '2018-02-01')
	print data_historique
	data = data_historique.json()
	for i in data["bpi"]:
		date_event = datetime.datetime.strptime(i, "%Y-%m-%d").date()
		value_event = data["bpi"][i]
		xy = (date_event, value_event)
		print xy
		

if __name__ == '__main__':
	main()