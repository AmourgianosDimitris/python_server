# #!/usr/bin/env python3
import socket
import pickle
import pandas as pd

host = socket.gethostname()
port = 1500
BUFFER_SIZE = 2000

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

open = True
while open:
    req = input("Give your request: ")
    p_req = {'request': req}
    # print (jsonResult['request'])
    serialise = pickle.dumps(p_req)
    # bluh = pickle.loads(jsonResult)
    tcpClientA.send(req)
    # data = pd.read_pickle(tcpClientA.recv(BUFFER_SIZE))
    data = tcpClientA.recv(BUFFER_SIZE)
    print (" Client2 received data:", data)
    MESSAGE = input("tcpClientA: Enter message to continue/ Enter exit:")

tcpClientA.close()
