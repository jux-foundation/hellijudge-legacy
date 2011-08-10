#!/bin/sh
#
#	jail.sh
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

TEST=$1 shift
TIME_LIMIT=`expr 2 \* $1` shift
FIRST_INPUT=$@

FIFORUN="/tmp/fiforun$$"

{
	mkfifo $FIFORUN
#	exec 3<>$FIFORUN

	sh -c "$FIRST_INPUT" >$FIFORUN &
	sleep 0.1
	coproc $TESTER $INIT_DIR/$TEST.init >$FIFORUN &

	exec <$FIFORUN >&${COPROC[1]}	\
		$TIME -f "result $TIME_FORMAT"	\
		$TIMEOUT --signal=SIGKILL $TIME_LIMIT	\
		$SU $RUN_USER \
		$SU_SYNTAX $OUT
#		$SU_SYNTAX "$OUT 2>/dev/null"				# FIXME
}  2>&1

rm -f $FIFORUN
