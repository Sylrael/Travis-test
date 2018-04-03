import requests

# Retrieve data from CoinDesk API
def get_historique_data(currency, start_date, end_date):	
	url_cours_bitcoin = 'https://api.coindesk.com/v1/bpi/historical/close.json?currency='+currency+'&start='+start_date+'&end='+end_date
	res = requests.get(url_cours_bitcoin)
	if res.ok:
		return res
	else:
		return None
		
def main():
	data_historique = get_historique_data('EUR', '2018-03-31', '2010-07-17')
	

if __name__ == '__main__':
	main()