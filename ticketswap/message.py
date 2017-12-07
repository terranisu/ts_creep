"""Defines Message"""

from subprocess import Popen, PIPE

class Message(object):
    def __init__(self, logger=None):
      self.logger = logger

    def send(self, phone, message):
        cmd = ['osascript', 'scripts/message.applescript', phone, message]
        if self.logger:
            self.logger.info("Sending message...")
            self.logger.info("Performed command: %s", cmd)
        p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        p.communicate()
