#!/bin/sh

LOCK=$JUDGE_PREFIX/judge.pid	#FIXME

if [ -e $LOCK ]
then
	PID=`cat $LOCK`

	if ps $PID >/dev/null
	then
		echo "Daemon is already running and it's PID is $PID." >&2
		exit 1
	else
		rm -f $LOCK
	fi
fi

sh $JUDGE_PREFIX/base/daemon.sh &>> $JUDGE_PREFIX/log/error.log &
