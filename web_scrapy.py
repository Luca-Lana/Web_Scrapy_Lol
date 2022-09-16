import requests
from bs4 import BeautifulSoup


class WebScrapyLol:

    __header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    __boots = ['botas da rapidez', 'botas ionianas da lucidez', 'botas da mobilidade', 'botas galvanizadas de aço', 'grevas do berserker', 'sapatos do feiticeiro', 'passos de mercúrio']
        
    @classmethod
    def get_runes(cls, champion, role):
        html = requests.get(f'https://br.op.gg/champions/{champion}/{role}/build?hl=pt_BR', headers=cls.__header)
        soup = BeautifulSoup(html.content, 'html.parser')
        runes = [rune.get('alt') for rune in soup.select('div.item img') if 'grayscale' not in rune.get('src')]

        return False if not runes else {runes[0]: runes[1:5], runes[5]: runes[6:]}

    @classmethod
    def get_speel(cls, champion, role):
        html = requests.get(f'https://br.op.gg/champions/{champion}/{role}/build?hl=pt_BR', headers=cls.__header)
        soup = BeautifulSoup(html.content, 'html.parser')
        speels = [speel.get('alt') for speel in soup.select('div.css-0 img')]

        return False if not speels else {'speel_1': speels[:2], 'speel_2': speels[2:]}

    @classmethod
    def get_build(cls, champion, role):
        html = requests.get(f'https://br.op.gg/champions/{champion}/{role}/build?hl=pt_BR', headers=cls.__header)
        soup = BeautifulSoup(html.content, 'html.parser')
        items = [item.get('alt') for item in soup.select('div.item_icon img')]
        index_boots = []
        boots = []

        for index, item in enumerate(items):
            if item.lower() in cls.__boots:
                index_boots.append(index)
                boots.append(item)

        return False if not items else {'starter_items': items[:index_boots[0]], 'boots': boots, 'build': [items[index_boots[1]+1:index_boots[1]+4], items[index_boots[1]+4:index_boots[1]+7] ]}

    @classmethod
    def get_summoner(cls, region, nick):
        nick.replace(' ', '%20')
        html = requests.get(f'https://br.op.gg/summoners/{region}/{nick}', headers=cls.__header)
        soup = BeautifulSoup(html.content, 'html.parser')
        level = soup.select_one('.level').get_text()
        rank = [{rank.parent.parent.parent.select_one('.header').get_text(): rank.get_text().capitalize()} for rank in soup.select('.tier')]

        return False if not level else {'nick': nick, 'level': level, 'rank': rank}
