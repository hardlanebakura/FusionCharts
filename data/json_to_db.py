import json
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared

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
    print(table)
    #cursor.execute("DROP TABLE {}".format(table))
    #cursor.execute("DELETE FROM {}".format(table))
    db.commit()
    for item in data:
        list1 = [(v) for k, v in item.items()]
        prep_statem = "INSERT INTO {} (company, rating) VALUES (?, ?)".format(table)
        cursor_prep.execute(prep_statem, (list1[0], list1[1]))
    db.commit()

#json_to_db("fragile_states_indexes")
#json_to_db("factionalized_elites_indexes")
#json_to_db("group_grievances_indexes")
#json_to_db("military_spendings_indexes")
#json_to_db("military_spendings_perc_indexes")
#json_to_db("inflation_indexes")
#json_to_db("forest_areas_perc_indexes")
#json_to_db("oil_reserves_indexes")
#json_companies_to_db("companies_with_highest_rating_indexes", "companies_ratings_indexes")