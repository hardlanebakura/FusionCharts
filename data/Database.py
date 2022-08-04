import json
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared

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

    def merge_tables(self):
        self.cursor.execute("SELECT * FROM fragile_states_indexes")
        file = open("./json/all_continents.json", "r")
        data = json.loads(file.read())
        countries = [item[1] for item in self.cursor.fetchall()]
        print(countries)
        print(data[0].items())
        self.cursor.execute("SELECT a.Country, a.`index` AS A, b.`index` AS B, c.`index` AS C, d.`index` FROM fragile_states_indexes as a INNER JOIN factionalized_elites_indexes as b ON a.Country = b.Country INNER JOIN group_grievances_indexes as c ON a.Country = c.Country INNER JOIN military_spendings_indexes as d ON a.Country = d.Country ORDER BY (A + B + C) DESC")
        rankings = self.cursor.fetchall()
        for item in rankings:
            rankings[rankings.index(item)] = list(item)
            rankings[rankings.index(list(item))][-1] = [country_data["continent"] for country_data in data if country_data["country"] == rankings[rankings.index(list(item))][0]][0]
        print([item for item in rankings])
        return self.cursor.fetchall()

    def __del__(self):
        self.con.close()

db = Database()
d = db.merge_tables()
#for row in d:
    #print(row)