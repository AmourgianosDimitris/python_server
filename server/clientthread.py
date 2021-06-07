import socket
import pickle
from threading import Thread
from socketserver import ThreadingMixIn
from db_operators import Db_Operators
from logs import op_log, info

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):

    def __init__(self, ip, port, conn, db):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        self.db = db
        # self.logs = Logs()

        op_log('Connected', 'Client', True)
        info('Client:'', f'{self.ip}:{self.port}\n')

    def run(self):
        while True :
            op_log('Waiting', 'for Request')

            data = self.conn.recv(2048)
            op_log('Reicived', 'Request', True)


            resp = self.db.show_parking_slots()

            # jsonResult = {resp}
            # print(jsonResult['response'])
            # pickle_resp = pickle.dumps(resp)

            self.conn.send(resp)  # echo
