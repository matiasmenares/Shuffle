from random import randint

class Banner:
	def __init__(self):
		self.rand = randint(0,2)

	def get_banner(self):
		print "\n"   
		for line in open("extras/banner-"+str(self.rand)+".txt"):
			print line,
		print "\n"   
		print "     [*]------------------- WebShell Ver. 0.1 @matiasmenares -------------------[*]\n"
		print "     	  [*]------------------- Fork me on github -------------------[*]\n"
		print "\n"
