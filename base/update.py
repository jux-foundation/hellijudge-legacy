#!/usr/bin/env python2

#   update.py
#   Copyright (C) 2011  Hamed Saleh and Mahrud Sayrafi

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import MySQLdb

HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USERNAME")
PASS = os.getenv("DB_PASSWORD")
NAME = os.getenv("DB_NAME")

conn = MySQLdb.connection (host=HOST, user=USER, passwd=PASS, db=NAME)

strstat = [ 'Accepted!', 'Wrong answer', 'Time limit exceeded', 'Memory limit exceeded',
		'Run time error', 'Unexpected error', 'Signal #' ]

def status (query, SUBID, status, test = -1, time = -1, mem = -1, score = -1):
	if query == 'COMPILE':
		if status == -1:
			msg = 'compiling...'
		elif status == 0:
			msg = 'successfully compiled'
		elif status == 124:
			msg = 'compile time limit exceeded'
		else:
			msg = 'compilation error'

		conn.query ("""UPDATE `submitions` 
						SET status='{MSG}' WHERE id='{SUBID}'""".format (MSG = msg, SUBID = SUBID))

	elif query == 'RUN':
		if status == -1:
			if test == -1:
				msg = 'running...'
			else:
				msg = 'running on test ' + str (test + 1)
		else:
			msg = 'running on test ' + str (test + 1)

		conn.query ("UPDATE `submitions` SET status='{MSG}' WHERE id='{SUBID}'".format (MSG = msg, SUBID = SUBID))
		
		return status > 0

	elif query == 'END':
		if status == -1:
			status = 5;

		msg = strstat [min (6, status)]

		if status > 5:
			msg += str (status - 6)

		if status > 0:
			msg += ' on test ' + str (test + 1)

		conn.query ("""UPDATE `submitions` 
						SET status='{MSG}' WHERE id='{SUBID}'""".format (MSG = msg, SUBID = SUBID))
