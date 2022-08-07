from selenium_config import *
from log_config import logging
import json
import re
from operator import itemgetter

COMPANIEST_WITH_HIGHEST_RATING_URL = "https://www.businessinsider.com/payscale-best-companies-with-happiest-employees-in-america-2016-4"

def get_companies_with_highest_rating(companies_with_highest_rating_url):
    driver.get(companies_with_highest_rating_url)
    list1 = []
    for i in range(2, 27, 2):
        d = {}
        str = get_element_text("/html/body/section/section/section/section[3]/section/div/article/section[1]/div/section/div/div/div[{}]/div/div[1]/h2".format(i))
        d["company"] = str[(len(re.findall("[0-9.]+[.]", str)[0]) + 1):len(str)]
        d["satisfaction_percentage"] = re.findall("[0-9.]+[%]", get_element_text("/html/body/section/section/section/section[3]/section/div/article/section[1]/div/section/div/div/div[{}]/div/p[3]".format(i)))[0]
        list1.append(d)
        list1.sort(key = itemgetter("satisfaction_percentage".split("%")[0]), reverse = True)
    print(list1)
    write_to_json("companies_with_highest_rating_indexes", list1)

def write_to_json(file_name, data):
    with open("./json/{}.json".format(file_name), "w") as file:
        json.dump(data, file, indent=4)

get_companies_with_highest_rating(COMPANIEST_WITH_HIGHEST_RATING_URL)







