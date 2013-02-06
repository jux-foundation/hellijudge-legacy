#!/usr/bin/env python2
#
#	core.py
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
import sys
import run
import config
import update

# Reading common options from env:
MODE_DIR = os.getenv("MODE_DIR")
COMPILER = os.getenv("COMPILER")
LOGGER = os.getenv("LOGGER")

# Reading user's code options from env
USER = os.getenv("USER")
SUBID = os.getenv("SUBID")
PROBLEM = os.getenv("PROBLEM")
LANGUAGE = os.getenv('LANGUAGE')

# Reading problem specific options from problem config
CONFIG = config.parse()

# Initializing log
prefix = SUBID + ':' + USER + ':' + PROBLEM + ':' + LANGUAGE + ': '
logmsg = ''

# Start compiling
update.status ('COMPILE', SUBID, -1)
compret = os.system (COMPILER + ' ' + LANGUAGE)
compret /= 256

update.status ('COMPILE', SUBID, compret)

if compret == 124:		# Compile time limit exceeded, refer to Gnu timeout manual
	logmsg = 'Compile time limit exceeded'
elif compret:			# Unspecified Compilation error
	logmsg = 'Compilation error'
else:
	# Start running
	update.status ('RUN', SUBID, -1, -1);
	arr = run.main (CONFIG)

	charstat = 'CWTMRU'	# [ correct, wrong, time, memory, runtime, unexpected ]

	for status in arr: 
		if status > 5:
			logmsg += '[' + str(status - 6) + ']'
		else:
			logmsg += charstat[status]

os.system (LOGGER + ' LOG grading ' + prefix + logmsg)

if HOST != "":
	update.conn.close()
