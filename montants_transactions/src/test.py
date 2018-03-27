import datetime
from datetime import date, timedelta
import time

def convert_date_in_ms(date):
	#timestamp = int(time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple()))
	timestamp = int(time.mktime(date.timetuple()))
	date_in_ms = (timestamp+3600)*1000
	return date_in_ms
	
date = '2017-01-01'
date_search = datetime.datetime.strptime(date, "%Y-%m-%d")
print date_search
print date_search.utcnow()
unixtime = convert_date_in_ms(date_search)
print unixtime
date_reversed = datetime.datetime.utcfromtimestamp(unixtime/1000)
print date_reversed