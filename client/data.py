import os
import json

# class Operators:
    # def __init__(self):
savedir = f'data'
colors = {
    'OKBLUE': '\033[94m', 'HEADER': '\033[95m', 'WARNING': '\033[93m',
    'OKCYAN': '\033[96m', 'BOLD': '\033[1m', 'FAIL': '\033[91m',
    'OKGREEN': '\033[92m', 'UNDERLINE': '\033[4m', 'ENDC': '\033[0m',
}
def make_dir():
    try:
        os.mkdir(f'{savedir}')
    except:
        pass

def save(name, index):
    try:
        with open( f'{savedir}/{name}.json', 'w') as f:
            json.dump(index, f)
            f.close()
    except:
        print(f"{colors['FAIL']}ERROR{colors['ENDC']} Something went wrong when writing to the file: {name}")


def store(name, obj):
    if not os.path.isfile(f'./{savedir}/{name}.json'):
        save(name, {1:obj})
    else:
        try:
            with open( f'./{savedir}/{name}.json', 'r') as f:
                data = json.load(f)
                max_id = 0
                for d_id, d_info in data.items():
                    print (d_id)
                    if int(d_id) > max_id:
                        max_id = int(d_id)
            f.close()
            data[max_id+1] = obj
            save(name, data)
        except:
            print(f"{colors['FAIL']}ERROR{colors['ENDC']} Something went wrong when writing to the file: {name}")
