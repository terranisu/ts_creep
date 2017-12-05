import cfscrape

class TicketSwapScrapper(object):
    def __init__(self):
        self.scrapper = cfscrape.create_scraper()

    def get_content(self, url):
        if url is None:
            raise ValueError('Parameter "url" is empty')
        return self.scrapper.get(url).content
