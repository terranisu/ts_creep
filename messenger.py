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
            set theBuddy to buddy "nkippers@unb.ca" of service id "4B4F0344-D715-42D0-A5A2-A3734A67CFD5"
            send "{}" to theBuddy
        end tell
        '''.format(message)
        self.connection.communicate(scpt)
