import sys
import os
import urllib  
import json
import requests
import httplib
from core.config import Config as config

class Server:

	def __init__(self,url,password):
		self.url = url
		self.password = password

	def connection(self):
		if self.beat():
			request = json.loads(requests.post(self.url, data = {'pass': self.password,'cmd': "shuffle-auth"}).text)
			if request['response'] == 'true':
				return {'response': 'true','cookie': request['connection']['cookie']}
			else:
				return {'response': False,'msg': request['msg'] }
	
	def beat(self):
		try: 
			request = urllib.urlopen(self.url)
			if request.getcode() == 200:
				return True
			else:
				print config.ROBOT_NAME+'@shuffle[~]$> Server Not Respond'
				sys.exit(2)
		except:
			print config.ROBOT_NAME+'@shuffle[~]$> Server Not Respond'
			sys.exit(2)

	def info(self, cookie):
		connection = self.connection()
		if connection["response"] == "true":
			request = json.loads(requests.post(self.url, data= {'pass': self.password}, cookies=cookie).text)
			return request['server_info']	
			
			
			
