from pyspark.sql import SparkSession, Row
from pyspark.ml.feature import CountVectorizer, Word2Vec
import requests
from elasticsearch import Elasticsearch
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import datetime
from datetime import timedelta

STOPWORDS = set(stopwords.words('english'))
CHAR_TO_REMOVE = ',.:;?!"()'

#Initialize SparkSession
spark = SparkSession \
    .builder \
    .appName("Machine learning Bitcoin") \
    .config("master", "local[2]") \
    .getOrCreate()
sc = spark.sparkContext

def convert(input):
    if isinstance(input, dict):
        return dict((convert(key), convert(value)) for key, value in input.iteritems())
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
		
def retrieve_bitcoin_cours(date_str):
	es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
	res = es.get(index='cours_btc_idx_test', doc_type='cours_btc_test', id=date_str)
	return res

def retrieve_data_day(date_str):
	url_googlenews_api = ('https://newsapi.org/v2/everything?'
       'q=Bitcoin&'
	   'language=en&'
       'from='+str(date_str)+'&'
       'sortBy=popularity&'
	   'pageSize=10&'
	   'page=1&'
       'apiKey=72c815576bf74fa88660849971ed592e')
	  
	response = requests.get(url_googlenews_api)
	if response.status_code == 200:
		return response.json()
	else:
		sys.exit(20)

#To do: filter number
def filter_text(text):
	#tokenize text
	list_mots = text.lower().split(' ')
	#filter ponctuations and stopwords
	list_mots = [mot.strip(CHAR_TO_REMOVE) for mot in list_mots]
	list_mots = [mot for mot in list_mots if mot not in STOPWORDS and mot != '' and '+' not in mot]
	#lemmatize words
	wordnet_lemmatizer = WordNetLemmatizer()
	list_mots = [wordnet_lemmatizer.lemmatize(mot) for mot in list_mots]
	list_mots = [wordnet_lemmatizer.lemmatize(mot, pos='v') for mot in list_mots]
	return list_mots

def get_aggregated_text(formatted_data):
	aggregated_mots = []
	for i in formatted_data:
		date, list_mots = i
		aggregated_mots += list_mots
	return aggregated_mots
	
def format_data(raw_data):
	formatted_data = []
	for i in range (len(raw_data['articles'])):
		#text_article = (raw_data["articles"][i]["title"])+' '+(raw_data["articles"][i]["description"])
		text_article = (raw_data["articles"][i]["description"])
		formatted_words_list = filter_text(text_article)
		date_article = (raw_data["articles"][i]["publishedAt"])
		formatted_data.append((date_article, formatted_words_list))
	return formatted_data
	
def extract_features(list_words):
	Word2Vec
	return vector
	
def prepare_data(rdd):
	rdd = rdd.map(lambda (indice, list): LabeledPoint(indice, extract_features(list)))
	return rdd
	
def split_data(rdd):
	SPLIT_WEIGHT = 0.7
	(rdd_train, rdd_test) = rdd.randomSplit([SPLIT_WEIGHT, 1.0 - SPLIT_WEIGHT])
	return (rdd_train, rdd_test)
	
def train_model(rdd_train):
	
	return True
	
def test_model():
	return True
	
def get_variation_value(date_str, date_next_str):
	date = date_str
	date_suiv = date_next_str
	bitcoin_data_date = (retrieve_bitcoin_cours(date))
	valeur_day = bitcoin_data_date["_source"]["rate"]
	
	bitcoin_data_date = (retrieve_bitcoin_cours(date_suiv))
	valeur_day_next = bitcoin_data_date["_source"]["rate"]
	
	difference = valeur_day_next - valeur_day
	# print (valeur_day)
	# print (valeur_day_next)
	print (valeur_day_next-valeur_day)
	return float(1) if difference >= 0 else float(0)

def get_next_day(date_str):
	date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
	next_day = date + timedelta(days=1)
	next_date_str = next_day.strftime("%Y-%m-%d")
	return next_date_str
	
def main():
	date_start = '2016-01-01'
	date_end = '2016-01-04'
	date_search = date_start
	
	tuples_list = []
	while (date_search != date_end):
		data_list = get_aggregated_text(format_data(retrieve_data_day(date_search)))
		data_list = [mot.encode('utf-8') for mot in data_list]
		diff = get_variation_value(date_search, get_next_day(date_search))
		diff_wordslist = (diff, data_list)
		tuples_list.append(diff_wordslist)
		date_search = get_next_day(date_search)
		
	'''data_list = get_aggregated_text(format_data(retrieve_data_day(date_search)))
	#data_list = [mot.encode('utf-8') for mot in data_list]
	for i in data_list:
		print i.encode('utf-8')'''

	'''date = '2017-01-05'
	date_suiv = get_next_day(date)
	date_next2 = get_next_day(date_suiv)
	diff_5_6 = get_variation_value(date, date_suiv)
	diff_6_7 = get_variation_value(date_suiv, date_next2)
	# Retrieve data from GoogleNews API
	raw_data = retrieve_data_day(date)
	# Format data from raw data to list of tuple (date, article_description) and filter ponctuations, stopwords and empty words
	formatted_data = format_data(raw_data)
	# Aggregate data from list of tuple to a single list of words
	aggregated_data_j1 = get_aggregated_text(formatted_data)
	aggregated_data_j1 = [mot.encode('utf-8') for mot in aggregated_data_j1]
	tuple1 = (diff_5_6, aggregated_data_j1)
	
	aggregated_data_j2 = get_aggregated_text(format_data(retrieve_data_day(date_suiv)))
	aggregated_data_j2 = [mot.encode('utf-8') for mot in aggregated_data_j2]
	tuple2 = (diff_6_7, aggregated_data_j2)
	
	tuples_list = []
	tuples_list.append(tuple1)
	tuples_list.append(tuple2)'''
	
	rdd = sc.parallelize(tuples_list)
	rdd = rdd.map(lambda (indice, list): Row(diff=indice, words=list))
	
	df_data = spark.createDataFrame(rdd)
	
	count_vectorizer = CountVectorizer(inputCol='words', outputCol='features')
	
	model_cv = count_vectorizer.fit(df_data)
	
	result = model_cv.transform(df_data)
	print('aaaaaaaaaaaaaa')
	print result.collect()
	#rdd = rdd.map(lambda (indice, list): (indice, list[0]))
	#print (aggregated_data)


if __name__ == "__main__":
	main()

