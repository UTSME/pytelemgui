import numpy as np

import time

from time import sleep
import pymongo

debugMode = True
counter = 0
id_name= "blank"
from bson.json_util import dumps

CAN_BUS_IDS = {0x03A: "OrionBMS_Set1", 
               0x03B: "OrionBMS_Set2",
               0x03C: "OrionBMS_Set3",
               0x03D: "OrionBMS_Set4",
               0x03E: "OrionBMS_Set5",
               0x500: "PDM15_STD",
               0x520: "PDM15_MSG0",
               0x521: "PDM15_MSG1",
               0x522: "PDM15_MSG2",
               0x250: "BSPD_FAULT",
               0x650: "BSPD_START",
               0x210: "BSPD_THROTTLE",
               0x245: "BSPD_BRAKE",
               0x190: "UNITEK",
               0x400: "M150_REGEN",}

def initialize():
    client = pymongo.MongoClient("mongodb://localhost:27020/")
    # config = {'_id': 'utsme', 'members': [{'_id': 0, 'host': 'localhost:27020'}]}
    database = client["UTSM19-" + time.strftime("%Y-%m-%d")]

    return (database)

def readfromDB(database):
    change_stream = database.watch()
    for change in change_stream:
        #print(change)
        print("from collection: " + change["ns"]["coll"])
        data = change["fullDocument"]
        del data["_id"]
        print(data)
        #print(change["fullDocument"])

def main():
   database = initialize()
   global counter
   while True:
       readfromDB(database)

# PYTHON MAIN CALL
if __name__ == "__main__":
    main()
