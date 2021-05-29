import random

v_type = {1.46: ['TW'],
          1.50: ['L1e', 'L2e'],
          1.80: ['L1e', 'L2e', 'L4e'],
          2.00: ['L1e', 'L2e', 'L4e', 'L5e-A'],
          2.10: ['L1e', 'L2e', 'L4e', 'L5e-A', 'L3e'],
          4.00: ['L1e', 'L2e', 'L4e', 'L5e-A', 'L3e', 'L5e-B'],
          4.16: ['TW', '3W'],
          5.36: ['TW', '3W', 'CS'],
          6.71: ['TW', '3W', 'CS', 'LCV'],
          8.11: ['TW', '3W', 'CS', 'LCV', 'CB'],
          15.41: ['TW', '3W', 'CS', 'LCV', 'CB', 'HCV'],
          25.44: ['TW', '3W', 'CS', 'LCV', 'CB', 'HCV', 'B'],
          27.83: ['TW', '3W', 'CS', 'LCV', 'CB', 'HCV', 'B', 'MAV']}

print (random.choice(v_type[25.44]))
