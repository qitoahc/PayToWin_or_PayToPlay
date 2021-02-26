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

### in process of transfer and cleaning from jupyter notebook