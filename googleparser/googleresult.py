import re
from urllib.parse import unquote
from bs4 import ResultSet


__all__ = ['GoogleResult']


class GoogleResult:
    def __init__(self, index: int, title: str, link: str):
        self.index = index
        self.title = title
        self.link = link

    @staticmethod
    def create_instance(index: int, block: ResultSet) -> 'GoogleResult':
        try:
            title = block.find('div', {'class': 'BNeawe vvjwJb AP7Wnd'}).text
            link = unquote(re.search(r'((https|http):\/\/[^&]*)', block.find('a').attrs.get('href'))[0])
            return GoogleResult(
                index,
                title,
                link
            )
        except:
            pass

    def __str__(self) -> str:
        return '#{}. {}. Link: {}'.format(
            self.index,
            self.title,
            self.link
        )
