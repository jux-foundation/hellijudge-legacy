#!/bin/sh
#
#	daemon.sh
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

PID=$$
LOCK="$JUDGE_PREFIX/judge.pid"

echo $PID >$LOCK
echo "Judge daemon started ... pid=$PID" >&2

export CHROOT=`which chroot`
export SU=`which su`
export TIME=`which time`
export TIMEOUT=`which timeout`

export JUDGE='/judge'

export BASE="$JUDGE/base"
export INIT="$BASE/init.sh"
export CORE="$BASE/core.py"
export LOGGER="$BASE/log.sh"
export JAILER="$BASE/jail.sh"
export COMPILER="$BASE/compile.sh"

export LOG_DIR="$JUDGE/log"

export JAIL="$JUDGE/jail"
export SU_SYNTAX="--session-command"

export PROBLEMS_DIR="$JUDGE/problems"

export COMPILER_DIR="/bin/compilers"
export CODE_DIR='/source'				# FIXME
export BIN_USER=0
export BIN_GROUP=0
export COMPILE_TIME=10                  # FIXME

export RUN_DIR='/home'                  # FIXME
export RUN_USER='judge'					# FIXME
export RUN_GROUP=99

export LOG_DIR="$JUDGE/log"
export LOG_DATE_FORMAT="--rfc-3339=ns"

export TIME_FORMAT='%e %M %x'

export DB_HOST='127.0.0.1'
export DB_USERNAME=''
export DB_PASSWORD=''
export DB_NAME=''

PORT=31415
FIFO="/tmp/fifo$PID"

rm -f /tmp/fifo*
mkfifo $FIFO

trap "{ killall -9 nc init.sh daemon.sh
		rm -f $FIFO $LOCK;	}" EXIT

while true
do
{
	echo .
	sh $INIT < $FIFO &
	nc -l $PORT > $FIFO
}
done

rm -f $FIFO $LOCK
