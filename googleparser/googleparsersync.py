from typing import List

import requests
from bs4 import BeautifulSoup

from .googleresult import GoogleResult


__all__ = ['GoogleParser']


class GoogleParser:
    def __init__(self):
        self.links: List[str] = []
        self.body: str = None
        self.non_filtered_links: List[str] = None
        self.links: List[str] = None
        self.bs: BeautifulSoup = None
        self.results: List[GoogleResult] = None

        # SearchParams
        # block class for top of position
        self.top_position_block = 'ZINbbc xpd O9g5cc uUPGi'
        # filtered class, for false position
        self.false_position_block = 'BNeawe vvjwJb AP7Wnd'

    def query(self, search_string) -> List[GoogleResult]:
        link = 'https://google.com/search?q={}'.format(search_string)
        response = requests.get(link)
        self.body = response.content.decode('utf-8', errors='ignore')
        self._get_links_with_soup()
        return self.results

    def _get_links_with_soup(self):
        self.bs = BeautifulSoup(self.body, 'html.parser')
        results = self.bs.find_all('div', {'class': self.top_position_block})
        results = list(filter(lambda i: self.false_position_block in str(i), results))

        self.results = []
        for result in results:
            res = GoogleResult.create_instance(len(self.results) + 1, result)
            if res:
                self.results.append(res)

    def get_str_results(self) -> str:
        return '\n'.join([str(res) for res in self.results])


if __name__ == '__main__':
    gp = GoogleParser()
    gp.query('bitcoin price')
    print(gp.get_str_results())
