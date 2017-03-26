from subprocess import Popen, PIPE


class Message(object):
    def __init__(self):
        self.connection = self.make_connection()

    def make_connection(self):
        args = ['2', '2']
        p = Popen(['osascript', '-'] + args, stdin=PIPE,
                  stdout=PIPE, stderr=PIPE)
        return p

    # def send_message(self, message='default message'):
    #     scpt = '''
    #     tell application "Messages"
    #         set theBuddy to buddy "nkippers@unb.ca" of service id "E:nkippers@unb.ca"
    #         send "{}" to theBuddy
    #     end tell
    #     '''.format(message)
    #     self.connection.communicate(scpt)

    def send_message(self, message='default message'):
        scpt = '''
        tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "nkippers@unb.ca" of targetService
        send {} to targetBuddy
    end tell
        '''.format(message).encode()
        args = ['2', '2']
        p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        p.communicate(scpt)
        # self.connection.communicate(scpt)
