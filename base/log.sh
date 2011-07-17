#!/bin/sh
#
#	log.sh
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

COMMAND=$1 shift
FILE=$1 shift
TEXT=$@

LOG_DIR="/judge/log"

if [ $COMMAND == "LOG" ]; then
	echo [`date $LOG_DATE_FORMAT`] $PID: $TEXT >>$LOG_DIR/$FILE.log
elif [ $COMMAND == "ARCHIVE" ]; then
	mv $LOG_DIR/$FILE.log $LOG_DIR/$FILE.log-`date +%Y%m%d`
	bzip2 $LOG_DIR/$FILE.log-`date +%Y%m%d` #$FILE.log --suffix=-`date +%Y%m%d`
fi
