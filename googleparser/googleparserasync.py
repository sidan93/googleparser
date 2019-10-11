from typing import List, Dict
from bs4 import BeautifulSoup
import aiohttp
import asyncio

from googleparser.googleresult import GoogleResult


__all__ = ['GoogleParserAsync']


class GoogleParserAsync:
    def __init__(self):
        self.links: List[str] = []
        self.body: str = None
        self.non_filtered_links: List[str] = None
        self.links: List[str] = None
        self.bs: BeautifulSoup = None
        self.results: Dict[str, List[GoogleResult]] = None

        # SearchParams
        # headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Cache-Control': 'no-cache',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }
        # block class for top of position
        self.top_position_block = 'ZINbbc xpd O9g5cc uUPGi'
        # filtered class, for false position
        self.false_position_block = 'BNeawe vvjwJb AP7Wnd'

    def query(self, search_strings: List[str]) -> Dict[str, List[GoogleResult]]:
        loop = asyncio.get_event_loop()
        results = {}
        calls = []

        for search_string in search_strings:
            calls.append(self._query(results, search_string))

        gather = asyncio.gather(*calls)
        loop.run_until_complete(gather)
        self.results = results
        return results

    async def _query(self, results: Dict, search_string):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            link = 'https://google.com/search?q={}'.format(search_string)
            response = await session.get(link)
            body = await response.text()
            results[search_string] = self.get_results(body)

    def get_results(self, body) -> List[GoogleResult]:
        self.bs = BeautifulSoup(body, 'html.parser')
        print(self.bs.prettify())
        results = self.bs.find_all('div', {'class': self.top_position_block})
        results = list(filter(lambda i: self.false_position_block in str(i), results))

        method_result = []
        for result in results:
            res = GoogleResult.create_instance(len(self.results) + 1, result)
            if res:
                method_result.append(res)
        return method_result

    def get_str_results(self) -> str:
        return '\n\n'.join(
            'Query: {} \n {}'.format(
                key,
                '\n'.join(str(value) for value in values)
            ) for key, values in self.results.items()
        )


if __name__ == '__main__':
    gp = GoogleParserAsync()
    gp.query(['bitcoin price'])
    print(gp.get_str_results())
