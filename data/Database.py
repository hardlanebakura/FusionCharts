import json
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared

config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "fusioncharts"
}

class Database(object):

    def connect(self):
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "fusioncharts"
        )   

    def __init__(self):   

        self.con = self.connect()
        self.cursor = self.con.cursor()
        self.cursor_prep = self.con.cursor(cursor_class = MySQLCursorPrepared)    

    def select_all(self, table_name):
        self.cursor.execute("SELECT * FROM {}".format(table_name))
        return self.cursor.fetchall()

    def __del__(self):
        self.con.close()

db = Database()
d = db.select_all("fragile_states_indexes")
for row in d:
    print(row)