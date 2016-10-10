import sys
from core.config import Config as config

class Generator:
	def __init__(self,name,password):
		self.password = password
		self.name = name

	def set_generator(self):
		shell = self.name.partition('.')
		if shell[2] == "php":
			print 'Creating Shell file...'
			creating = self.php()
		if creating:
			print(config.ROBOT_NAME+'@shuffle[~]$> Shell was created! in '+config.OUTPUT_SHELL_DIR+self.name)
		else:
			print(config.ROBOT_NAME+"@shuffle[~]$> Something went wrong")
		sys.exit(1)	

	def php(self):
		try:
			file = open(config.OUTPUT_SHELL_DIR+self.name, 'w')
			file.close()
			with open(config.SHELL_DIR+config.SHELL_PHP) as f:
				with open(config.OUTPUT_SHELL_DIR+self.name, "w") as f1:
					for line in f:
						if "<password>" in line:
							f1.write("protected static $password = '"+self.password+"';")
						else:
							f1.write(line)
		except:
			return False
		return True
