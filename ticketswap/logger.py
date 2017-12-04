import logging

class Logger(object):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)
        self.log.addHandler(self.__init_handler)

    def __init_handler(self):
      handler = logging.StreamHandler()
      formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
      )
      handler.setFormatter(formatter)
      return handler

