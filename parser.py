import logging


import requests
import bs4


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('mt')



class Client:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
            'accept-Language':'en',
        }


    def load_page(self):
        url = 'https://www.vesselfinder.com/ru/vessels/NS-CLIPPER-IMO-9341081-MMSI-636012661'
        res = self.session.get(url=url)
        res.raise_for_status()   #возвращает коды ответа, если возврашает код 400 или больше, то код должен возвращать ошибку
        return res.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('div.vi__r1.vi__sbt')
        for block in container:
            self.parse_block(block=block)


    def parse_block(self, block):
        logger.info(block)
        logger.info('='*100)


    def run(self):
        text = self.load_page()
        self.parse_page(text=text)

if __name__ == '__main__':
    parser = Client()
    parser.run()


