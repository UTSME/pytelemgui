import numpy as np

import time

from time import sleep
import pymongo

debugMode = True
counter = 0
id_name= "blank"
from bson.json_util import dumps
from can_message_type import can_msg_types

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

def readfromDB(database, can_interpret):
    change_stream = database.watch()
    for change in change_stream:
        #print(change)
        print("from collection: " + change["ns"]["coll"])
        id_name = change["ns"]["coll"]
        data = change["fullDocument"]
        del data["_id"]
        can_table = can_interpret.set_db_data(id_name, data)
        for id, data in can_table.items():
            print("The Current ID Name is: " + id)
            for key in data:
                print(key + " : " + str(data[key]))

def main():
   database = initialize()
   can_interpret = can_msg_types()
   global counter
   while True:
       readfromDB(database, can_interpret)

# PYTHON MAIN CALL
if __name__ == "__main__":
    main()
