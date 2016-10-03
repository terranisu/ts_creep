import messenger
import scrapper
from bs4 import BeautifulSoup

class TicketSwapTrigger(object):
    def __init__(self, main_url):
        self.main_url = main_url
        self.test_message = messenger.Message()
        self.scapper = scrapper.TicketSwapScrapper(self.main_url)

    def send_successful_message(self, message):
        test_message.send_message(message)

    def send_url_message(self):
        self.send_successful_message(str(self.main_url))

    def get_web_content(self):
        return self.scapper.get_content()

    def get_pretty_content(self):
        return BeautifulSoup(self.get_web_content(), "html5lib")


# r = urllib.urlopen('https://www.ticketswap.com/event/frank-carter-the-rattlesnakes-/dae96a33-5093-4218-b2fe-3db3b2681450').read()
# soup = BeautifulSoup(r, "html5lib")
# tickets = soup.find_all("div", class_="counter-value")
# available_tickets = int(tickets[0].get_text())
