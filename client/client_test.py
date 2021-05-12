from profile import Profile
from data import make_dir, store
import json

v1 = {  'category': 'cat1', 'type': 'type1', 'model': 'model1', 'size': 'size1',
        'registration_plate': 'plate1', 'use': 'use1', 'preference': True}

v2 = {  'category': 'cat2', 'type': 'type2', 'model': 'model2', 'size': 'size2',
        'registration_plate': 'plate2', 'use': 'use2', 'preference': False}

v4 = {  'category': 'cat4', 'type': 'type4', 'model': 'model4', 'size': 'size4',
        'registration_plate': 'plate4', 'use': 'use4', 'preference': False}

# a = {'v3': [5]}
# op = Operators()
make_dir()
store('vehicle', v1)
store('vehicle', v2)
store('vehicle', v4)
# op.update('vehicle', a)
# index = op.load('vehicle')
# print (index)
#
# op.update('vehicle', b)
# index = op.load('vehicle')
# # for i in int(len(index)):
# 	print (index[i])
# [ OK ]
# [INFO]
# -ERROR-
# WARNING
