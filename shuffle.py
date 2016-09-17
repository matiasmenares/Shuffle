#!/usr/bin/python
# import requests
#
# Author(s): Matias Menares (Gh0st)
# The Super Shell
from core.config import Config
from core.terminal import Terminal
from core.server import Server
from core.generate import Generator
from core.banner import Banner
import os
import urllib  
import json
import argparse
import sys
import sqlite3 as lite

parser = argparse.ArgumentParser()
parser.add_argument("-u", help="Url")
parser.add_argument("-g", help="Generate Shell")
parser.add_argument("-p", help="Password")
args = parser.parse_args()
#BANNER
banner = Banner()
banner.get_banner()
params = parser.parse_args()
def main(params):
	if params.u and params.p:
		url = params.u
		password = params.p
	if params.g and params.p:
		shell.set_generator()
	if params.u and params.p:
		conection = Terminal(params.u,params.p)			
		conection.loop_terminal()
if __name__ == '__main__':
	terminal = Terminal(params.u,params.p)
	shell = Generator(params.g,params.p)

try:
    main(params)
except (KeyboardInterrupt, EOFError):
    log.info('Exiting.')
