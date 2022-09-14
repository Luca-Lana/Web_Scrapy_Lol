import requests
from bs4 import BeautifulSoup

class InfoLol:

    def __init__(self, champion, lane, header = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}):
        self.__champion = champion
        self.__lane     = lane
        self.__header   = header
        self.__boots = ['botas da rapidez', 'botas ionianas da lucidez', 'botas da mobilidade', 'botas galvanizadas de aço', 'grevas do berserker', 'sapatos do feiticeiro', 'passos de mercúrio']
        self.__correct_lane()

    def __correct_lane(self):
        if self.__lane == 'sup':
            self.__lane = 'support'
        elif self.__lane == 'jg':
            self.__lane = 'jungle'

    def __get_html(self):   
        html = requests.get(f'https://br.op.gg/champions/{self.__champion}/{self.__lane}/build?hl=pt_BR', headers=self.__header)
        soup = BeautifulSoup(html.content, 'html.parser')

        return soup
    
    def get_runes(self):
        html = self.__get_html()
        runes = [rune.get('alt') for rune in html.select('div.item img') if 'grayscale' not in rune.get('src')]

        return {runes[0] : runes[1:5], runes[5] : runes[6:]}

    def get_speel(self):         
        html = self.__get_html()
        speels = [speel.get('alt') for speel in html.select('div.css-0 img')]

        return {'speel_1' : speels[:2], 'speel_2' : speels[2:]}

    def get_build(self):
        html = self.__get_html()
        items = [item.get('alt') for item in html.select('div.item_icon img')]
        index_boots = []
        boots = []

        for index, item in enumerate(items):
            if item.lower() in self.__boots:
                index_boots.append(index)
                boots.append(item)

        return {'starter_items': items[:index_boots[0]], 'boots': boots, 'build': [items[index_boots[1]+1:index_boots[1]+4], items[index_boots[1]+4:index_boots[1]+7] ]}
        
        


print(InfoLol('lux', 'sup').get_build())
