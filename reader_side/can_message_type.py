

class can_msg_types:

    def __init__(self, debug=False):
        self.debug = debug

        self.CAN_BUS_DATA_TYPES = {
            "OrionBMS_Set1" : {"Rolling Counter" : 0, 
                               "custom_flag_1" : 0, 
                               "custom_flag_2" : 0, 
                               "custom_flag_3" : 0, 
                               "checksum" : 0, 
                               "Timestamp": 0}, 
            "OrionBMS_Set2" : {"High_temperature" : 0, 
                               "High_temp_id" : 0, 
                               "Low_temperature" : 0, 
                               "Low_temp_id" : 0, 
                               "checksum" : 0,  
                               "Timestamp": 0},
            "OrionBMS_Set3" : {"High_cell_voltage_byte_0" : 0, 
                              "High_cell_voltage_byte_1" : 0, 
                              "High_cell_volt_id" : 0, 
                              "Low_cell_voltage_byte_0" : 0, 
                              "Low_cell_voltage_byte_1" : 0, 
                              "Low_cell_volt_id" : 0, 
                              "checksum" : 0,  
                              "Timestamp": 0},
            "OrionBMS_Set4" : {"Pack_inst_voltage_byte_0" : 0, 
                               "Pack_inst_voltage_byte_1" : 0, 
                               "Pack_current_byte_0" : 0, 
                               "Pack_current_byte_1" : 0, 
                               "Pack_summed_volt_byte_0" : 0, 
                               "Pack_summed_volt_byte_1" : 0, 
                               "checksum" : 0, 
                               "Timestamp": 0} ,
            "OrionBMS_Set5" : {"Avg_cell_resistance_byte_0" : 0, 
                               "Avg_cell_resistance_byte_0" : 0, 
                               "Pack_ccl_byte_0" : 0, 
                               "Pack_ccl_byte_1" : 0,
                               "Pack_dcl_byte_0" : 0, 
                               "Pack_dcl_byte_0" : 0, 
                               "checksum" : 0, 
                               "Timestamp": 0},
            "PDM15_STD" :     {"PDM_STD" : 0, 
                               "Timestamp": 0},
            "PDM15_MSG0" :    {"F_fault_hvs_bms" : 0,
                               "F_fault_hvs_pdoc" : 0, 
                               "F_fault_hvs_imd" : 0,
                               "F_fault_imd_imd" : 0,
                               "F_hv_precharge" : 0,
                               "F_hv_precharged" : 0,
                               "F_ready_to_drive" : 0,
                               "F_drive_enable" : 0, 
                               "Timestamp": 0},
            "PDM15_MSG1" :    {"F_brake_trigger" : 0,
                               "F_bcm_control_on" : 0,
                               "F_bcm_control" : 0,  
                               "F_shutdown_lock" : 0,
                               "F_standby" : 0,
                               "Timestamp": 0} ,
            "PDM15_MSG2" :    {"F_reset" : 0, 
                               "Timestamp": 0} ,
            "BSPD_FAULT" :    {"F_bspd_current_brake_fault" : 0, 
                               "sensor_failure" : 0,
                               "throttle_brake_check" : 0,
                               "throttle_implausbility" : 0,
                               "torque_multi" : 0, 
                               "Timestamp": 0} ,
            "BSPD_START" :    {"start_btn_state" : 0, 
                               "Timestamp": 0} ,
            "BSPD_THROTTLE" : {"bspd_throttle_byte_1" : 0,
                               "Throttle_byte_0" : 0, 
                               "Throttle_byte_1": 0, 
                               "Timestamp": 0} ,
            "BSPD_BRAKE" :    {"brake_avg_byte_0" : 0, 
                               "brake_avg_byte_1": 0, 
                               "brake_rear_byte_0" : 0, 
                               "brake_rear_byte_1": 0,
                               "brake_front_byte_0" : 0, 
                               "brake_front_byte_1": 0,
                               "Timestamp": 0} ,
            "UNITEK" :        {"unitek_byte_0" : 0, 
                               "unitek_byte_1": 0, 
                               "unitek_byte_2": 0, 
                               "Timestamp": 0},
            "M150_REGEN" :    {"regen_flag" : 0, 
                               "Timestamp": 0} 
        }

    def get_can_table(self):
        return self.CAN_BUS_DATA_TYPES


    def set_db_data(self, id_name, msg):
        check = False
        # print(id_name)
        for key in msg:
            self.CAN_BUS_DATA_TYPES[id_name][key] = msg[key]
        
        return (self.CAN_BUS_DATA_TYPES)








            

