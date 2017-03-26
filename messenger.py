from subprocess import Popen, PIPE


class Message(object):
    def __init__(self):
        self.connection = self.make_connection()

    def make_connection(self):
        args = ['2', '2']
        p = Popen(['osascript', '-'] + args, stdin=PIPE,
                  stdout=PIPE, stderr=PIPE)
        return p

    def send_message(self, message='default message'):
        scpt = '''
        tell application "Messages"
	       send "{}" to buddy "nkippers@unb.ca" of (first service whose service type is iMessage)
        end tell'''.format(message).encode()

        args = ['2', '2']
        p = Popen(['osascript', '-'] + args,
                  stdin=PIPE, stdout=PIPE, stderr=PIPE)
        p.communicate(scpt)
        # self.connection.communicate(scpt)
