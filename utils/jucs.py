#!/usr/bin/python

import os
import socket

def submit (sid, user, prob, lang, addr, host = "127.0.0.1", port = 31415):
	child_pid = os.fork()
	if child_pid == 0:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect( (host, port) )
		sock.send("""{SID} {USER} {PROB} {LANG} {ADDR} 
				0""".format(SID=sid, USER=user, PROB=prob, LANG=lang, ADDR=addr))
		sock.close()
	else:
		return 0
