import json
from os import listdir
from os.path import isfile, join
import os
import sys
from io import StringIO

import pandas as pd
import numpy as np

import psycopg2 as psy
from psycopg2 import sql
import sqlalchemy
from sqlalchemy import create_engine

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path+"/src") 
from mtg_helpers import *

con_details = {"dbname" : 'pay_to_play', 
               "user" : os.environ['PGSQL_P_USER'], 
               "password" : os.environ['PGSQL_P_PWD'], 
               "host" : 'localhost'}  

data_path = '../data/MTGJSONcards/'
file_name = 'AllPrices.json'
file = open(data_path+file_name, 'r')
price_data = json.load(file)['data']

conn = connect(con_details)

card_format = 'paper'
price_source = 'cardkingdom'
price_list = 'retail'
card_type_order = ['normal','foil']

uuids_in_price = price_data.keys()
uuids_price_lookup = set(uuids_in_price).intersection(set(uuids_in_db['uuid']))
uuid_prices = []
uuid_fails =[]

for i in uuids_price_lookup:
    card_prices = get_prices(i, card_format, price_source, price_list, card_type_order,price_data)
    if card_prices is None:
        uuid_fails.append(i)
    else:
        date = min(card_prices.keys())
        price = card_prices[date]
        uuid_prices.append((i, price_source, price, date))

print('number of uuids with failed price searches:')
print(len(uuid_fails))

proceed = input ('Enter 1 to proceed to load to DB.  0 to end without loading.')

if proceed == 1
    prices_to_load = pd.DataFrame(uuid_prices, columns = ['uuid', 'price_source', 'price', 'price_date'])

    add_new_card_data(con_details, prices_to_load,'fixed_prices',conn)
elif:
    print('Process aborted, no price data was loaded.')