import sys
import logging

from random import randrange

import numpy as np

import messenger
import scrapper
from bs4 import BeautifulSoup
import sched
import time

# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(handler)

# LOGGER = logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class TicketSwapTrigger(object):
    def __init__(self, main_url, t_min=5, t_max=10):
        self.main_url = main_url
        self.t_min = t_min
        self.t_max = t_max
        self.messenger = messenger.Message()
        self.scapper = scrapper.TicketSwapScrapper(self.main_url)
        self.content = None
        self.refresh_count = 0

    def send_message(self, message):
        self.messenger.send_message(message)

    def send_url_message(self):
        self.send_message(self.main_url)

    def get_web_content(self):
        return self.scapper.get_content()

    def get_pretty_content(self):
        return BeautifulSoup(self.get_web_content(), "lxml")

    def get_content_values(self):
        try:
            self.content = self.get_pretty_content()
        except:
            self.send_message('Connection died')
            self.run_task()

    def get_ticket_values(self):
        self.get_content_values()
        tickets = self.content.find_all("div", class_="counter-value")
        ticket_count = {}
        try:
            ticket_count['offered'] = int(tickets[0].get_text())
            ticket_count['sold'] = int(tickets[1].get_text())
            ticket_count['wanted'] = int(tickets[2].get_text())
        except IndexError:
            ticket_count['offered'] = np.nan
            ticket_count['sold'] = np.nan
            ticket_count['wanted'] = np.nan
        return ticket_count

    def refresh_content(self, s):
        self.refresh_count += 1
        LOGGER.info('Resfresh count: %s', self.refresh_count)
        ticket_count = self.get_ticket_values()
        LOGGER.info('Tickets available: %s', ticket_count['offered'])
        LOGGER.info('Tickets sold: %s', ticket_count['sold'])
        if ticket_count['offered'] > 0:
            self.send_message('There is a ticket available')
            for i in range(50):
                LOGGER.info('+++++++++++++++++++++++++++++++++++++++++++++')

        else:
            time_delay = randrange(self.t_min, self.t_max)
            LOGGER.info('Time delay: %s', time_delay)
            LOGGER.info('=====================')
            if ticket_count['offered'] is not np.nan:
                s.enter(time_delay, 1, self.refresh_content, (s,))
            else:
                self.send_message('You are a robot, increase the time')
                LOGGER.criticl('You are a robot')

    def run_task(self):
        s = sched.scheduler(time.time, time.sleep)
        s.enter(1, 1, self.refresh_content, (s,))
        s.run()


if __name__ == '__main__':
    url = 'https://www.ticketswap.com/event/mastodon/3fbfe1b5-a457-4b3e-b7ff-bab5cc25a866'
    concert = TicketSwapTrigger(main_url=url, t_min=2, t_max=5)
    concert.run_task()
