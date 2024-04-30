import requests

api_key="47fa2572b9004ba88f7835c66fb2f8c8"


url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'language=en&'
       'apiKey=47fa2572b9004ba88f7835c66fb2f8c8')
#make request
request =  requests.get(url)

#dictionory of response
content =  request.json()

#access the acrticle titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

