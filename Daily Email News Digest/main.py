import requests
from send_email import send_email

api_key="47fa2572b9004ba88f7835c66fb2f8c8"


url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'language=en&'
       'apiKey=47fa2572b9004ba88f7835c66fb2f8c8')
#make request
request =  requests.get(url)

#dictionory of response
content =  request.json()

message = ""
count = 1
#access the acrticle titles and description
for article in content["articles"]:
    title = article["title"]
    description = article["description"]
    message = message + f"News {count}:" \
        +"\n" +title +"\n" + description +"\n"
    count+=1
    
    
message = message.encode("utf-8")
send_email(message)
print("message sent")