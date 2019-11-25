

class can_msg_types:

    def __init__(self, debug=False):
        self.debug = debug
        self.CAN_BUS_IDS = {"0x03A": "OrionBMS_Set1", 
               "0x03B": "OrionBMS_Set2",
               "0x03C": "OrionBMS_Set3",
               "0x03D": "OrionBMS_Set4",
               "0x03E": "OrionBMS_Set5",
               "0x500": "PDM15_STD",
               "0x520": "PDM15_MSG0",
               "0x521": "PDM115_MSG1",
               "0x522": "PDM115_MSG2",
               "0x250": "BSPD_FAULT",
               "0x650": "BSPD_START",
               "0x210": "BSPD_THROTTLE",
               "0x245": "BSPD_BRAKE",
               "0x190": "UNITEK",
               "0x400": "M150_REGEN",}

    def intepretID(id):
        if hex(id) in self.CAN_BUS_IDS:
            id_name = self.CAN_BUS_IDS[hex(id)]
        else:
            id_name = "NULL"

        return id_name

        
    def make_db_data(id_name, msg):
        check = False
        if id_name is "OrionBMS_Set1":
            collection = database[id_name]
            counter = msg.data[0]
            data = {"Rolling Counter" : counter, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[1]
            data = {"custom_flag_1" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[2]
            data = {"custom_flag_2" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[3]
            data = {"custom_flag_2" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[4]
            data = {"checksum" : byte, "Timestamp": msg.timestamp}
        
        elif id_name is "OrionBMS_Set2":
            collection = database[id_name]
            temp = msg.data[0]
            data = {"High_temperature" : temp, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[1]
            data = {"High_temp_id" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[2]
            data = {"Low_temperature" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[3]
            data = {"Low_temp_id" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[4]
            data = {"checksum" : byte, "Timestamp": msg.timestamp}

        elif id_name is "OrionBMS_Set3":
            collection = database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            data = {"High_cell_voltage_byte_0" : byte_0, "High_cell_voltage_byte_1" : byte_1, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[2]
            data = {"High_cell_volt_id" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte_0 = msg.data[3]
            byte_1 = msg.data[4]
            data = {"Low_cell_voltage_byte_0" : byte_0, "Low_cell_voltage_byte_1" : byte_1, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[5]
            data = {"Low_cell_volt_id" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[6]
            data = {"checksum" : byte, "Timestamp": msg.timestamp}  

        elif id_name is "OrionBMS_Set4":
            collection = database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            data = {"Pack_inst_voltage_byte_0" : byte_0, "Pack_inst_voltage_byte_1" : byte_1, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte_0 = msg.data[2]
            byte_1 = msg.data[3]
            data = {"Pack_current_byte_0" : byte_0, "Pack_current_byte_1" : byte_1, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte_0 = msg.data[4]
            byte_1 = msg.data[5]
            data = {"Pack_summed_volt_byte_0" : byte_0, "Pack_summed_volt_byte_1" : byte_1, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[6]
            data = {"checksum" : byte, "Timestamp": msg.timestamp}  
        

        elif id_name is "OrionBMS_Set5":
            collection = database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            data = {"Avg_cell_resistance_byte_0" : byte_0, "Avg_cell_resistance_byte_0" : byte_1, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte_0 = msg.data[2]
            byte_1 = msg.data[3]
            data = {"Pack_ccl_byte_0" : byte_0, "Pack_ccl_byte_1" : byte_1, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte_0 = msg.data[4]
            byte_1 = msg.data[5]
            data = {"Pack_dcl_byte_0" : byte_0, "Pack_dcl_byte_0" : byte_1, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[6]
            data = {"checksum" : byte, "Timestamp": msg.timestamp}    

        elif id_name is "PDM15_STD":
            collection = database[id_name]
            byte = msg.data[0]
            data = {"Byte" : byte, "Timestamp": msg.timestamp}    
    
        elif id_name is "PDM15_MSG0":
            collection = database[id_name]
            byte = msg.data[0]
            data = {"F_fault_hvs_bms" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[1]
            data = {"F_fault_hvs_pdoc" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[2]
            data = {"F_fault_hvs_imd" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[3]
            data = {"F_fault_imd_imd" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[4]
            data = {"F_hv_precharge" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[5]
            data = {"F_hv_precharged" : byte, "Timestamp": msg.timestamp}  

            collection = database[id_name]
            byte = msg.data[6]
            data = {"F_ready_to_drive" : byte, "Timestamp": msg.timestamp}  

            collection = database[id_name]
            byte = msg.data[7]
            data = {"F_drive_enable" : byte, "Timestamp": msg.timestamp}  

        elif id_name is "PDM15_MSG1":
            collection = database[id_name]
            byte = msg.data[0]
            data = {"F_brake_trigger" : byte, "Timestamp": msg.timestamp}  

            collection = database[id_name]
            byte = msg.data[0]
            data = {"F_bcm_control_on" : byte, "Timestamp": msg.timestamp} 

            collection = database[id_name]
            byte = msg.data[0]
            data = {"F_bcm_control" : byte, "Timestamp": msg.timestamp}  

            collection = database[id_name]
            byte = msg.data[0]
            data = {"F_shutdown_lock" : byte, "Timestamp": msg.timestamp}

            collection = database[id_name]
            byte = msg.data[0]
            data = {"F_standby" : byte, "Timestamp": msg.timestamp} 
        
        elif id_name is "PDM15_MSG2":
            collection = database[id_name]
            byte = msg.data[0]
            data = {"F_reset" : byte, "Timestamp": msg.timestamp} 

        elif id_name is "BSPD_FAULT":
            collection = database[id_name]
            byte = msg.data[0]
            data = {"F_bspd_current_brake_fault" : byte, "Timestamp": msg.timestamp} 

            collection = database[id_name]
            byte = msg.data[1]
            data = {"sensor_failure" : byte, "Timestamp": msg.timestamp} 

            collection = database[id_name]
            byte = msg.data[2]
            data = {"throttle_brake_check" : byte, "Timestamp": msg.timestamp} 

            collection = database[id_name]
            byte = msg.data[3]
            data = {"throttle_implausbility" : byte, "Timestamp": msg.timestamp} 

            collection = database[id_name]
            byte = msg.data[4]
            data = {"torque_multi" : byte, "Timestamp": msg.timestamp} 

        elif id_name is "BSPD_START":
            collection = database[id_name]
            byte = msg.data[0]
            data = {"start_btn_state" : byte, "Timestamp": msg.timestamp} 

        elif id_name is "BSPD_THROTTLE":
            collection = database[id_name]
            byte = msg.data[0]
            data = {"byte_1" : byte, "Timestamp": msg.timestamp} 

            collection = database[id_name]
            byte_0 = msg.data[1]
            byte_1 = msg.data[2]
            data = {"Throttle_byte_0" : byte_0, "Throttle_byte_1": byte_1, "Timestamp": msg.timestamp} 

        elif id_name is "BSPD_THROTTLE":
            collection = database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            data = {"brake_avg_byte_0" : byte_0, "brake_avg_byte_1": byte_1, "Timestamp": msg.timestamp} 

            collection = database[id_name]
            byte_0 = msg.data[2]
            byte_1 = msg.data[3]
            data = {"brake_rear_byte_0" : byte_0, "brake_rear_byte_1": byte_1, "Timestamp": msg.timestamp} 

            collection = database[id_name]
            byte_0 = msg.data[4]
            byte_1 = msg.data[5]
            data = {"brake_front_byte_0" : byte_0, "brake_front_byte_1": byte_1, "Timestamp": msg.timestamp} 

        elif id_name is "UNITEK":
            collection = database[id_name]
            byte_0 = msg.data[0]
            byte_1 = msg.data[1]
            byte_2 = msg.data[2]

            data = {"unitek_byte_0" : byte_0, "unitek_byte_1": byte_1, "unitek_byte_2": byte_2, "Timestamp": msg.timestamp} 

        elif id_name is "M150_REGEN":
            collection = database[id_name]
            byte_0 = msg.data[0]
            data = {"regen_flag" : byte_0, "Timestamp": msg.timestamp} 
        
        return (collection, data)








            

