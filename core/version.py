import sys
import os
import json
import requests
import subprocess
import git
from core.config import Config as config
from subprocess import call, STDOUT

class Version:
	def __init__(self):
		self.remote_repo = config.REPO_URL
		self.home_repo = git.cmd.Git(os.getcwd())

	def is_git(self):
		if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
			return False
		else:
			return True

	def update(self):
		if self.is_git():
			if self.repo_up():
				if self.compare_commit():
					self.loop_update()

	def loop_update(self):
		question = raw_input("Exist new version of this software, do you want update? [Y/n]")
		if question is None or question == "y" or question == "Y":
			self.update_repo()
		else:
			False
			
	def current_commit_hash(self):
		return subprocess.check_output(['git', 'rev-parse', 'HEAD'])

	def compare_commit(self):
		if str(self.current_commit_hash()).strip() == str(self.repo_commit_hash().strip()):
			return False
		else:
			return True

	def update_repo(self):
		out = self.home_repo.pull()
		print out
		print "Done."

	def repo_commit_hash(self):
		request = json.loads(requests.get(self.remote_repo).text)
		return request['object']['sha']

	def repo_up(self):
		try: 
			request = urllib.urlopen(self.remote_repo)
			if request.getcode() == 200:
				return True
			else:
				return False
		except:
				return False