

class can_msg_types:

    def __init__(self, database, debug=False):
        self.debug = debug
        self.CAN_BUS_IDS = {0x03A: "OrionBMS_Set1", 
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

        self.database = database
        self.collection = database["blank"]
        self.data = {}

    def intepretID(self, id):
        if id in self.CAN_BUS_IDS:
            id_name = self.CAN_BUS_IDS[id]
        else:
            id_name = "NULL"

        return id_name

        
    def make_db_data(self, id_name, msg):
        check = False
        print(id_name)
        if id_name is "OrionBMS_Set1":
            print("The ID IS " + id_name)

            self.collection = self.database[id_name]
            counter = msg.data[0]
            byte_0 = msg.data[1]
            byte_1 = msg.data[2]
            byte_2 = msg.data[3]
            byte_3 = msg.data[4]
            self.data = {"Rolling Counter" : counter, 
            "custom_flag_1" : byte_0, 
            "custom_flag_2" : byte_1, 
            "custom_flag_3" : byte_2, 
            "checksum" : byte_3, 
            "Timestamp": msg.timestamp}

        elif id_name is "OrionBMS_Set2":
            self.collection = self.database[id_name]
            print("The ID IS " + id_name)
            temp = msg.data[0]
            byte_0 = msg.data[1]
            byte_1 = msg.data[2]
            byte_2 = msg.data[3]
            byte_3 = msg.data[4]
            self.data = {"High_temperature" : temp, "High_temp_id" : byte_0, "Low_temperature" : byte_1, "Low_temp_id" : byte_2, "checksum" : byte_3,  "Timestamp": msg.timestamp}


        elif id_name is "OrionBMS_Set3":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            self.data = {"High_cell_voltage_byte_0" : byte_0, "High_cell_voltage_byte_1" : byte_1, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte = msg.data[2]
            self.data = {"High_cell_volt_id" : byte, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte_0 = msg.data[3]
            byte_1 = msg.data[4]
            self.data = {"Low_cell_voltage_byte_0" : byte_0, "Low_cell_voltage_byte_1" : byte_1, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte = msg.data[5]
            self.data = {"Low_cell_volt_id" : byte, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte = msg.data[6]
            self.data = {"checksum" : byte, "Timestamp": msg.timestamp}  

        elif id_name is "OrionBMS_Set4":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            self.data = {"Pack_inst_voltage_byte_0" : byte_0, "Pack_inst_voltage_byte_1" : byte_1, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte_0 = msg.data[2]
            byte_1 = msg.data[3]
            self.data = {"Pack_current_byte_0" : byte_0, "Pack_current_byte_1" : byte_1, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte_0 = msg.data[4]
            byte_1 = msg.data[5]
            self.data = {"Pack_summed_volt_byte_0" : byte_0, "Pack_summed_volt_byte_1" : byte_1, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte = msg.data[6]
            self.data = {"checksum" : byte, "Timestamp": msg.timestamp}  
        

        elif id_name is "OrionBMS_Set5":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            self.data = {"Avg_cell_resistance_byte_0" : byte_0, "Avg_cell_resistance_byte_0" : byte_1, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte_0 = msg.data[2]
            byte_1 = msg.data[3]
            self.data = {"Pack_ccl_byte_0" : byte_0, "Pack_ccl_byte_1" : byte_1, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte_0 = msg.data[4]
            byte_1 = msg.data[5]
            self.data = {"Pack_dcl_byte_0" : byte_0, "Pack_dcl_byte_0" : byte_1, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte = msg.data[6]
            self.data = {"checksum" : byte, "Timestamp": msg.timestamp}    

        elif id_name is "PDM15_STD":
            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"Byte" : byte, "Timestamp": msg.timestamp}    
    
        elif id_name is "PDM15_MSG0":
            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"F_fault_hvs_bms" : byte, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte = msg.data[1]
            self.data = {"F_fault_hvs_pdoc" : byte, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte = msg.data[2]
            self.data = {"F_fault_hvs_imd" : byte, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte = msg.data[3]
            self.data = {"F_fault_imd_imd" : byte, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte = msg.data[4]
            self.data = {"F_hv_precharge" : byte, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte = msg.data[5]
            self.data = {"F_hv_precharged" : byte, "Timestamp": msg.timestamp}  

            self.collection = self.database[id_name]
            byte = msg.data[6]
            self.data = {"F_ready_to_drive" : byte, "Timestamp": msg.timestamp}  

            self.collection = self.database[id_name]
            byte = msg.data[7]
            self.data = {"F_drive_enable" : byte, "Timestamp": msg.timestamp}  

        elif id_name is "PDM15_MSG1":
            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"F_brake_trigger" : byte, "Timestamp": msg.timestamp}  

            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"F_bcm_control_on" : byte, "Timestamp": msg.timestamp} 

            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"F_bcm_control" : byte, "Timestamp": msg.timestamp}  

            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"F_shutdown_lock" : byte, "Timestamp": msg.timestamp}

            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"F_standby" : byte, "Timestamp": msg.timestamp} 
        
        elif id_name is "PDM15_MSG2":
            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"F_reset" : byte, "Timestamp": msg.timestamp} 

        elif id_name is "BSPD_FAULT":
            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"F_bspd_current_brake_fault" : byte, "Timestamp": msg.timestamp} 

            self.collection = self.database[id_name]
            byte = msg.data[1]
            self.data = {"sensor_failure" : byte, "Timestamp": msg.timestamp} 

            self.collection = self.database[id_name]
            byte = msg.data[2]
            self.data = {"throttle_brake_check" : byte, "Timestamp": msg.timestamp} 

            self.collection = self.database[id_name]
            byte = msg.data[3]
            self.data = {"throttle_implausbility" : byte, "Timestamp": msg.timestamp} 

            self.collection = self.database[id_name]
            byte = msg.data[4]
            self.data = {"torque_multi" : byte, "Timestamp": msg.timestamp} 

        elif id_name is "BSPD_START":
            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"start_btn_state" : byte, "Timestamp": msg.timestamp} 

        elif id_name is "BSPD_THROTTLE":
            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"byte_1" : byte, "Timestamp": msg.timestamp} 

            self.collection = self.database[id_name]
            byte_0 = msg.data[1]
            byte_1 = msg.data[2]
            self.data = {"Throttle_byte_0" : byte_0, "Throttle_byte_1": byte_1, "Timestamp": msg.timestamp} 

        elif id_name is "BSPD_BRAKE":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            self.data = {"brake_avg_byte_0" : byte_0, "brake_avg_byte_1": byte_1, "Timestamp": msg.timestamp} 

            self.collection = self.database[id_name]
            byte_0 = msg.data[2]
            byte_1 = msg.data[3]
            self.data = {"brake_rear_byte_0" : byte_0, "brake_rear_byte_1": byte_1, "Timestamp": msg.timestamp} 

            self.collection = self.database[id_name]
            byte_0 = msg.data[4]
            byte_1 = msg.data[5]
            self.data = {"brake_front_byte_0" : byte_0, "brake_front_byte_1": byte_1, "Timestamp": msg.timestamp} 

        elif id_name is "UNITEK":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            byte_2 = msg.data[2]
            self.data = {"unitek_byte_0" : byte_0, "unitek_byte_1": byte_1, "unitek_byte_2": byte_2, "Timestamp": msg.timestamp} 

        elif id_name is "M150_REGEN":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            self.data = {"regen_flag" : byte_0, "Timestamp": msg.timestamp} 
        
        return (self.collection, self.data)








            

