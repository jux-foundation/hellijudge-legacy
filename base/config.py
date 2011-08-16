#!/usr/bin/env python2
#
#	config.py:	parse problem config
#	Copyright (C) 2011  Hamed Saleh and Mahrud Sayrafi

#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.

#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.

#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

PROBCONFADDR = os.getenv('PROBCONFADDR')
INPUT_DIR = os.getenv('INPUT_DIR')

class Config:
	def __init__(self, address):
		self.data = []
		self.address = address
	
	def parse(self):
		PROBCONF = open (self.address, 'r')

		self.count = int (PROBCONF.readline().strip())
		CONFMOD = PROBCONF.readline().strip()

		if CONFMOD == 'default':
			confline = PROBCONF.readline().strip()
			for i in range(self.count):
				self.data.append (confline.replace ('%n', str(i)).split())
		else:
			for i in range(self.count):
				confline = PROBCONF.readline()
				self.data.append (confline.replace ('%n', str(i)).split())

		PROBCONF.close()

	def input_command(self, test):
		input_command = INPUT_DIR + '/' + self.data[test][3];

		if (self.data[test][0] == 'normal'):
			input_command = 'cat ' + input_command
		return input_command
	
	def get_limits(self, test):
		return [int(self.data[test][1]), int(self.data[test][2])]

def parse():
	CONFIG = Config (PROBCONFADDR)
	CONFIG.parse()
	return CONFIG
