from profile import Profile
from data import Operators
import json

a = {'v1': [1,2,3]}
b = {'v2': [4,5,6]}
c = {'v3': [7,8,9]}

# a = {'v3': [5]}
op = Operators()
op.save('vehicle', a)
# op.update('vehicle', a)
index = op.load('vehicle')
print (index)
#
# op.update('vehicle', b)
# index = op.load('vehicle')
# # for i in int(len(index)):
# 	print (index[i])
