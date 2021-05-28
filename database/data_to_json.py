import os
import json
import random
import datetime

emv = [1.46, 1.50, 1.80, 2.00, 2.10, 4.00, 4.16, 5.36, 6.71, 8.11,  15.41, 25.44, 27.83]

def get_date():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2022, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date

def bydate():
    f = open('json_files/data.json')
    data = json.load(f)
    f.close()

    list = []

    reps = 0
    for i in data:

        dict= {}
        id = i['ID']
        sum = i['Sum']

        while sum >= 0:
            if sum == 0:
                break

            reps = reps + 1
            
            total = random.randint(0, 20)
            if total == 0:
                break

            if sum > total:

                dict = {
                    'ID': reps,
                    'Parking_ID': i['ID'],
                    'Parking_Date': str(get_date()),
                    'Total': total
                }
                list.append(dict)
                sum = sum - total
            else:
                if sum < total:

                    dict = {
                        'ID': reps,
                        'Parking_ID': i['ID'],
                        'Parking_Date': str(get_date()),
                        'Total': sum
                    }
                    list.append(dict)
                    break


    with open( f'json_files/bydate.json', 'w') as h:
        json.dump(list, h)
        h.close()

def bymonth():
    months = ['January', ' February', ' March', ' April', ' May', ' June', ' July', ' August', ' September', ' October', ' November', ' December']

    f = open('json_files/data.json')
    data = json.load(f)
    f.close()

    list = []

    for i in data:
        dict = {}
        id = i['ID']
        sum = i['Sum']

        s1 = random.randint(0, sum)
        sum = sum - s1

        s2 = random.randint(0, sum)
        sum = sum - s2

        s3 = random.randint(0, sum)
        sum = sum - s3

        s4 = random.randint(0, sum)
        sum = sum - s4

        s5 = random.randint(0, sum)
        sum = sum - s5

        s6 = random.randint(0, sum)
        sum = sum - s6

        s7 = random.randint(0, sum)
        sum = sum - s7

        s8 = random.randint(0, sum)
        sum = sum - s8

        s9 = random.randint(0, sum)
        sum = sum - s9

        s10 = random.randint(0, sum)
        sum = sum - s10

        s11 = random.randint(0, sum)
        sum = sum - s11

        print (i['ID'], ":", i['Sum'], s1, s2, s3, sum)

        dict = {
            'ID': i['ID'],
            'Parking_ID': i['ID'],
            'January': s1,
            ' February': s2,
            ' March': s3,
            ' April': s4,
            ' May': s5,
            ' June': s6,
            ' July': s7,
            ' August': s8,
            ' September': s9,
            ' October': s10,
            ' November': s11,
            ' December': sum
        }
        list.append(dict)

    with open( f'json_files/bymonth.json', 'w') as h:
        json.dump(list, h)
        h.close()


def bytimezone():
    tz = ['Morning', 'Noon', 'Afternoon', 'Night']

    f = open('json_files/data.json')
    data = json.load(f)
    f.close()

    list = []

    for i in data:
        dict = {}
        id = i['ID']
        sum = i['Sum']

        s1 = random.randint(0, sum)
        sum = sum - s1

        s2 = random.randint(0, sum)
        sum = sum - s2

        s3 = random.randint(0, sum)
        sum = sum - s3

        print (i['ID'], ":", i['Sum'], s1, s2, s3, sum)

        dict = {
            'ID': i['ID'],
            'Parking_ID': i['ID'],
            'Morning': s1,
            'Noon': s2,
            'Afternoon': s3,
            'Night': sum
        }
        list.append(dict)

    with open( f'json_files/bytimezone.json', 'w') as h:
        json.dump(list, h)
        h.close()

def main_table():
    f = open('json_files/MOCK_DATA.json')
    data = json.load(f)
    f.close()

    for i in data:
        area = random.choice(emv)
        sum = random.randint(0, 1000)
        i['Area'] = area
        i['Sum'] = sum
        print (area, sum)
        # print(i['Street'])

    with open( f'json_files/data.json', 'w') as h:
        json.dump(data, h)
        h.close()

# main_table()
# bytimezone()
# bymonth()
bydate()
