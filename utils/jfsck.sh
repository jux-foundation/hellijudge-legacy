#!/bin/sh

set -e

exec 2>/dev/null

[ -e $JUDGE_PREFIX/judge.pid ] && kill `cat $JUDGE_PREFIX/judge.pid`
sleep 1
[ -e $JUDGE_PREFIX/init.pid  ] && kill -s 9 `cat $JUDGE_PREFIX/init.pid`
[ -e $JUDGE_PREFIX/judge.pid ] && kill -s 9 `cat $JUDGE_PREFIX/judge.pid`

rm -f $JUDGE_PREFIX/init.pid
rm -f $JUDGE_PREFIX/judge.pid

rm -f $FIFO $LOCK

echo hasta la vista, baby! :-t
