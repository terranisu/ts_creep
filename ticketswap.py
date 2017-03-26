from __future__ import print_function, division
from random import randrange
import numpy as np

import messenger
import scrapper
from bs4 import BeautifulSoup
import sched
import time


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
        print('1')
        self.get_content_values()
        print('g')
        tickets = self.content.find_all("div", class_="counter-value")
        print('2')
        ticket_count = {}
        print('3')
        try:
            ticket_count['offered'] = int(tickets[0].get_text())
            ticket_count['sold'] = int(tickets[1].get_text())
            ticket_count['wanted'] = int(tickets[2].get_text())
        except IndexError:
            ticket_count['offered'] = np.nan
            ticket_count['sold'] = np.nan
            ticket_count['wanted'] = np.nan
        print('4')
        return ticket_count

    def refresh_content(self, s):
        self.refresh_count += 1
        print('Resfresh count WTF: {}'.format(self.refresh_count))
        ticket_count = self.get_ticket_values()
        print('Tickets available: {}'.format(ticket_count['offered']))
        print('Tickets sold: {}'.format(ticket_count['sold']))
        if ticket_count['offered'] > 0:
            self.send_message('There is a ticket available')
        else:
            time_delay = randrange(self.t_min, self.t_max)
            print('Time delay: {}'.format(time_delay))
            print('=====================')
            if ticket_count['offered'] is not np.nan:
                s.enter(time_delay, 1, self.refresh_content, (s,))
            else:
                self.send_message('You are a robot, increase the time')
                print('You are a robot')

    def run_task(self):
        s = sched.scheduler(time.time, time.sleep)
        s.enter(1, 1, self.refresh_content, (s,))
        s.run()

if __name__ == '__main__':
    url = 'https://www.ticketswap.nl/event/meshuggah/14c0a986-09f6-48aa-bfd1-400e7913c967'
    concert = TicketSwapTrigger(main_url=url, t_min=120, t_max=300)
    concert.run_task()
