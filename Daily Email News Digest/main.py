import requests
from send_email import send_email

api_key="47fa2572b9004ba88f7835c66fb2f8c8"

topic = "houthis"
url = ('https://newsapi.org/v2/everything?'
       f"q={topic}&"
       'sortBy=publishedAt&'
       'language=en&'
       'apiKey=47fa2572b9004ba88f7835c66fb2f8c8')
#make request
request =  requests.get(url)

#dictionory of response
content =  request.json()

message = "Subject: Today's news" + "\n"
count = 1
#access the acrticle titles and description
for article in content["articles"][:20]:
    title = article["title"]
    description = article["description"]
    message = message +"\n" +title.title() +"\n" \
        + description + "\n" +article["url"]\
        +"\n" + "\n"

    
    
message = message.encode("utf-8")
send_email(message)
print("message sent")