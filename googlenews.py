import requests

'''url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=72c815576bf74fa88660849971ed592e')
res = requests.get(url)
# print (res.json())

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=72c815576bf74fa88660849971ed592e')
response = requests.get(url)
# print (response.json())'''

def convert(input):
    if isinstance(input, dict):
        return dict((convert(key), convert(value)) for key, value in input.iteritems())
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

url = ('https://newsapi.org/v2/everything?'
       'q=Bitcoin&'
	   'language=en&'
       'from=2018-03-27&'
       'sortBy=relevancy&'
	   'pageSize=20&'
	   'page=1&'
       'apiKey=72c815576bf74fa88660849971ed592e')

response = requests.get(url)
data = response.json()
print (response.encoding)
data = convert(data)
print (data["totalResults"])

for i in range(len(data["articles"])):
	print (i)
	print (data["articles"][i]["title"])
	print (data["articles"][i]["description"])
	

