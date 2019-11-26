import numpy as np

import time

from time import sleep
import pymongo

debugMode = True
counter = 0
id_name= "blank"
from bson.json_util import dumps
from can_message_type import can_msg_types

def initialize():
    client = pymongo.MongoClient("mongodb://localhost:27020/")
    # config = {'_id': 'utsme', 'members': [{'_id': 0, 'host': 'localhost:27020'}]}
    database = client["UTSM19-" + time.strftime("%Y-%m-%d")]

    return (database)

def readfromDB(database, can_interpret):
    change_stream = database.watch()
    print("This shoulld continue forever")
    print(change_stream)
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



