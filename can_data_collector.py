import numpy as np

import time

import can
from time import sleep
import serial
import json
import pymongo
import random
import time

debugMode = True
counter = 0
id_name= "blank"

def initialize():
    if debugMode is False:
        can1 = can.interface.Bus(bustype='kvaser', channel=0, bitrate=1000000)
    else:
        can1 = "NULL"

    client = pymongo.MongoClient("mongodb://localhost:27020/")
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
        if counter % 2 == 0:
            msg = generateMsg(0x400)
        else:
            msg = generateMsg(0x210)
    elif can is not "NULL":
        msg = can.recv(1)
        print("Getting CAN")
    return msg


def intepretID(id):
    if (id == 0x3B):
        id_name = 'BMSMAIN'
    elif (id == 0x3CB):
        id_name = 'BMSDCL'
    elif (id == 0x6B2):
        id_name = 'BMSCUSTOM'
    elif (id == 0x36):
        id_name = 'BMSCELL'
    elif (id == 0x80):
        id_name = 'THERMISTER'
    elif (id == 0x81):
        id_name = 'THERMISTERTEMP'
    elif (id == 0x82):
        id_name = 'THERMISTERMAIN'
    elif (id == 0x74F):
        id_name = 'THERMISTERUTILTIY'
    elif (id == 0x500):
        id_name = 'PDM15STANDARD'
    elif (id == 0x520):
        id_name = 'PDM15FAULTS'
    elif (id == 0x521):
        id_name = 'PDM15TRIGGER'
    elif (id == 0x522):
        id_name = 'PDM15RESET'
    elif (id == 0x250):
        id_name = 'BSPSFLAGS'
    elif (id == 0x245):
        id_name = 'BSPSBRAKEPRESSURES'
    elif (id == 0x190):
        id_name = 'UNITEK'
    elif (id == 0x210):
        id_name = 'UNITEKTHROTTLE'
    elif (id == 0x670):
        id_name = 'DASH'
    elif (id == 0x400):
        id_name = 'M150'
    else:
        id_name = 'BMSCELL'

    return id_name

def writetoDB(collection, data, database):
    check = database.changestream.collection.insert_one(data)
    return check.acknowledged

def addtoDB(msg, id_name, id_num, database):
    check = False
    if id_name is "UNITEKTHROTTLE":
        collection = database["Throttle"]
        data = {"Throttle Low": msg.data[1], "Throttle High": msg.data[2], "Timestamp": msg.timestamp}
    
    elif id_name is "M150":
        collection = database["Regen Flag"]
        regen = msg.data[0]
        data = {"Regen Flag" : regen, "Timestamp": msg.timestamp}
        check = writetoDB(collection, data, database)
        
        collection = database["BMS High Temp"]
        BMSHigh = msg.data[1]
        data = {"BMS High Temp" : BMSHigh, "Timestamp": msg.timestamp}
        check = writetoDB(collection, data, database)
        
        collection = database["Speed"]
        speed = msg.data[2] + msg.data[3]
        data = {"Speed": speed, "Timestamp": msg.timestamp}
        check = writetoDB(collection, data, database)      
        
    elif id_name is "DASH":
        collection = database["Start Button"]
        btn = msg.data[0]
        data = {"Start Button": btn, "Timestamp": msg.timestamp}
        check = writetoDB(collection, data, database)
    
    elif id_name is "BSPSBRAKEPRESSURES":
        collection = database["Brake Pressure"]
        Pressure = msg.data[0] + msg.data[1]
        data = {"Brake Pressure": Pressure, "Timestamp": msg.timestamp}
        check = writetoDB(collection, data, database)
    
    elif id_name is "BSPSFLAGS":
        collection = database["Relay Latch"]
        relay = msg.data[0]
        data = {"Relay Latch": relay, "Timestamp": msg.timestamp}
        check = writetoDB(collection, data, database)
        
        collection = database["Sensor Failure"]
        sensor = msg.data[1]
        data = {"Senor Failure": sensor, "Timestamp": msg.timestamp}
        check = writetoDB(collection, data, database)
        
        collection = database["Throttle Brake Check"]
        brakecheck = msg.data[2]
        data = {"Throttle Brake Check": brakecheck, "Timestamp": msg.timestamp}
        check = writetoDB(collection, data, database)
        
        collection = database["Implausibility"]
        Implausibility = msg.data[3]
        data = {"Throttle Implausibility": Implausibility, "Timestamp": msg.timestamp}
        check = writetoDB(collection, data, database)
    
    elif id_name is "PDM15RESET":
        collection = database["PDM RESET"]
        reset = msg.data[0]
        data = {"PDM Reset": reset, "Timestamp": msg.timestamp}
        check = writetoDB(collection, data, database)
           
    
    return check

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
   global counter
   while True:
       msg = getData(can)
       print(msg)
       id = msg.arbitration_id
       id_name = intepretID(id)
       check = addtoDB(msg, id_name, id, database)
       addtoDBRaw(msg, id_name, id, database)

       print("The message is: ")
       print(msg)
       print("The ID is: " + str(id))
       print("The ID Name: " + str(id_name))
       print("The Database Insert Okay?: " + str(check))

       counter = counter + 1


       time.sleep(0.1)


# PYTHON MAIN CALL
if __name__ == "__main__":
    main()
