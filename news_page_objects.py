import requests as rq
import bs4

from common import config

class HomePage:

    def __init__(self, news_site_uid):
        self._config = config()['news_sites'][news_site_uid]
        self._queries = self._config['queries']
        self._html = None
        self._visit(self._config['url'])

    
    @property
    def article_links(self):
        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)

        return set(link['href'] for link in link_list)

    
    def _select(self, query_string):
        return self._html.select(query_string)


    def _visit(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        response = rq.get(url, headers=headers)

        response.raise_for_status()

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')