"""Defines TicketSwapLogger"""

import logging

class TicketSwapLogger(object):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)
        self.log.addHandler(self.__init_handler())

    def __getattr__(self, method_name):
        return getattr(self.log, method_name)

    # Private section

    def __init_handler(self):
      handler = logging.StreamHandler()
      formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
      )
      handler.setFormatter(formatter)
      return handler

