import os
import json

class Operators:
    def __init__(self):
        self.savedir = f'data'
        self.colors = {
            'OKBLUE': '\033[94m', 'HEADER': '\033[95m', 'WARNING': '\033[93m',
            'OKCYAN': '\033[96m', 'BOLD': '\033[1m', 'FAIL': '\033[91m',
            'OKGREEN': '\033[92m', 'UNDERLINE': '\033[4m', 'ENDC': '\033[0m',
        }
        try:
            os.mkdir(f'{self.savedir}')
        except:
            pass

    def open_file(self, name):
        try:
            f = open( f'{self.savedir}/{name}.json')
        except:
            print(f'Something went wrong trying opening the file: {name}')
        else:
            return f

    def save(self, name, index):
        try:
            f = self.open_file(name)
            json.dump(index, f)
        except:
            print(f"{self.colors['FAIL']}ERROR{self.colors['ENDC']} Something went wrong when writing to the file: {name}")
        finally:
            f.close()

    def load(self, name):
         f = self.open_file(name)
         index = json.load(f)
         return index
        # try:
        #     f = self.open_file(name)
        #     index = json.load(f)
        #     return index
        # except:
        #     print(f"{self.colors['FAIL']}ERROR{self.colors['ENDC']} Something went wrong when loading the file: {name}")
        # finally:
        #     f.close()

    def update(self, name, obj):
    	index = self.load(name)
    	# print (int(len(index)+1))
    	# index[int(len(index)+1)] = obj
    	self.save(name, obj)
