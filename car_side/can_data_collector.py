import numpy as np

import time

import can
from time import sleep
import serial
import json
import pymongo
import random
import time

from can_message_type import can_msg_types

debugMode = True
counter = 0
id_name= "blank"


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
    if debugMode is False:
        can1 = can.interface.Bus(bustype='kvaser', channel=0, bitrate=1000000)
    else:
        can1 = "NULL"

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    config = {'_id': 'utsme', 'members': [{'_id': 0, 'host': 'localhost:27020'}]}
    #rcv = client.admin.command("replSetInitiate", config)
    #print(rcv) 
    database = client["UTSM19-" + time.strftime("%Y-%m-%d")]

    return (can1, database)

def generateMsg(id):
    data = [random.randrange(0, 2 ** 8 - 1) for b in range(8)]
    timestamp = int(round(time.time() * 1000))
    msg = can.Message(arbitration_id=id, data=data, extended_id=False, timestamp=timestamp)
    return msg

def getData(can):
    if debugMode is True:
        rand_id = random.choice(list(CAN_BUS_IDS.keys()))
        print(hex(rand_id))
        #hex_int = int(rand_id, 16)
        #print(hex_int)
        msg = generateMsg(rand_id)
    elif can is not "NULL":
        msg = can.recv(1)
        print("Getting CAN")
    return msg


def writetoDB(collection, data, database):
    print(collection)
    check = database.changestream.collection.insert_one(data)
    return check.acknowledged

def addtoDBRaw(msg, id_name, id_num, database):
    i = 0
    data = dict()
    collection = database["RAW CAN"]
    for item in msg.data:
        data['Byte' + str(i)] = item
        i+=1

    check = collection.insert_one(data)
    return check

def main():
   (can, database) = initialize()
   can_msg_typing = can_msg_types(database=database)
   global counter
   while True:
       msg = getData(can)
       id = msg.arbitration_id
       id_name = can_msg_typing.intepretID(id)
       (collection, data) = can_msg_typing.make_db_data(id_name, msg)

       print("The message is: ")
       print(msg)
       print("The ID is: " + str(id))
       print("The ID Name: " + str(id_name))

       check = writetoDB(collection, data, database)
       print("The Database Insert Okay?: " + str(check))
       # check = addtoDBRaw(msg, id_name, id, database)

       
       
       counter = counter + 1

       time.sleep(0.1)


# PYTHON MAIN CALL
if __name__ == "__main__":
    main()
