"""Defines Monitor"""

import yaml
import sched
import time

from random import randrange
from bs4 import BeautifulSoup
# from cart import Cart as TicketSwapCart
from scrapper import Scrapper as TicketSwapScrapper
from message import Message as TicketSwapMessage

class Monitor(object):
    SCHEDULER_DELAY = 1
    SCHEDULER_PRIORITY = 1

    def __init__(self, url, config, logger=None):
        self.iterations = 0
        self.url = url
        self.logger = logger
        self.scrapper = TicketSwapScrapper(self.logger)
        self.message = TicketSwapMessage(self.logger)
        self.__init_from_config(config)

    def run(self):
        if self.logger:
            self.logger.info("Iteration: %s", self.iterations)
            self.logger.info("Scheduler in running...")
        scheduler = sched.scheduler(time.time, time.sleep)
        scheduler.enter(self.SCHEDULER_DELAY, self.SCHEDULER_PRIORITY, self.__callback, (scheduler,))
        scheduler.run()

    # Private section

    def __callback(self, scheduler):
        self.iterations += 1
        tickets = self.__get_tickets_count()
        if tickets["offered"] > 0:
            self.message.send(self.phone, "Here is a ticket")
            if self.logger:
                self.logger.info("Iteration: %s", self.iterations)
                self.logger.info("Tickets available: %s", tickets["offered"])
                self.logger.info("Tickets sold: %s", tickets["sold"])
                self.logger.info("Tickets wanted: %s", tickets["wanted"])
                self.logger.info("Trying to buy the ticket...")
            # TicketSwapCart(self.url).authorize(self.user, self.password).add()
            return
        else:
            delay = randrange(self.SCHEDULER_DELAY, self.limit)
            scheduler.enter(delay, self.SCHEDULER_PRIORITY, self.__callback, (scheduler,))
            self.message.send(self.phone, "There is no ticket")
            if self.logger:
                self.logger.info("Iteration: %s", self.iterations)
                self.logger.info("There are not available tickets")
                self.logger.info("Waiting for %s seconds...", delay)

    def __get_tickets_count(self):
        try:
            content = BeautifulSoup(self.scrapper.get_content(self.url), "lxml")
            elements = content.find_all("div", class_="counter-value")
            return {
                "offered": self.__get_element_value(elements[0]),
                "sold": self.__get_element_value(elements[1]),
                "wanted": self.__get_element_value(elements[2])
            }
        except:
            if self.logger:
                self.logger.info("Unable to fetch the data. Rescheduling the monitor...")
            self.run()

    def __get_element_value(self, element):
        try:
            int(element.get_text())
        except IndexError:
            return 0

    def __init_from_config(self, config):
        self.limit = config.limit
        if config.file is None:
            self.user = config.user
            self.password = config.password
            self.phone = config.phone
        else:
            settings = self.__load_config(config.file)
            (self.user, self.password) = settings["credentials"]
            self.phone = settings["receivers"]["phone"]
        if self.user is None or self.password is None:
            raise ValueError("You need to input Facebook user/password or use settings file")

    def __load_config(self, filename):
        with open(filename, "r") as ymlfile:
            return yaml.load(ymlfile)
