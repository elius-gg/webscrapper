import argparse
import logging
logging.basicConfig(level=logging.INFO)
import news_page_objects as news


from common import config

logger = logging.getLogger(__name__)


def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logger.info(f'Beginning scraper for {host}')
    homepage = news.HomePage(news_site_uid)

    for link in homepage.article_links:
        print(link)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    news_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site', help='El sitio a scrapear', type=str, choices=news_site_choices)


    args = parser.parse_args()
    _news_scraper(args.news_site)