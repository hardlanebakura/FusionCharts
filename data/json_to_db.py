import json
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
import os
from operator import itemgetter

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "fusioncharts"
)

cursor = db.cursor()
cursor_prep = db.cursor(cursor_class = MySQLCursorPrepared)

""" cursor.execute("CREATE TABLE fragile_states_indexes (rank INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(89), `index` FLOAT(6, 2))")
cursor.execute("CREATE TABLE factionalized_elites_indexes (rank INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(89), `index` FLOAT(6, 2))")
cursor.execute("CREATE TABLE group_grievances_indexes (rank INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(89), `index` FLOAT(3, 2))")
cursor.execute("CREATE TABLE military_spendings_indexes (rank INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(89), `index` FLOAT(7, 2))") """
""" cursor.execute("CREATE TABLE military_spendings_perc_indexes (rank INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(89), `index` FLOAT(4, 2))")
cursor.execute("CREATE TABLE inflation_indexes (rank INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(89), `index` FLOAT(7, 2))")
cursor.execute("CREATE TABLE forest_areas_perc_indexes (rank INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(89), `index` FLOAT(7, 2))")
cursor.execute("CREATE TABLE oil_reserves_indexes (rank INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(89), `index` FLOAT(5, 2))") """
#cursor.execute("CREATE TABLE companies_ratings_indexes (rank INT AUTO_INCREMENT PRIMARY KEY, company VARCHAR(89), rating VARCHAR(4))")

def json_to_db(file_name, *argv):
    file = open("./json/{}.json".format(file_name))
    data = json.load(file)
    table = file_name if len(argv) == 0 else argv[0]
    print(table)
    #cursor.execute("DROP TABLE {}".format(table))
    #cursor.execute("DELETE FROM {}".format(table))
    db.commit()
    for item in data:
        list1 = [(v) for k, v in item.items()]
        prep_statem = "INSERT INTO {} (country, `index`) VALUES (?, ?)".format(table)
        cursor_prep.execute(prep_statem, (list1[0], list1[1]))
    db.commit()

def json_companies_to_db(file_name, *argv):
    file = open("./json/{}.json".format(file_name))
    data = json.load(file)
    table = file_name if len(argv) == 0 else argv[0]
    #cursor.execute("DROP TABLE {}".format(table))
    #cursor.execute("DELETE FROM {}".format(table))
    db.commit()
    for item in data:
        list1 = [(v) for k, v in item.items()]
        prep_statem = "INSERT INTO {} (company, rating) VALUES (?, ?)".format(table)
        cursor_prep.execute(prep_statem, (list1[0], list1[1]))
    db.commit()

def json_states(file_name, *argv):
    file = open("./json/{}".format(file_name))
    data = json.load(file)
    table = file_name if len(argv) == 0 else argv[0]
    d = {}
    for item in data:
        d[list(item.values())[0]] = list(item.values())[1]
    cursor.execute("CREATE TABLE if not exists states_us (rank INT AUTO_INCREMENT PRIMARY KEY, state VARCHAR(40), depression_rate TINYINT, temperature FLOAT(3, 1), tv_time FLOAT(3, 2), uninsurance_rate VARCHAR(5))")
    return d

def json_states_to_db(d):
    states = list(d[list(d)[0]].keys())
    dict1 = {}
    for state in states:
        dict1[state] = {}
        for column in d:
            c = column.split("us_")[1][:-1]
            dict1[state][c] = d[column][state]
            dict1[state]["state"] = state
    list1 = sorted(list(dict1.values()), key = itemgetter("state"))
    #cursor.execute("DROP TABLE states_us")
    #cursor.execute(cursor.execute("CREATE TABLE if not exists states_us (rank INT AUTO_INCREMENT PRIMARY KEY, state VARCHAR(40), depression_rate TINYINT, temperature FLOAT(3, 1), tv_time FLOAT(3, 2), uninsurance_rate VARCHAR(5))"))
    for item in list1:
        print(item)
        prep_statem = "INSERT INTO states_us (state, depression_rate, temperature, tv_time, uninsurance_rate) VALUES (?, ?, ?, ?, ?)"
        cursor_prep.execute(prep_statem, (item["state"], item["depression_rate"], item["temperature"], item["tv_time"], item["uninsurance_rate"]))
        db.commit()
    return states

#json_to_db("fragile_states_indexes")
#json_to_db("factionalized_elites_indexes")
#json_to_db("group_grievances_indexes")
#json_to_db("military_spendings_indexes")
#json_to_db("military_spendings_perc_indexes")
#json_to_db("inflation_indexes")
#json_to_db("forest_areas_perc_indexes")
#json_to_db("oil_reserves_indexes")
#json_companies_to_db("companies_with_highest_rating_indexes", "companies_ratings_indexes")


files_us = [item for item in os.listdir("json") if item[-8:] == "_us.json"]
print(files_us)
d = {}
for item in files_us: 
    d["us_" + item[:-8]] = json_states(item)
#d = json_states_to_db(d)

data = json.load(open("json/us_states_acronyms.json"))
d = dict([(value, key) for key, value in data.items()])
print(d)




