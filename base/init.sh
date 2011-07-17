#!/bin/sh
#
#	init.sh
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

export PID=$$

read SUBID USER PROBLEM LANGUAGE CODE TEST

if [ -z "$SUBID" -o -z "$USER" -o -z "$PROBLEM" \
	   -o -z "$LANGUAGE" -o -z "$CODE" -o -z "$TEST" ]
then
	sh $LOGGER LOG error "receiving initial variables failed"
	exit 1
fi

sh $LOGGER LOG error "init started ..."

# TODO seams buggy FIXME
LOCK="/var/run/judgeinit.pid"
while [ -e $LOCK ]
do
	LOCK_PID=`cat $LOCK`
	if ! ps $LOCK_PID >/dev/null
	then
		rm -f $LOCK
	else
		sleep 1
	fi
done
echo $PID >$LOCK

export SUBID=$SUBID
export PROBLEM=$PROBLEM
export PROBLEM_DIR="$PROBLEMS_DIR/$PROBLEM"
export PROBCONFADDR="$PROBLEM_DIR/config"
export TESTER="$PROBLEM_DIR/tester"
export INIT_DIR="$PROBLEM_DIR/inits"
export TEST_INIT="$INIT_DIR/$TEST.init"
export INPUT_DIR="$PROBLEM_DIR/inputs"
export TEST_INPUT="$INPUT_DIR/$TEST.in"

export USER=$USER
export LANGUAGE=$LANGUAGE
export SOURCE="$CODE_DIR/$SUBID-$PROBLEM-$USER.$LANGUAGE"				# FIXME
export OUT="$RUN_DIR/$SUBID.out"

cp -f $CODE $JAIL$SOURCE

sh $LOGGER LOG error "core started ..."

python $CORE

rm -f $LOCK
