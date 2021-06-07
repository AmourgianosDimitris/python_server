from datetime import datetime, time

current_day = datetime.now().time()
# print (f'current_day: {current_day}')
# time = current_day.strftime("%H:%M:%S")
time = int(current_day.strftime("%H"))
# time = 15
# print (time)
# print (time('6','0'))
# print (datetime.time(6, 0))
if 6 <= int(time) <= 12:
    return 'Morning'
elif 12 <= int(time) <= 17:
    return 'Noon'
elif 17 <= int(time) <= 22:
    return 'Afternoon'
else:
    return 'Night'
