import logging


import requests
from bs4 import BeautifulSoup

def parse(ships_url):
    URL = ships_url
    #URL = 'https://www.vesselfinder.com/ru/vessels/NS-CAPTAIN-IMO-9341067-MMSI-636012659'
    #URL = 'https://www.vesselfinder.com/ru/vessels/NS-CLIPPER-IMO-9341081-MMSI-636012661'
    HEADERS = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        'accept-Language': 'en',
    }
    response = requests.get(URL, headers=HEADERS).text
    soup = BeautifulSoup(response, 'lxml')

    block = soup.find('div', {"class":"vi__r1 vi__sbt"})
    port = block.find('a', {'class':'_npNa'}).text
    return port







