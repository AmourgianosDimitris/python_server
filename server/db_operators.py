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

    def show_db(self):
        my_data = pd.read_sql("SHOW databases;", self.mydb)
        print (my_data)
        return my_data

    def show_table(self):
        my_data = pd.read_sql("SHOW tables;", self.mydb)
        print (my_data)
        return my_data

    def show_parking_slots(self):
        my_data = pd.read_sql("Select * From Parking_Slots;", self.mydb)
        print (my_data)

    def show_dates(self):
        my_data = pd.read_sql("Select * From Dates;", self.mydb)
        print (my_data)
