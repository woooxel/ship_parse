import requests
import mparse


API_link = 'https://api.telegram.org/bot5053636509:AAF0a7J3lsNF_Q0wFwJIDsrWTMa6uLkDflI'


updates = requests.get(API_link+"/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]

chat_id = message["from"]["id"]

text = mparse.parse()
print(text)


#text = message["text"]




sent_message = requests.get(API_link+f"/sendMessage?chat_id={chat_id}&text=Привет, ты написал {text}")