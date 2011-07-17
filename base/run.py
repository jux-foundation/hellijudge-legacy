#!/usr/bin/env python2
#
#	run.py
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
import update

SUBID = os.getenv("SUBID")
LOGGER = os.getenv("LOGGER")
JAILER = os.getenv("JAILER")
INPUT_DIR = os.getenv("INPUT_DIR")

def run (testnum, CONFIG):
	TIMELIM = CONFIG[1]
	MEMLIM = CONFIG[2]
	INPUT_COMMAND = INPUT_DIR + '/' + CONFIG[3]

	if (CONFIG[0] == 'normal'):
		INPUT_COMMAND = 'cat ' + INPUT_COMMAND

#	print JAILER + ' ' + str (testnum) + ' ' + str(TIMELIM) + ' ' + INPUT_COMMAND

	update.status ('RUN', SUBID, -1, testnum)

	stdin = os.popen (JAILER + ' ' + str (testnum) + ' ' + str(TIMELIM) + ' ' + INPUT_COMMAND , 'r')

	status = time = mem = ret = score = -1

	while True:
		line = stdin.readline()

		if not line:	break

		result = line.strip().split(' ')

		if result[0].isdigit():
			score = int (result[0])
		elif result[0] == "result":
			time = float (result[1])
			mem = int (result[2])
			ret = int (result[3])

	if ret > 127:			status = 6 + retstat - 128	# signal
	elif ret > 124:			status = 5					# unexpected
	elif ret == 124:		status = 2					# time
	elif ret != 0:			status = 4					# runtime
	elif mem > MEMLIM:		status = 3					# memory
	elif time > TIMELIM:	status = 2					# time
	elif score <= 0:		status = 1					# wrong
	else:					status = 0					# correct

	os.system(LOGGER + " LOG error {0} {1} {2} {3} {4} {5} {6}".format(SUBID, status, testnum, time, mem, ret, score))

	error = update.status ('RUN', SUBID, status, testnum, time, mem, score)

	return [status, error]

#strstat = [ 'Accepted!', 'Wrong answer', 'Time limit exceeded', 'Memory limit exceeded', 'Run time error', 'Unexpected error', 'Signal #' ]

def main(COUNT, CONFIG):
	arr = []
	for i in range(COUNT):
		[status, error] = run (i, CONFIG[i])
		arr.append(status)
		if error:
			break

	update.status ('END', SUBID, status)

	return arr
