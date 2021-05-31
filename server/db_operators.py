import mysql.connector
import pandas as pd

class Db_Operators:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="okjimmyu",
            database="python_server"
        )

        self.mycursor = self.mydb.cursor()

    def show_db(self):
        my_data = pd.read_sql("SHOW databases;", self.mydb)
        print (my_data)
        return my_data

    def show_table(self):
        my_data = pd.read_sql("SHOW tables;", self.mydb)
        print (my_data)
        return my_data

    def show_parking_slots(self):
        self.mycursor.execute("Select ID, Street, Free, Area, Sum From Parking_Slots;")
        for x in self.mycursor.fetchall():
            print (x[0], x[1], x[2], x[3], x[4])

    def show_dates(self):
        my_data = pd.read_sql("Select * From Dates;", self.mydb)
        print (my_data)

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

        a = str((mnths[0][1]/sum[0][0])*100)[:5] + "%"
        print (a)

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
                'Night': str((tmzn[0][5]/sum[0][0])*100)[:5] + "%",
            }
        }

        print (details)
