import cfscrape

class TicketSwapScrapper(object):
    def __init__(self, url):
        self.url = url
        self.scrapper = self.get_scrapper()

    def get_scrapper(self):
        return cfscrape.create_scraper()

    def get_content(self):
        return self.scrapper.get(self.url).content
