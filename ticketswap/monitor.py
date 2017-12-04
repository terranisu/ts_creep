import yaml

class TicketSwapMonitor(object):
    def __init__(self, url, config):
        self.logger = None
        self.url = url
        self.limit = config.limit
        self.__init_credentials(config)

    def set_logger(self, logger):
        self.logger = logger

    def run(self):
        print self.logger
        print 'Run method'

    # Private section

    def __init_credentials(self, config):
        if config.file is not None:
            (self.user, self.password) = self.__load_config(config.file)
        else:
            self.user = config.user
            self.password = config.password
        if not self.user or not self.password:
            raise ValueError('You need to input Facebook user/password or use credentials file')

    def __load_config(self, filename):
        with open(filename, 'r') as ymlfile:
            return yaml.load(ymlfile)['credentials']
