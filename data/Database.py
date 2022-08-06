import json
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from log_config import logging

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
        self.cursor = self.con.cursor(buffered = True)
        self.cursor1 = self.con.cursor(buffered = True)
        self.cursor_prep = self.con.cursor(cursor_class = MySQLCursorPrepared)    

    def select_all(self, table_name):
        self.cursor.execute("SELECT * FROM {}".format(table_name))
        return self.cursor.fetchall()

    def insert_into(self, table_name, columns, values):
        if not isinstance(table_name, str):
            raise TypeError("Expected string input")
        if not isinstance(columns, list):
            raise TypeError("Expected list input")
        if not isinstance(values, list):
            raise TypeError("Expected list input")
        prep_statem = "INSERT INTO {} (country, `index`) VALUES (?, ?)".format(table_name)

    def merge_tables(self):
        self.cursor.execute("SELECT * FROM fragile_states_indexes")
        file = open("./json/all_continents.json", "r")
        data = json.loads(file.read())
        countries = [item[1] for item in self.cursor.fetchall()]
        self.cursor.execute("SELECT a.Country, a.`index` AS A, b.`index` AS B, c.`index` AS C, d.`index` AS D, e.`index` AS E, f.`index`, g.`index`, h.`index` FROM fragile_states_indexes as a INNER JOIN factionalized_elites_indexes as b ON a.Country = b.Country INNER JOIN group_grievances_indexes as c ON a.Country = c.Country INNER JOIN military_spendings_indexes as d ON a.Country = d.Country INNER JOIN military_spendings_perc_indexes as e ON a.Country = e.Country INNER JOIN forest_areas_perc_indexes as f ON a.Country = f.Country INNER JOIN inflation_indexes as g ON a.Country = g.Country INNER JOIN oil_reserves_indexes as h ON a.Country = h.Country ORDER BY (A + B + C) DESC")
        rankings = self.cursor.fetchall()
        #self.cursor.execute("DROP TABLE if exists world_map")
        #self.cursor.execute("CREATE TABLE world_map (rank int AUTO_INCREMENT PRIMARY KEY, country VARCHAR(89), FSI FLOAT(6, 2), FEI FLOAT(6, 2), GGI FLOAT(3, 2), MSI FLOAT(7, 2), MSPI FLOAT(4, 2), FAPI FLOAT(7, 2), II FLOAT(7, 2), ORI FLOAT(5,2), continent VARCHAR(19))")
        

        for item in rankings:
            i = rankings.index(item)
            rankings[i] = list(item)
            rankings[i].append([country_data["continent"] for country_data in data if country_data["country"] == rankings[rankings.index(list(item))][0]][0])
            #print(rankings[i])
        
            #prep_statem = "INSERT INTO world_map (country, FSI, FEI, GGI, MSI, MSPI, FAPI, II, ORI, continent) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            #self.cursor_prep.execute(prep_statem, (rankings[i][0], rankings[i][1], rankings[i][2], rankings[i][3], rankings[i][4], rankings[i][5], rankings[i][6], rankings[i][7], rankings[i][8], rankings[i][9]))
            #self.con.commit()

        d = {}
        COLS = ["FEI", "FSI", "GGI", "MSI"]
        CONTINENTS = ["North America", "South America", "Asia", "Europe", "Oceania", "Africa"]
        ALIASES = { "North America": "NA", "South America": "SA", "Asia": "AS", "Europe": "EU", "Oceania": "AU", "Africa": "AF" }
        for item in CONTINENTS: d[item] = {}
        self.cursor.execute("SELECT * FROM world_map")
        for row in self.cursor.fetchall():
            self.cursor1.execute("SELECT * FROM world_map WHERE continent = '{}'".format(row[-1]))
            rows = len(self.cursor1.fetchall())
            d[row[-1]]["fsi"] = round((d[row[-1]]["fsi"] + row[2] / rows if "fsi" in d[row[-1]] else row[2] / rows), 2)
            d[row[-1]]["fei"] = round((d[row[-1]]["fei"] + row[3] / rows if "fei" in d[row[-1]] else row[3] / rows), 2)
            d[row[-1]]["ggi"] = round((d[row[-1]]["ggi"] + row[4] / rows if "ggi" in d[row[-1]] else row[4] / rows), 2)
            d[row[-1]]["msi"] = round((d[row[-1]]["msi"] + row[5] / rows if "msi" in d[row[-1]] else row[5] / rows), 2)
            d[row[-1]]["mspi"] = round((d[row[-1]]["mspi"] + row[6] / rows if "mspi" in d[row[-1]] else row[6] / rows), 2)
            d[row[-1]]["fapi"] = round((d[row[-1]]["fapi"] + row[7] / rows if "fapi" in d[row[-1]] else row[7] / rows), 2)
            d[row[-1]]["ii"] = round((d[row[-1]]["ii"] + row[8] / rows if "ii" in d[row[-1]] else row[8] / rows), 2)
            d[row[-1]]["ori"] = round((d[row[-1]]["ori"] + row[9] / rows if "ori" in d[row[-1]] else row[9] / rows), 2)
        #self.cursor.execute("DROP TABLE if exists continents")
        #self.cursor.execute("CREATE TABLE continents (rank int AUTO_INCREMENT PRIMARY KEY, FSI FLOAT(6, 2), FEI FLOAT(6, 2), GGI FLOAT(3, 2), MSI FLOAT(7, 2), MSPI FLOAT(4, 2), FAPI FLOAT(7, 2), II FLOAT(7, 2), ORI FLOAT(5,2), continent VARCHAR(19), continent_id VARCHAR(4))")
        """     for item in list(d.values()):
        rep_statem = "INSERT INTO continents (FSI, FEI, GGI, MSI, MSPI, FAPI, II, ORI, continent, continent_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor_prep.execute(prep_statem, (item["fsi"], item["fei"], item["ggi"], item["msi"], item["mspi"], item["fapi"], item["ii"], item["ori"], list(d.keys())[list(d.values()).index(item)], ALIASES[list(d.keys())[list(d.values()).index(item)]]))
        self.con.commit() """
        logging.info(d)

        return rankings

    def get_chart(self, table_name):
        self.cursor.execute("SELECT * FROM {}".format(table_name))
        logging.info(self.cursor.fetchall())
        col = "".join([string[0] for string in table_name.split("_")])
        self.cursor.execute("SELECT {} FROM continents".format(col))
        results = self.cursor.fetchall()
        max_result = max(results)[0]
        min_result = min(results)[0]
        gradient_1 = round((min_result + (max_result - min_result) * 0.3333), 2)
        gradient_2 = round((min_result + (max_result - min_result) * 0.67), 2)
        d = { "min_result": min_result, "gradient_1": gradient_1, "gradient_2": gradient_2, "max_result": max_result }
        print(d)
        return d

    def get_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def show(self, table_name):
        self.cursor.execute("SHOW columns FROM {}".format(table_name))
        return self.cursor.fetchall()

db = Database()
d = db.merge_tables()
#for row in d:
    #logging.info(row)

#db.get_chart("fragile_states_indexes")