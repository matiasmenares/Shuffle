import sys
import os
import urllib  
import json

class Server:

	def __init__(self,url,password):
		self.url = url
		self.password = password

	def conect(self):
		targer = urllib.urlopen(self.url+"?pass="+self.password)
		if targer.getcode() == 200:
			htmlSource = targer.read()
			j = json.loads(htmlSource)
			return j
		else:
			print "robot@shuffle[~]$ Server Not Respond."
			sys.exit(2)
		
	def server_info(self):
		targer = urllib.urlopen(self.url+"?pass="+self.password)
		if targer.getcode() == 200:
			htmlSource = targer.read()
			j = json.loads(htmlSource)
			return j['server_info']	