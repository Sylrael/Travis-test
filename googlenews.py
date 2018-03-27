import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=72c815576bf74fa88660849971ed592e')
res = requests.get(url)
# print (res.json())

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=72c815576bf74fa88660849971ed592e')
response = requests.get(url)
# print (response.json())

url = ('https://newsapi.org/v2/everything?'
       'q=Bitcoin&'
       'from=2018-03-27&'
       'sortBy=popularity&'
       'apiKey=72c815576bf74fa88660849971ed592e')

response = requests.get(url)
print (response.json())