from subprocess import Popen, PIPE


class Message(object):
	def __init__(self):
		self.connection = self.make_connection()

	def make_connection(self):
		args = ['2', '2']
		p = Popen(['osascript', '-'] + args,
				  stdin=PIPE, stdout=PIPE, stderr=PIPE)
		return p
	def send_message(self, message='default message'):
		scpt = '''
		tell application "Messages"
			set theBuddy to buddy "nkippers@unb.ca" of service id "DC5C9C11-2799-4D88-B7D7-3E3AB3ED7FA2"
			send "{}" to theBuddy
		end tell
		'''.format(message)
		self.connection.communicate(scpt)
