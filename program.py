# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 23:31:29 2017

@author: Madhu
"""

from datetime import datetime
import numpy as np
import json

with open('data.json') as data_file:    
    D = json.load(data_file)
    
    
def Ingest(e, D):
    eventFilterData = [x for x in D if datetime.date(datetime.strptime(x["event_time"].split(":")[0], "%Y-%m-%d")).isocalendar()[1] == e]
    return eventFilterData;
    
def TopXSimpleLTVCustomers(x, D):
    customers = [ud for ud in D if ud["type"] == "CUSTOMER"]
    sites = [ud for ud in D if ud["type"] == "SITE_VISIT"]
    orders = [ud for ud in D if ud["type"] == "ORDER"]
    images = [ud for ud in D if ud["type"] == "IMAGE"]
    custKeyList = []
    expenList = []

    for c in customers:
        custKeyList.append(c["key"])
        expenList.append(sum([float(cs["total_amount"].split(" ")[0]) for cs in orders if cs["customer_id"] == c["key"]]))
    expenList = np.array(expenList)
    
    TopXLTVIndex = expenList.argsort()[-1*x:][::-1]
    
    TopXLTV = [custKeyList[i] for i in TopXLTVIndex]
    
    return TopXLTV

UD = Ingest(1, D)
print(TopXSimpleLTVCustomers(2, UD))