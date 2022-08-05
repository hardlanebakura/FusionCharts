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

    COLUMNS = { "fsi": { "id": 1, "alt": "fragile_states_indexes" }, "fei": { "id": 2, "alt": "factionalized_elites_indexes" }, "ggi": { "id": 3, "alt": "group_grievances_indexes" }, "msi": { "id": 4, "alt": "military_spendings_indexes" }}
    d = {}
    for k, v in COLUMNS.items():
        d[k] = { "gradients": db.get_chart(v["alt"]), "values": get_data_for_charts(k) }
    continents_data = db.select_all("continents")
    print(continents_data)
    return d

if (__name__ == "__main__"):
    app.run(debug=True)