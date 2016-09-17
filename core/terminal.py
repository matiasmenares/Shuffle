import sys
import os
import urllib  
import json
from core.server import Server

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

	def loop_terminal(self):
		Ser = Server(self.url,self.password)
		con = Ser.conect()
		if con['response'] == '200':
			print "#> Conecction Established, Enjoy!\n"
			server_info = Ser.server_info()
			while True:
				send = raw_input(server_info['server_name']+"@"+server_info['user']+"["+server_info['pwd']+"]"+server_info['user_bash']+">")
				termina = self.terminal(send)
				print termina['command']
		elif con['response'] == '302':
			print "robot@shuffle[~]$> Response: "+con['error']
		else:
			print "robot@shuffle[~]$> Connection fail."
