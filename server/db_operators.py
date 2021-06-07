import mysql.connector
import pandas as pd
# from datetime import date
from datetime import datetime
import random

class Db_Operators:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="okjimmyu",
            database="python_server"
        )

        self.mycursor = self.mydb.cursor()

    def query_db(self, sql, commit=False):
        self.mycursor.execute(sql)
        if commit == False:
            return self.mycursor.fetchall()
        else:
            self.mydb.commit()
            print( self.mycursor.rowcount, "record inserted.")


    def get_nearest(self, area):

        if area == 1.46:
            near = self.query_db(f'Select * From Parking_Slots WHERE Free=False AND Area = 1.46')
        elif area == 4.16:
            near = self.query_db(f'Select * From Parking_Slots WHERE Free=False AND Area = 4.16')
        elif area < 4.16:
            near = self.query_db(f'Select * From Parking_Slots WHERE Free=False AND Area BETWEEN 1.46 AND {area}')
        else:
            near = self.query_db(f'Select * From Parking_Slots WHERE Free=False AND Area BETWEEN 4.16 AND {area}')

        slots = {}

        for i in range(random.randrange(5, 20)):
            id = random.randint(0, len(near)-1)
            slots[near[id][0]] = near[id]

        for x in slots:
            print (slots[x])

    def get_timezone(self, current_day):
        '''
        Morning   -> 6:00-12:00,  Noon  -> 12:00-17:00
        Afternoon -> 17:00-22:00, Night -> 22:00-6:00
        '''

        time = int(current_day.strftime("%H"))

        if 6 <= int(time) <= 12:
            return 'Morning'
        elif 12 <= int(time) <= 17:
            return 'Noon'
        elif 17 <= int(time) <= 22:
            return 'Afternoon'
        else:
            return 'Night'

    def park_action(self, p_id, type):
        current_day = datetime.now()
        today = current_day.strftime("%Y-%m-%d")
        print (f'\ntoday: {today}')
        month = current_day.strftime("%B")
        print (f'month: {month}')
        time = current_day.strftime("%H:%M:%S")
        print (f'time: {time}\n')

        park = self.query_db(f'UPDATE Parking_Slots SET Free = true WHERE ID={p_id}', True)
        park_sum = self.query_db(f'UPDATE Parking_Slots SET Sum = Sum + 1 WHERE ID={p_id}', True)

        exists = self.query_db(f'Select COUNT(1) From Dates WHERE Parking_ID={p_id} AND Parking_Date={today}')
        
        types = self.query_db(f'Select COUNT(1) From Types WHERE Parking_ID={p_id} AND Parking_Date={today}')

        months = self.query_db(f'Select COUNT(1) From Months WHERE Parking_ID={p_id}')
        if months[0][0] == 1:
            self.query_db(f'UPDATE Months SET {month} = {month} + 1 WHERE Parking_ID={p_id}', True)

        timezone = self.query_db(f'Select COUNT(1) From Timezone WHERE Parking_ID={p_id}')
        if timezone[0][0] == 1:
            current_timezone = self.get_timezone(current_day)
            self.query_db(f'UPDATE Timezone SET {current_timezone} = {current_timezone} + 1 WHERE Parking_ID={p_id}', True)

    def unpark_action(self, p_id):
        unpark = self.query_db(f'UPDATE Parking_Slots SET Free = 0 WHERE ID={p_id}', True)

    def get_details(self, p_id):

        sum = self.query_db(f'Select Sum From Parking_Slots WHERE ID={p_id}')

        mnths = self.query_db(f'Select * From Months WHERE Parking_ID={p_id}')

        tmzn = self.query_db(f'Select * From Timezone WHERE Parking_ID={p_id}')

        tps = self.query_db(f'Select Type From Types WHERE Parking_ID={p_id}')

        details = {

            'months': {
                'January': str((mnths[0][2])/sum[0][0]*100)[:5] + "%",
                'February': str((mnths[0][3]/sum[0][0])*100)[:5] + "%",
                'March': str((mnths[0][4]/sum[0][0])*100)[:5] + "%",
                'April': str((mnths[0][5]/sum[0][0])*100)[:5] + "%",
                'May': str((mnths[0][6]/sum[0][0])*100)[:5] + "%",
                'June': str((mnths[0][7]/sum[0][0])*100)[:5] + "%",
                'July': str((mnths[0][8]/sum[0][0])*100)[:5] + "%",
                'August': str((mnths[0][9]/sum[0][0])*100)[:5] + "%",
                'September': str((mnths[0][10]/sum[0][0])*100)[:5] + "%",
                'October': str((mnths[0][11]/sum[0][0])*100)[:5] + "%",
                'November': str((mnths[0][12]/sum[0][0])*100)[:5] + "%",
                'December': str((mnths[0][13]/sum[0][0])*100)[:5] + "%"},

            'timezone': {
                'Morning': str((tmzn[0][2])/sum[0][0]*100)[:5] + "%",
                'Noon': str((tmzn[0][3]/sum[0][0])*100)[:5] + "%",
                'Afternoon': str((tmzn[0][4]/sum[0][0])*100)[:5] + "%",
                'Night': str((tmzn[0][5]/sum[0][0])*100)[:5] + "%",},

            'types': self.get_types(tps, sum[0][0])
        }

        print (details)


    def get_types(self, tps, sum):
        lst = {}
        final_lst = {}

        for x in tps:
            if x[0] in lst:
                lst[x[0]] = lst[x[0]] + 1
            else:
                lst[x[0]] = 1

        for x in lst:
            final_lst[x] = str(lst[x]/sum)[:5] + "%"

        return final_lst
