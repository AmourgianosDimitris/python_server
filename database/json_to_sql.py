import os
import json

def bytype():
    f = open('json_files/bytype.json')
    data = json.load(f)
    f.close()

    insert_into = []

    for item in data:
        keys = []
        values = []
        for key, value in item.items() :
            keys.append(key)
            values.append(value)
        sql_command = f"INSERT INTO Types ({keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}) VALUES ({values[0]}, {values[1]}, '{values[2]}', '{values[3]}');\n"
        insert_into.append(sql_command)

    with open('sql_files/types.sql', 'w') as file:
        for item in insert_into:
            file.write(item)
        file.close()

def bydate():
    f = open('json_files/bydate.json')
    data = json.load(f)
    f.close()

    insert_into = []

    for item in data:
        keys = []
        values = []
        for key, value in item.items() :
            keys.append(key)
            values.append(value)
        sql_command = f"INSERT INTO Dates ({keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}) VALUES ({values[0]}, {values[1]}, '{values[2]}', {values[3]});\n"
        insert_into.append(sql_command)

    with open('sql_files/dates.sql', 'w') as file:
        for item in insert_into:
            file.write(item)
        file.close()


def bymonth():
    f = open('json_files/bymonth.json')
    data = json.load(f)
    f.close()

    insert_into = []

    for item in data:
        keys = []
        values = []
        for key, value in item.items() :
            keys.append(key)
            values.append(value)
        sql_command = f"INSERT INTO Months ({keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}, {keys[4]}, {keys[5]}, {keys[6]}, {keys[7]}, {keys[8]}, {keys[9]}, {keys[10]}, {keys[11]}, {keys[12]}, {keys[13]}) VALUES ({values[0]}, {values[1]}, {values[2]}, {values[3]}, {values[4]}, {values[5]}, {values[6]}, {values[7]}, {values[8]}, {values[9]}, {values[10]}, {values[11]}, {values[12]}, {values[13]});\n"
        insert_into.append(sql_command)

    with open('sql_files/months.sql', 'w') as file:
        for item in insert_into:
            file.write(item)
        file.close()


def bytimezone():
    f = open('json_files/bytimezone.json')
    data = json.load(f)
    f.close()

    insert_into = []

    for item in data:
        keys = []
        values = []
        for key, value in item.items() :
            keys.append(key)
            values.append(value)
        sql_command = f"INSERT INTO Timezone ({keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}, {keys[4]}, {keys[5]}) VALUES ({values[0]}, {values[1]}, {values[2]}, {values[3]}, {values[4]}, {values[5]});\n"
        insert_into.append(sql_command)

    with open('sql_files/timezone.sql', 'w') as file:
        for item in insert_into:
            # print (item)
            file.write(item)
        file.close()

def main_table():
    f = open('json_files/data.json')
    data = json.load(f)
    f.close()

    # a='┬'
    b='├'
    c='└'
    d=''

    insert_into = []

    for item in data:
        keys = []
        values = []
        for key, value in item.items() :
            keys.append(key)
            values.append(value)
        sql_command = f"INSERT INTO Parking_Slots ({keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}, {keys[4]}, {keys[5]}, {keys[6]}, {keys[7]}, {keys[8]}) VALUES ({values[0]}, {values[1]}, {values[2]}, {values[3]}, {values[4]}, '{values[5]}', {values[6]}, {values[7]}, {values[8]});\n"
        insert_into.append(sql_command)

    with open('sql_files/parking_slots.sql', 'w') as file:
        for item in insert_into:
            # print (item)
            file.write(item)
        file.close()

# main_table()
# bytimezone()
# bymonth()
# bydate()
bytype()
