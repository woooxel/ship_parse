import requests
from bs4 import BeautifulSoup
import urllib

def wikiparse(wiki_name):
    URL = 'https://ru.wikipedia.org/wiki/'
    backurl = str(URL.__add__(wiki_name))
    HEADERS = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        'accept-Language': 'en',
    }
    response = requests.get(backurl, headers=HEADERS).text
    bs = BeautifulSoup(response, 'lxml')
    back_1 = bs.find_all('p')
    for back_1 in back_1:
        return back_1.text


#wikiparse('Голова')
# print(wikiparse('Голова'))
#print(wikiparse('Нога'))