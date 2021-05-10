import datetime


class Logs():
    def __init__(self):
        self.colors = {
            'OKBLUE': '\033[94m', 'HEADER': '\033[95m', 'WARNING': '\033[93m',
            'OKCYAN': '\033[96m', 'BOLD': '\033[1m', 'FAIL': '\033[91m',
            'OKGREEN': '\033[92m', 'UNDERLINE': '\033[4m', 'ENDC': '\033[0m',
        }

    def get_time(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def op_log (self, msg, completed=False):

        if completed == False:
            print (f"[    ]  {self.get_time()}  {msg}")
        else:
            print (f"[ {self.colors['OKGREEN']}OK{self.colors['ENDC']} ]  {self.get_time()}  {msg}")

    def info (self, msg):
        print (f"[{self.colors['OKBLUE']}INFO{self.colors['ENDC']}]  {self.get_time()}  {msg}")
