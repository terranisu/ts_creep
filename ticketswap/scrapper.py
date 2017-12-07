"""Defines Scrapper"""

import cfscrape

class Scrapper(object):
    def __init__(self, logger=None):
        self.scrapper = cfscrape.create_scraper()
        self.logger = logger

    def get_content(self, url):
        if url is None:
            raise ValueError('Parameter "url" is empty')
        if self.logger:
            self.logger.info("Fetching content from %s", url)
        return self.scrapper.get(url).content
