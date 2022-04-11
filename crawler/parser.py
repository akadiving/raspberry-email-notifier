import requests
from bs4 import BeautifulSoup
from crawler.utils import convert_list_to_dict
from crawler.constants import HEADERS, URL


class Parser:
    """
    Parser class that converts html response in to a json object
    """

    def __init__(self):
        self.page = requests.get(URL, headers=HEADERS).text
        self.parser_class = 'html.parser'
        self.sample = []
        self.data = []
        self.data_keys = ['name', '', 'last_updated', 'shop', 'available', 'date', 'price']
        self.headers = HEADERS
        self.soup = BeautifulSoup(self.page, self.parser_class)


    def _initial_results(self, max=None):
        return self.soup.find_all("tr", limit=max)

    def parse(self, result_count=None):
        for pi in self._initial_results(result_count):
            raspberry=pi.find_all('td')
            if len(raspberry) == 0:
                continue
            for i, v in enumerate(raspberry):
                if len(v.text) == 0:
                    continue
                self.sample.append(self.data_keys[i])
                self.sample.append(v.text)
            self.sample.append('link')
            self.sample.append(pi.a)
            self.data.append(convert_list_to_dict(self.sample))
        return self.data
