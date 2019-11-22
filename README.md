# Telemetry19

UTSME19 Telemetry Subsystem using Python

## Dependencies
Python-can
Kvaser canlib
MongoDB (Replica Set)

## Startup
Make sure to initialize a replica set of the main MongoDB instances
The process is 

1. Startup a new MongoDB instances with replica sets enabled
--* sudo mongod --replSet rs0 --port 27020 --bind_ip_all --dbpath /srv/mongodb/rs0-0  --oplogSize 128

2. Login to the new instancse
--* mongo --port 27020 (Change the port numbers to reflect above)

3. In the mongo console, start the replica set
--* rs.initiate()

## Components

* [Vehicle Interface]
  * Kvaser Leaf Pro
  * Raspberry Pi 4 running Ubuntu 18.04
  * USB Wifi Adapter with high gain antenna
* [Database Interface]
  * Ubiquiti High Gain access point
  * Database reader script
* Database Server
  * MongoDB
