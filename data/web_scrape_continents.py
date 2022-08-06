from selenium_config import *
from log_config import logging
import json

URL = "https://www.theglobaleconomy.com/rankings/"
FSI_URL = "{}fragile_state_index/".format(URL)
FEI_URL = "{}factionalized_elites_index/".format(URL)
GROUP_GRI_URL = "{}group_grievance_index/".format(URL)
MIL_SPEND_URL = "{}mil_spend/".format(URL)
MIL_SPEND_PERC_URL = "{}mil_spend_gdp/".format(URL)
INFLA_URL = "{}inflation_annual/".format(URL)
FORES_PERC_URL = "{}forest_area/".format(URL)
OIL_RESERVES_URL = "{}oil_reserves/".format(URL)

def get_fsi(fsi_url):
    driver.get(fsi_url)

    list1 = []
    for i in range(1, 172):
        d = {}
        d["country_name"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[1]/a".format(i))
        d["country_fsi"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[2]".format(i))
        list1.append(d)
    write_to_json("fragile_states_indexes", list1)

def get_fei(fei_url):
    driver.get(fei_url)

    list1 = []
    for i in range(1, 172):
        d = {}
        d["country_name"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[1]/a".format(i))
        d["country_fei"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[2]".format(i))
        list1.append(d)
    write_to_json("factionalized_elites_indexes", list1)

def get_group_gri(group_gri_url):
    driver.get(group_gri_url)

    list1 = []
    for i in range(1, 172):
        d = {}
        d["country_name"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[1]/a".format(i))
        d["country_group_grievance"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[2]".format(i))
        list1.append(d)
    write_to_json("group_grievances_indexes", list1)

def get_military_spendings(military_spendings_url):
    driver.get(military_spendings_url)

    list1 = []
    for i in range(1, 140):
        d = {}
        d["country_name"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[1]/a".format(i))
        d["country_military_spending"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[2]".format(i))
        list1.append(d)
    write_to_json("military_spendings_indexes", list1)

def get_military_spendings_perc(military_spendings_perc_url):
    driver.get(military_spendings_perc_url)

    list1 = []
    for i in range(1, 140):
        d = {}
        d["country_name"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[1]/a".format(i))
        d["country_military_spending_perc"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[2]".format(i))
        list1.append(d)
    write_to_json("military_spendings_perc_indexes", list1)

def get_inflations(infl_url):
    driver.get(infl_url)

    list1 = []
    for i in range(1, 172):
        d = {}
        d["country_name"] = get_element_text("/html/body/div[3]/div/div[1]/div[5]/div[3]/table/tbody/tr[{}]/td[1]/a".format(i))
        d["inflation"] = get_element_text("/html/body/div[3]/div/div[1]/div[5]/div[3]/table/tbody/tr[{}]/td[2]".format(i))
        list1.append(d)
    write_to_json("inflation_indexes", list1)

def get_forest_areas_perc(forest_areas_url):
    driver.get(forest_areas_url)

    list1 = []
    for i in range(1, 172):
        d = {}
        d["country_name"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[1]/a".format(i))
        d["forest_areas_perc"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[2]".format(i))
        list1.append(d)
    write_to_json("forest_areas_perc_indexes", list1)

def get_oil_reserves(oil_reserves_url):
    driver.get(oil_reserves_url)

    list1 = []
    for i in range(1, 172):
        d = {}
        d["country_name"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[1]/a".format(i))
        d["oil_reserves"] = get_element_text("/html/body/div[3]/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[2]".format(i))
        list1.append(d)
    write_to_json("oil_reserves_indexes", list1)

def write_to_json(file_name, data):
    with open("./json/{}.json".format(file_name), "w") as file:
        json.dump(data, file, indent=4)

""" get_fsi(FSI_URL)
get_fei(FEI_URL)
get_group_gri(GROUP_GRI_URL)
get_military_spendings(MIL_SPEND_URL) """
#get_military_spendings_perc(MIL_SPEND_PERC_URL)
#get_inflations(INFLA_URL)
""" get_forest_areas_perc(FORES_PERC_URL)
get_oil_reserves(OIL_RESERVES_URL) """







