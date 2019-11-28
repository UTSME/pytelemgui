

class can_msg_types:

    def __init__(self, database, debug=False):
        self.debug = debug
        self.CAN_BUS_IDS = {"0x03a": "OrionBMS_Set1", 
               "0x03b": "OrionBMS_Set2",
               '0x03c": "OrionBMS_Set3",
               "0x03d": "OrionBMS_Set4",
               "0x03e": "OrionBMS_Set5",
               "0x500": "PDM15_STD",
               "0x520": "PDM15_MSG0",
               "0x521": "PDM15_MSG1",
               "0x522": "PDM15_MSG2",
               "0x250": "BSPD_FAULT",
               "0x650": "BSPD_START",
               "0x210": "BSPD_THROTTLE",
               "0x245": "BSPD_BRAKE",
               "0x190": "UNITEK",
               "0x400": "M150_REGEN",}

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
        #print(id_name)
        if id_name is "OrionBMS_Set1":
            #print("The ID IS " + id_name)

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
            #print("The ID IS " + id_name)
            temp = msg.data[0]
            byte_0 = msg.data[1]
            byte_1 = msg.data[2]
            byte_2 = msg.data[3]
            byte_3 = msg.data[4]
            self.data = {"High_temperature" : temp, 
            "High_temp_id" : byte_0, 
            "Low_temperature" : byte_1, 
            "Low_temp_id" : byte_2, 
            "checksum" : byte_3,  
            "Timestamp": msg.timestamp}

        elif id_name is "OrionBMS_Set3":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            byte_2 = msg.data[2]
            byte_3 = msg.data[3]
            byte_4 = msg.data[4]
            byte_5 = msg.data[5]
            byte_6 = msg.data[6]
            self.data = {"High_cell_voltage_byte_0" : byte_0, 
            "High_cell_voltage_byte_1" : byte_1, 
            "High_cell_volt_id" : byte_2, 
            "Low_cell_voltage_byte_0" : byte_3, 
            "Low_cell_voltage_byte_1" : byte_4, 
            "Low_cell_volt_id" : byte_5, 
            "checksum" : byte_6,  
            "Timestamp": msg.timestamp}

        elif id_name is "OrionBMS_Set4":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            byte_2 = msg.data[2]
            byte_3 = msg.data[3]
            byte_4 = msg.data[4]
            byte_5 = msg.data[5]
            byte_6 = msg.data[6]
            self.data = {"Pack_inst_voltage_byte_0" : byte_0, 
            "Pack_inst_voltage_byte_1" : byte_1, 
            "Pack_current_byte_0" : byte_2, 
            "Pack_current_byte_1" : byte_3, 
            "Pack_summed_volt_byte_0" : byte_4, 
            "Pack_summed_volt_byte_1" : byte_5, 
            "checksum" : byte_6, 
            "Timestamp": msg.timestamp}

        elif id_name is "OrionBMS_Set5":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            byte_2 = msg.data[2]
            byte_3 = msg.data[3]
            byte_4 = msg.data[4]
            byte_5 = msg.data[5]
            byte_6 = msg.data[6]
            self.data = {"Avg_cell_resistance_byte_0" : byte_0, 
            "Avg_cell_resistance_byte_1" : byte_1, 
            "Pack_ccl_byte_0" : byte_2, 
            "Pack_ccl_byte_1" : byte_3,
            "Pack_dcl_byte_0" : byte_4, 
            "Pack_dcl_byte_1" : byte_5, 
            "checksum" : byte_6, 
            "Timestamp": msg.timestamp}

        elif id_name is "PDM15_STD":
            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"PDM_STD" : byte, "Timestamp": msg.timestamp}    
    
        elif id_name is "PDM15_MSG0":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            byte_2 = msg.data[2]
            byte_3 = msg.data[3]
            byte_4 = msg.data[4]
            byte_5 = msg.data[5]
            byte_6 = msg.data[6]
            byte_7 = msg.data[7]
            self.data = {"F_fault_hvs_bms" : byte_0,
            "F_fault_hvs_pdoc" : byte_1, 
            "F_fault_hvs_imd" : byte_2,
            "F_fault_imd_imd" : byte_3,
            "F_hv_precharge" : byte_4,
            "F_hv_precharged" : byte_5,
            "F_ready_to_drive" : byte_6,
            "F_drive_enable" : byte_7, 
            "Timestamp": msg.timestamp}

        elif id_name is "PDM15_MSG1":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            byte_2 = msg.data[2]
            byte_3 = msg.data[3]
            byte_4 = msg.data[4]
            self.data = {"F_brake_trigger" : byte_0,
            "F_bcm_control_on" : byte_1,
            "F_bcm_control" : byte_2,  
            "F_shutdown_lock" : byte_3,
            "F_standby" : byte_4,
             "Timestamp": msg.timestamp}  
        
        elif id_name is "PDM15_MSG2":
            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"F_reset" : byte, "Timestamp": msg.timestamp} 

        elif id_name is "BSPD_FAULT":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            byte_2 = msg.data[2]
            byte_3 = msg.data[3]
            byte_4 = msg.data[4]
            self.data = {"F_bspd_current_brake_fault" : byte_0, 
            "sensor_failure" : byte_1,
            "throttle_brake_check" : byte_2,
            "throttle_implausbility" : byte_3,
            "torque_multi" : byte_4, 
            "Timestamp": msg.timestamp} 

        elif id_name is "BSPD_START":
            self.collection = self.database[id_name]
            byte = msg.data[0]
            self.data = {"start_btn_state" : byte, "Timestamp": msg.timestamp} 

        elif id_name is "BSPD_THROTTLE":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            byte_2 = msg.data[2]
            self.data = {"bspd_throttle_byte_1" : byte_0,
            "Throttle_byte_0" : byte_1, 
            "Throttle_byte_1": byte_2, 
            "Timestamp": msg.timestamp} 

        elif id_name is "BSPD_BRAKE":
            self.collection = self.database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            byte_2 = msg.data[2]
            byte_3 = msg.data[3]
            byte_4 = msg.data[4]
            byte_5 = msg.data[5]
            self.data = {"brake_avg_byte_0" : byte_0, 
            "brake_avg_byte_1": byte_1, 
            "brake_rear_byte_0" : byte_2, 
            "brake_rear_byte_1": byte_3,
            "brake_front_byte_0" : byte_4, 
            "brake_front_byte_1": byte_5,
            "Timestamp": msg.timestamp} 

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








            

