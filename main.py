import messenger

class TicketSwapTrigger(object):
    def __init__(self, main_url):
        self.main_url = main_url
        self.test_message = messenger.Message()

    def send_successful_message(self, message):
        test_message.send_message(message)

    def send_url_message(self):
        self.send_successful_message(str(self.main_url))
