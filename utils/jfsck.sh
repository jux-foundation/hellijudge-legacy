#!/bin/sh

exec 2>/dev/null

kill `cat $JUDGE_PREFIX/judge.pid`
sleep 1
kill -s 9 `cat /var/run/judgeinit.lock0`
kill -s 9 `cat $JUDGE_PREFIX/judge.pid`

echo hasta la vista, baby! :-t
