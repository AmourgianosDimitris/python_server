import mysql.connector
import pandas as pd
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

    def get_types(self, tps):
        lst = {}
        # for x in tps:
        #     if len(lst) == 0:

    def get_nearest(self):

        sql1 = f'Select * From Parking_Slots WHERE Free=False'
        self.mycursor.execute(sql1)
        near = self.mycursor.fetchall()

        slots = {}

        rng = random.randrange(5, 20)
        print (rng)
        for i in range(random.randrange(5, 20)):
            slots[i] = near[random.randint(0, len(near)-1)]

        print (slots)

    def get_details(self, p_id):

        sql1 = f'Select Sum From Parking_Slots WHERE ID={p_id}'
        self.mycursor.execute(sql1)
        sum = self.mycursor.fetchall()

        sql2 = f'Select * From Months WHERE Parking_ID={p_id}'
        self.mycursor.execute(sql2)
        mnths = self.mycursor.fetchall()

        sql2 = f'Select * From Timezone WHERE Parking_ID={p_id}'
        self.mycursor.execute(sql2)
        tmzn = self.mycursor.fetchall()

        sql3 = f'Select Type From Types WHERE Parking_ID={p_id}'
        self.mycursor.execute(sql3)
        tps = self.mycursor.fetchall()


        # print (tps[0][0])

        #
        # details = {
        #
        #     'months': {
        #         'January': str((mnths[0][2])/sum[0][0]*100)[:5] + "%",
        #         'February': str((mnths[0][3]/sum[0][0])*100)[:5] + "%",
        #         'March': str((mnths[0][4]/sum[0][0])*100)[:5] + "%",
        #         'April': str((mnths[0][5]/sum[0][0])*100)[:5] + "%",
        #         'May': str((mnths[0][6]/sum[0][0])*100)[:5] + "%",
        #         'June': str((mnths[0][7]/sum[0][0])*100)[:5] + "%",
        #         'July': str((mnths[0][8]/sum[0][0])*100)[:5] + "%",
        #         'August': str((mnths[0][9]/sum[0][0])*100)[:5] + "%",
        #         'September': str((mnths[0][10]/sum[0][0])*100)[:5] + "%",
        #         'October': str((mnths[0][11]/sum[0][0])*100)[:5] + "%",
        #         'November': str((mnths[0][12]/sum[0][0])*100)[:5] + "%",
        #         'December': str((mnths[0][13]/sum[0][0])*100)[:5] + "%"},
        #
        #     'timezone': {
        #         'Morning': str((tmzn[0][2])/sum[0][0]*100)[:5] + "%",
        #         'Noon': str((tmzn[0][3]/sum[0][0])*100)[:5] + "%",
        #         'Afternoon': str((tmzn[0][4]/sum[0][0])*100)[:5] + "%",
        #         'Night': str((tmzn[0][5]/sum[0][0])*100)[:5] + "%"},
        #
        #     'types': {
        #
        #     }
        # }
        #
        # print (details)
