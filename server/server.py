#!/usr/bin/env python3

import socket
import json
from threading import Thread
from socketserver import ThreadingMixIn
from db_operators import Db_Operators
from logs import op_log, info
from clientthread import ClientThread


#Connect to MySql database
# logs = Logs()

op_log("Connecting", "to Database")
db = Db_Operators()
if db.mydb:
    op_log("Connected", " to Database", True)

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0'
TCP_PORT = 1500
BUFFER_SIZE = 1024  # Usually 1024, but we need quick response

op_log("Starting", "Server")
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []
op_log("Started", " Server", True)

op_log("Waiting", "for Clients")
while True:
    tcpServer.listen(4)
    (conn, (ip,port)) = tcpServer.accept()
    newthread = ClientThread(ip, port, conn, db)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
