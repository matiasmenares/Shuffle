import sys
import os
import urllib  
import json

class Terminal:

	def __init__(self,url,password):
		self.url = url
		self.password = password

	def terminal(self,send):
		command = self.command(send)
		if command == False:
			return self.execute(send)

	def command(self,send):
		if send == "exit":
			print "\nBye :)"
			sys.exit(2)
		else:
			return False

	def execute(self,input):
		targer = urllib.urlopen(self.url+"?cmd="+input+"&pass="+self.password)
		if targer.getcode() == 200:
			htmlSource = targer.read()
			response = json.loads(htmlSource)
			return response
		else:
			print "No response"
			sys.exit(2)