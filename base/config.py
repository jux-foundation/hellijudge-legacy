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

def parse():
	PROBCONF = open (PROBCONFADDR, 'r')

	COUNT = int (PROBCONF.readline().strip())
	CONFMOD = PROBCONF.readline().strip()

	CONFIG = []

	if CONFMOD == 'default':
		confline = PROBCONF.readline().strip()
		for i in range(COUNT):
			CONFIG.append (confline.replace ('%n', str(i)).split())
	else:
		for i in range(COUNT):
			confline = PROBCONF.readline()
			CONFIG.append (confline.replace ('%n', str(i)).split())

	PROBCONF.close()

	return [COUNT, CONFIG]
