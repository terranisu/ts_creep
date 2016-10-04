from __future__ import print_function, division
from random import randrange
import numpy as np

import messenger
import scrapper
from bs4 import BeautifulSoup
import sched, time


class TicketSwapTrigger(object):
    def __init__(self, main_url, t_min=5, t_max=10):
        self.main_url = main_url
        self.t_min = t_min
        self.t_max = t_max
        self.messenger = messenger.Message()
        self.scapper = scrapper.TicketSwapScrapper(self.main_url)
        self.content = None

    def send_message(self, message):
        self.messenger.send_message(message)

    def send_url_message(self):
        self.send_message(self.main_url)

    def get_web_content(self):
        return self.scapper.get_content()

    def get_pretty_content(self):
        return BeautifulSoup(self.get_web_content())

    def get_content_values(self):
        self.content = self.get_pretty_content()

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

    def refreash_content(self, s):
        ticket_count = self.get_ticket_values()
        if ticket_count['offered'] > 0:
            self.send_message('There is a ticket available')
        else:
            time_delay = randrange(self.t_min, self.t_max)
            print('Time delay: {}'.format(time_delay))
            if ticket_count['offered'] is not np.nan:
                s.enter(time_delay, 1, self.refreash_content, (s,))
            else:
                self.send_message('You are a robot, increase the time')
                print('You are a robot')

    def run_task(self):
        s = sched.scheduler(time.time, time.sleep)
        s.enter(1, 1, self.refreash_content, (s,))
        s.run()
