"""Defines TicketSwapMonitor"""

import yaml
import sched
import time

from random import randrange
from bs4 import BeautifulSoup
from scrapper import TicketSwapScrapper
from logger import TicketSwapLogger

class TicketSwapMonitor(object):
    SCHEDULER_DELAY = 1
    SCHEDULER_PRIORITY = 1

    def __init__(self, url, config):
        self.iterations = 0
        self.url = url
        self.limit = config.limit
        self.verbose = config.verbose
        self.__init_credentials(config)
        self.logger = TicketSwapLogger()
        self.scrapper = TicketSwapScrapper()

    def run(self):
        if self.verbose:
            self.logger.info('iteration: %s', self.iterations)
            self.logger.info('run scheduler')
        scheduler = sched.scheduler(time.time, time.sleep)
        scheduler.enter(self.SCHEDULER_DELAY, self.SCHEDULER_PRIORITY, self.__callback, (scheduler,))
        scheduler.run()

    # Private section

    def __callback(self, scheduler):
        self.iterations += 1
        tickets = self.__get_tickets_count()
        if tickets['offered'] > 0:
            if self.verbose:
                self.logger.info('iteration: %s', self.iterations)
                self.logger.info('Tickets available: %s', tickets['offered'])
                self.logger.info('Tickets sold: %s', tickets['sold'])
                self.logger.info('Tickets wanted: %s', tickets['wanted'])
            # Add the found ticket to a cart
            print 'Add ticket'
        else:
            delay = randrange(self.SCHEDULER_DELAY, self.limit)
            scheduler.enter(delay, self.SCHEDULER_PRIORITY, self.__callback, (scheduler,))
            if self.verbose:
                self.logger.info('iteration: %s', self.iterations)
                self.logger.info('There are not available tickets')
                self.logger.info('Waiting for %s sec...', delay)


    def __get_tickets_count(self):
        try:
            return {
                'offered': 0,
                'sold': 0,
                'wanted': 0
            }
            # content = BeautifulSoup(self.scrapper.get_content(self.url), "lxml")
            # counters = content.find_all("div", class_="counter-value")
            # return {
            #     'offered': self.__get_counter(counters[0]),
            #     'sold': self.__get_counter(counters[1]),
            #     'wanted': self.__get_counter(counters[2])
            # }
        except:
            # self.send_message('Connection died')
            self.run()

    def __get_counter(self, counter):
        try:
            int(counter.get_text())
        except IndexError:
            return 0

    def __init_credentials(self, config):
        if config.file is None:
            self.user = config.user
            self.password = config.password
        else:
            (self.user, self.password) = self.__load_config(config.file)
        if self.user is None or self.password is None:
            raise ValueError('You need to input Facebook user/password or use credentials file')

    def __load_config(self, filename):
        with open(filename, 'r') as ymlfile:
            return yaml.load(ymlfile)['credentials']
