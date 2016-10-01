import sys
import os
import urllib  
import json
import requests
import subprocess
from core.config import Config as config
from subprocess import call, STDOUT

class Version:
	def __init__(self):
		self.repo_url = config.REPO_URL
	def is_git(self):
		if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
			return False
		else:
			return True

	def update(self):
		if self.is_git():
			if self.repo_up():
				True
				
			
	def current_commit_hash(self):
		return subprocess.check_output(['git', 'rev-parse', 'HEAD'])

	def compare_commit(self):
		if self.current_commit_hash() === self.repo_commit_hash():
			return False
		else:
			return True

	def repo_commit_hash(self):
		request = json.loads(requests.get(self.repo_url).text)
		return request['object']['sha']

	def repo_up(self):
		try: 
			request = urllib.urlopen(self.repo_url)
			if request.getcode() == 200:
				return True
			else:
				return False
		except:
				return False