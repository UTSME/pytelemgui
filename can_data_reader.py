import numpy as np

import time

from time import sleep
import pymongo

debugMode = True
counter = 0
id_name= "blank"
from bson.json_util import dumps

def initialize():
    client = pymongo.MongoClient("mongodb://localhost:27020/")
    # config = {'_id': 'utsme', 'members': [{'_id': 0, 'host': 'localhost:27020'}]}
    database = client["UTSM19-" + time.strftime("%Y-%m-%d")]

    return (database)

def readfromDB(database):
    change_stream = database.changestream.collection.watch()
    for change in change_stream:
        print (dumps(change))
        print('')
    

def main():
   database = initialize()
   global counter
   while True:
       readfromDB(database)

# PYTHON MAIN CALL
if __name__ == "__main__":
    main()
