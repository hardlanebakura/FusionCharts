from operator import itemgetter
from flask import Flask, render_template, render_template, url_for, jsonify
from flask_cors import CORS, cross_origin
from Database import *

db = Database()

app = Flask(__name__)

@app.route("/continents")
@cross_origin()
def continents():
    
    def get_data_for_charts(column):
        for item in db.select_all("continents"):
            print(item)
        print(COLUMNS[column]["id"])
        #all from continents where continent_id = item[-1] and COLUMNS[column]["id"] index
        print(db.get_query("SELECT * FROM continents WHERE continent_id = '{}'".format("NA")))
        return [{"continent": item[-1], "{}".format(column): db.get_query("SELECT * FROM continents WHERE continent_id = '{}'".format(item[-1]))[0][COLUMNS[column]["id"]]} for item in db.select_all("continents")]

    COLUMNS = { "fsi": { "id": 1, "alt": "fragile_states_indexes" }, "fei": { "id": 2, "alt": "factionalized_elites_indexes" }, "ggi": { "id": 3, "alt": "group_grievances_indexes" }, "msi": { "id": 4, "alt": "military_spendings_indexes" }, "mspi": { "id": 5, "alt": "military_spendings_perc_indexes" }, "fapi": { "id": 6, "alt": "forest_areas_perc_indexes" }, "ii": { "id": 7, "alt": "inflation_indexes" }, "ori": { "id": 8, "alt": "oil_reserves_indexes" } }
    d = {}
    for k, v in COLUMNS.items():
        d[k] = { "gradients": db.get_chart(v["alt"]), "values": get_data_for_charts(k) }
    continents_data = db.select_all("continents")
    print(continents_data)
    return d

@app.route("/countries")
@cross_origin()
def countries():

    def get_indexes(list1):
        list2 = []
        print(list1)
        for item in list1:
            list3 = []
            for item1 in item:
                if item.index(item1) != 0 and item.index(item1) != len(item) - 1:
                    list3.append(item1)
            list2.append(list3)
        return list2

    def get_zip_dict(list1):
        list2 = []
        for item in list1:
            list2.append(dict(zip([item[0] for item in COLS if COLS.index(item) != 0 and COLS.index(item) != (len(COLS) - 1)], item)))
        return list2

    def get_zip_dict_countries(list1):
        list2 = []
        for item in list1:
            list2.append(dict(zip([item for item in COUNTRY_COLS], item[1:])))
            #print(item)
        return list2

    #keep only columns that affect country's stability ranking
    def stability_rank_format(list1):
        UNAFFECTED = ["FAPI", "ORI", "MSI", "MSPI"]
        for item in list1: 
            for k in UNAFFECTED:
                del list1[list1.index(item)][k]
        return list1

    COLS = db.show("world_map")
    COUNTRY_COLS = ["country", "index"]
    print([item[0] for item in COLS if COLS.index(item) != 0 and COLS.index(item) != (len(COLS) - 1)])
    get_indexes(COLS)
    d = {}
    d["least_stable_countries"] = stability_rank_format(get_zip_dict(get_indexes(db.select_all("world_map")[:5])))
    d["most_stable_countries"] = stability_rank_format(get_zip_dict(get_indexes(db.select_all("world_map")[-5:])))
    d["oil_reserves"] = get_zip_dict_countries(db.select_all("oil_reserves_indexes")[:5])
    return d

@app.route("/companies")
@cross_origin()
def companies():
    return {"highest_rating_companies": [{"company": item[1], "value": item[2]} for item in db.select_all("companies_ratings_indexes")]}

@app.route("/states")
@cross_origin()
def states():
    COLS = [item[0] for item in db.show("states_us") if db.show("states_us").index(item) != 0]
    d = {}
    list1 = db.select_all("states_us")
    def format_perc(string):
        return d["value"].split
    for column in COLS:
        print(column)
        d[column] = []
        if COLS.index(column) != 0 and COLS.index(column) != 1:
            states = db.select("states_us", ["state", "state_id", column])
            for item in states:
                print(item)
                d[column].append({ "state":item[0], "state_id":item[1], "value":item[2]})
        dict1 = {}
    for column in d:
        dict1[column + "s"] = d[column]
    d = dict1

    return d

if (__name__ == "__main__"):
    app.run(debug=True)