from selenium_config import *
from log_config import logging
import json
import re
from operator import itemgetter
import time

TEMPERATURES_BY_STATE_URL = "https://worldpopulationreview.com/state-rankings/average-temperatures-by-state"
TV_TIME_BY_STATE_URL = "https://www.verizonspecials.com/resources/tv-viewership-by-state/"
UNINSURANCE_RATES_URL = "https://www.kff.org/other/state-indicator/total-population/"
DEPRESSION_RATES_URL = "https://worldpopulationreview.com/state-rankings/most-depressed-states"

def get_temperatures_by_state(temperatures_by_state_url):
    driver.get(temperatures_by_state_url)
    list1 = []
    for i in range(1, 50):
        d = {}
        d["state"] = get_element_text("/html/body/div[1]/div/div[3]/section[3]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr[{}]/td[1]/a".format(i))
        d["temperature"] = get_element_text("/html/body/div[1]/div/div[3]/section[3]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr[{}]/td[2]".format(i))
        list1.append(d)
    list1.sort(key = itemgetter("temperature"), reverse = True)
    print(list1)
    write_to_json("temperatures_us", list1)

def write_to_json(file_name, data):
    with open("./json/{}.json".format(file_name), "w") as file:
        json.dump(data, file, indent=4)

def get_tv_time_by_state(tv_time_by_state_url):
    driver.get(tv_time_by_state_url)
    list1 = []
    select_option_by_value("/html/body/div[1]/div[2]/main/article/div/div[2]/div[1]/label/select", "100")
    for i in range(1, 51):
        d = {}
        d["state"] = get_element_text("/html/body/div[1]/div[2]/main/article/div/div[2]/table/tbody/tr[{}]/td[2]".format(i))
        d["tv_time"] = get_element_text("/html/body/div[1]/div[2]/main/article/div/div[2]/table/tbody/tr[{}]/td[3]".format(i))
        list1.append(d)
    list1.sort(key = itemgetter("tv_time"), reverse = True)
    write_to_json("tv_times_us", list1)

def get_uninsurance_rates(uninsurance_rates_url):
    driver.get(uninsurance_rates_url)
    list1 = []
    time.sleep(3)
    for i in range(2, 52):
        d = {}
        d["state"] = get_element_text("/html/body/div[2]/div/div[1]/div[2]/div/datacenter-wrapper/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div[4]/div[1]/div/div[{}]/div/span".format(i))
        d["uninsurance_rate"] = get_element_text("/html/body/div[2]/div/div[1]/div[2]/div/datacenter-wrapper/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div[4]/div[3]/div/div[1]/div[{}]/div[6]/span".format(i))
        list1.append(d)
    list1.sort(key = itemgetter("uninsurance_rate"), reverse = True)
    write_to_json("uninsurance_rates_us", list1)

def get_depression_rates(depression_rates_url):
    driver.get(depression_rates_url)
    list1 = []
    for i in range(1, 51):
        d = {}
        d["state"] = get_element_text("/html/body/div[1]/div/div[3]/section[2]/div[1]/div/div[1]/div[1]/div[2]/table/tbody/tr[{}]/td[1]".format(i))
        d["depression_rate"] = int(get_element_text("/html/body/div[1]/div/div[3]/section[2]/div[1]/div/div[1]/div[1]/div[2]/table/tbody/tr[{}]/td[3]".format(i)))
        list1.append(d)
    write_to_json("depression_rates_us", list1)

#get_temperatures_by_state(TEMPERATURES_BY_STATE_URL)
#get_tv_time_by_state(TV_TIME_BY_STATE_URL)
#get_uninsurance_rates(UNINSURANCE_RATES_URL)
#get_depression_rates(DEPRESSION_RATES_URL)








