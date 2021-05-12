import datetime


colors = {
    'OKBLUE': '\033[94m', 'HEADER': '\033[95m', 'WARNING': '\033[93m',
    'OKCYAN': '\033[96m', 'BOLD': '\033[1m', 'FAIL': '\033[91m',
    'OKGREEN': '\033[92m', 'UNDERLINE': '\033[4m', 'ENDC': '\033[0m',
}

def get_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def op_log (msg, completed=False):

    if completed == False:
        print (f"[    ]  {get_time()}  {msg}")
    else:
        print (f"[ {colors['OKGREEN']}OK{colors['ENDC']} ]  {get_time()}  {msg}")

def info (msg):
    print (f"[{colors['OKBLUE']}INFO{colors['ENDC']}]  {get_time()}  {msg}")
