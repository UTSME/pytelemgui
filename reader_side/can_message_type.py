import copy
import time
import datetime

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
                               "Avg_cell_resistance_byte_1" : 0, 
                               "Pack_ccl_byte_0" : 0, 
                               "Pack_ccl_byte_1" : 0,
                               "Pack_dcl_byte_0" : 0, 
                               "Pack_dcl_byte_1" : 0, 
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

        self.SIMPLE_CAN_TABLE = {
            "OrionBMS_Set1" : {"Rolling Counter" : 0, 
                               "Custom Flag 1" : 0, 
                               "Custom Flag 2" : 0, 
                               "Custom Flag 3" : 0, 
                               "Timestamp": 0}, 
            "OrionBMS_Set2" : {"High Temp" : 0, 
                               "High Temp ID" : 0, 
                               "Low Temp" : 0, 
                               "Low Temp ID" : 0,   
                               "Timestamp": 0},
            "OrionBMS_Set3" : {"High Cell Volt" : 0, 
                              "High Cell ID" : 0, 
                              "Low Cell Volt" : 0,  
                              "Low Cell ID" : 0,
                              "Timestamp": 0},
            "OrionBMS_Set4" : {"Pack Inst Volts" : 0, 
                               "Pack Current" : 0, 
                               "Pack Summed Volts" : 0,
                               "Timestamp": 0} ,
            "OrionBMS_Set5" : {"Avg Cell Resist" : 0, 
                               "Pack CCL" : 0, 
                               "Pack DCL" : 0, 
                               "Timestamp": 0},
            "PDM15_STD" :     {"PDM STD" : 0, 
                               "Timestamp": 0},
            "PDM15_MSG0" :    {"Fault: HVS BMS" : 0,
                               "Fault: HVS PDOC" : 0, 
                               "Fault: HVS IMD" : 0,
                               "Fault: IMD IMD" : 0,
                               "HV Precharge" : 0,
                               "HV Precharged" : 0,
                               "Ready to Drive" : 0,
                               "Drive Enable" : 0, 
                               "Timestamp": 0},
            "PDM15_MSG1" :    {"Brake Trigger" : 0,
                               "BCM Control On" : 0,
                               "BCM Control" : 0,  
                               "Shutdown Lock" : 0,
                               "Standby" : 0,
                               "Timestamp": 0} ,
            "PDM15_MSG2" :    {"Reset" : 0, 
                               "Timestamp": 0} ,
            "BSPD_FAULT" :    {"Crnt Brake Fault" : 0, 
                               "Sensor Failure" : 0,
                               "Thrt Brake Check" : 0,
                               "Thrt Implaus" : 0,
                               "Torque Multi" : 0, 
                               "Timestamp": 0} ,
            "BSPD_START" :    {"Start Btn State" : 0, 
                               "Timestamp": 0} ,
            "BSPD_THROTTLE" : {"BSPD Throttle" : 0,
                               "Throttle" : 0, 
                               "Timestamp": 0},
            "BSPD_BRAKE" :    {"Brake Avg" : 0, 
                               "Brake Rear" : 0, 
                               "Brake Front" : 0, 
                               "Timestamp": 0} ,
            "UNITEK" :        {"Unitek Flag 1" : 0, 
                               "Unitek Flag 2": 0, 
                               "Unitek Flag 3": 0, 
                               "Timestamp": 0},
            "M150_REGEN" :    {"Regen Flag" : 0, 
                               "Timestamp": 0} 
        }

        self.previous_simple_table = copy.deepcopy(self.SIMPLE_CAN_TABLE)

    def compare_database(self, id, key):
        if self.SIMPLE_CAN_TABLE[id][key] is not self.previous_simple_table[id][key]:
            return False
        else:
            return True

    def update_previous_db(self):
        self.previous_simple_table = copy.deepcopy(self.SIMPLE_CAN_TABLE)

    def get_can_table(self):
        self.convert_to_simple()
        return self.SIMPLE_CAN_TABLE


    def set_db_data(self, id_name, msg):
        check = False
        # print(id_name)
        for key in msg:
            self.CAN_BUS_DATA_TYPES[id_name][key] = msg[key]
        
        return (self.get_can_table())

    # Yes I like to see the world burn
    # No I can't use a for loop because my keys are different
    # Yes, please do figure out a nice way of doing this
    def convert_to_simple(self):

        ##### ORION BMS SET 1
        self.SIMPLE_CAN_TABLE["OrionBMS_Set1"]["Rolling Counter"] = self.CAN_BUS_DATA_TYPES["OrionBMS_Set1"]["Rolling Counter"]
        self.SIMPLE_CAN_TABLE["OrionBMS_Set1"]["Custom Flag 1"] = self.CAN_BUS_DATA_TYPES["OrionBMS_Set1"]["custom_flag_1"]
        self.SIMPLE_CAN_TABLE["OrionBMS_Set1"]["Custom Flag 1"] = self.CAN_BUS_DATA_TYPES["OrionBMS_Set1"]["custom_flag_2"]
        self.SIMPLE_CAN_TABLE["OrionBMS_Set1"]["Custom Flag 1"] = self.CAN_BUS_DATA_TYPES["OrionBMS_Set1"]["custom_flag_3"]
        self.SIMPLE_CAN_TABLE["OrionBMS_Set1"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["OrionBMS_Set1"]["Timestamp"]//1000.0)

        ##### ORION BMS SET 2
        self.SIMPLE_CAN_TABLE["OrionBMS_Set2"]["High Temp"] = self.CAN_BUS_DATA_TYPES["OrionBMS_Set2"]["High_temperature"]
        self.SIMPLE_CAN_TABLE["OrionBMS_Set2"]["High Temp ID"] = self.CAN_BUS_DATA_TYPES["OrionBMS_Set2"]["High_temp_id"]
        self.SIMPLE_CAN_TABLE["OrionBMS_Set2"]["Low Temp"] = self.CAN_BUS_DATA_TYPES["OrionBMS_Set2"]["Low_temperature"]
        self.SIMPLE_CAN_TABLE["OrionBMS_Set2"]["Low Temp ID"] = self.CAN_BUS_DATA_TYPES["OrionBMS_Set2"]["Low_temp_id"]
        self.SIMPLE_CAN_TABLE["OrionBMS_Set2"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["OrionBMS_Set2"]["Timestamp"]//1000.0)
        
        ##### ORION BMS SET 3
        # Big Endian - Units are 0.0001V
        high_cell_volt = 0.0001 * ((self.CAN_BUS_DATA_TYPES["OrionBMS_Set3"]["High_cell_voltage_byte_1"] << 8) | (self.CAN_BUS_DATA_TYPES["OrionBMS_Set3"]["High_cell_voltage_byte_1"]))
        self.SIMPLE_CAN_TABLE["OrionBMS_Set3"]["High Cell Volt"] = high_cell_volt
        self.SIMPLE_CAN_TABLE["OrionBMS_Set3"]["High Cell ID"] = self.CAN_BUS_DATA_TYPES["OrionBMS_Set3"]["High_cell_volt_id"]
       
        # Big Endian - Units are 0.0001V
        low_cell_volt = 0.0001 * ((self.CAN_BUS_DATA_TYPES["OrionBMS_Set3"]["Low_cell_voltage_byte_1"] << 8) | (self.CAN_BUS_DATA_TYPES["OrionBMS_Set3"]["Low_cell_voltage_byte_0"]))
        self.SIMPLE_CAN_TABLE["OrionBMS_Set3"]["Low Cell Volt"] = low_cell_volt
        self.SIMPLE_CAN_TABLE["OrionBMS_Set3"]["Low Cell ID"] = self.CAN_BUS_DATA_TYPES["OrionBMS_Set3"]["Low_cell_volt_id"]
        self.SIMPLE_CAN_TABLE["OrionBMS_Set3"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["OrionBMS_Set3"]["Timestamp"]//1000.0)
        
        ##### ORION BMS SET 4
        # Big Endian - Units are 0.1V
        pack_inst_volt = 0.1 * ((self.CAN_BUS_DATA_TYPES["OrionBMS_Set4"]["Pack_inst_voltage_byte_1"] << 8) | (self.CAN_BUS_DATA_TYPES["OrionBMS_Set4"]["Pack_inst_voltage_byte_0"]))
        self.SIMPLE_CAN_TABLE["OrionBMS_Set4"]["Pack Inst Volts"] = pack_inst_volt       
        
        # Big Endian - Units are 0.1A
        pack_inst_current = 0.1 * ((self.CAN_BUS_DATA_TYPES["OrionBMS_Set4"]["Pack_current_byte_1"] << 8) | (self.CAN_BUS_DATA_TYPES["OrionBMS_Set4"]["Pack_current_byte_0"]))
        self.SIMPLE_CAN_TABLE["OrionBMS_Set4"]["Pack Current"] = pack_inst_current
        
        # Big Endian - Units are 0.1V
        pack_summed_volt = 0.1 * ((self.CAN_BUS_DATA_TYPES["OrionBMS_Set4"]["Pack_summed_volt_byte_1"] << 8) | (self.CAN_BUS_DATA_TYPES["OrionBMS_Set4"]["Pack_summed_volt_byte_0"]))
        self.SIMPLE_CAN_TABLE["OrionBMS_Set4"]["Pack Summed Volts"] = pack_summed_volt
        self.SIMPLE_CAN_TABLE["OrionBMS_Set4"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["OrionBMS_Set4"]["Timestamp"]//1000.0)

        ##### ORION BMS SET 5
        # Big Endian - Units are 0.01mOhm
        avg_cell_resist = 0.1 * ((self.CAN_BUS_DATA_TYPES["OrionBMS_Set5"]["Avg_cell_resistance_byte_1"] << 8) | (self.CAN_BUS_DATA_TYPES["OrionBMS_Set5"]["Avg_cell_resistance_byte_0"]))
        self.SIMPLE_CAN_TABLE["OrionBMS_Set5"]["Avg Cell Resist"] = avg_cell_resist       
        
        # Big Endian - Units are 1A
        pack_ccl = 0.1 * ((self.CAN_BUS_DATA_TYPES["OrionBMS_Set5"]["Pack_ccl_byte_1"] << 8) | (self.CAN_BUS_DATA_TYPES["OrionBMS_Set5"]["Pack_ccl_byte_0"]))
        self.SIMPLE_CAN_TABLE["OrionBMS_Set5"]["Pack CCL"] = pack_inst_current
        
        # Big Endian - Units are 1A
        pack_dcl = 0.1 * ((self.CAN_BUS_DATA_TYPES["OrionBMS_Set5"]["Pack_dcl_byte_1"] << 8) | (self.CAN_BUS_DATA_TYPES["OrionBMS_Set5"]["Pack_dcl_byte_0"]))
        self.SIMPLE_CAN_TABLE["OrionBMS_Set5"]["Pack DCL"] = pack_summed_volt
        self.SIMPLE_CAN_TABLE["OrionBMS_Set5"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["OrionBMS_Set5"]["Timestamp"]//1000.0)

        ##### PDM15_STD
        self.SIMPLE_CAN_TABLE["PDM15_STD"]["PDM STD"] = self.CAN_BUS_DATA_TYPES["PDM15_STD"]["PDM_STD"]
        self.SIMPLE_CAN_TABLE["PDM15_STD"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["PDM15_STD"]["Timestamp"]//1000.0)

        ##### PDM15_MSG0
        self.SIMPLE_CAN_TABLE["PDM15_MSG0"]["Fault: HVS BMS"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG0"]["F_fault_hvs_bms"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG0"]["Fault: HVS PDOC"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG0"]["F_fault_hvs_pdoc"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG0"]["Fault: HVS IMD"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG0"]["F_fault_hvs_imd"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG0"]["Fault: IMD IMD"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG0"]["F_fault_imd_imd"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG0"]["HV Precharge"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG0"]["F_hv_precharge"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG0"]["HV Precharged"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG0"]["F_hv_precharged"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG0"]["Ready to Drive"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG0"]["F_ready_to_drive"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG0"]["Drive Enable"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG0"]["F_drive_enable"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG0"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["PDM15_MSG0"]["Timestamp"]//1000.0)

        ##### PDM15_MSG1
        self.SIMPLE_CAN_TABLE["PDM15_MSG1"]["Brake Trigger"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG1"]["F_brake_trigger"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG1"]["BCM Control On"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG1"]["F_bcm_control_on"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG1"]["BCM Control"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG1"]["F_bcm_control"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG1"]["Shutdown Lock"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG1"]["F_shutdown_lock"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG1"]["Standby"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG1"]["F_standby"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG1"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["PDM15_MSG1"]["Timestamp"]//1000.0)

        ##### PDM15_MSG2
        self.SIMPLE_CAN_TABLE["PDM15_MSG2"]["Reset"] = self.CAN_BUS_DATA_TYPES["PDM15_MSG2"]["F_reset"]
        self.SIMPLE_CAN_TABLE["PDM15_MSG2"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["PDM15_MSG2"]["Timestamp"]//1000.0)

        ##### BSPD FAULTS
        self.SIMPLE_CAN_TABLE["BSPD_FAULT"]["Crnt Brake Fault"] = self.CAN_BUS_DATA_TYPES["BSPD_FAULT"]["F_bspd_current_brake_fault"]
        self.SIMPLE_CAN_TABLE["BSPD_FAULT"]["Sensor Failure"] = self.CAN_BUS_DATA_TYPES["BSPD_FAULT"]["sensor_failure"]
        self.SIMPLE_CAN_TABLE["BSPD_FAULT"]["Thrt Brake Check"] = self.CAN_BUS_DATA_TYPES["BSPD_FAULT"]["throttle_brake_check"]
        self.SIMPLE_CAN_TABLE["BSPD_FAULT"]["Thrt Implaus"] = self.CAN_BUS_DATA_TYPES["BSPD_FAULT"]["throttle_implausbility"]
        self.SIMPLE_CAN_TABLE["BSPD_FAULT"]["Torque Multi"] = self.CAN_BUS_DATA_TYPES["BSPD_FAULT"]["torque_multi"]
        self.SIMPLE_CAN_TABLE["BSPD_FAULT"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["BSPD_FAULT"]["Timestamp"]//1000.0)

        ##### BSPD_START
        self.SIMPLE_CAN_TABLE["BSPD_START"]["Start Btn State"] = self.CAN_BUS_DATA_TYPES["BSPD_START"]["start_btn_state"]
        self.SIMPLE_CAN_TABLE["BSPD_START"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["BSPD_START"]["Timestamp"]//1000.0)

        ##### BSPD_THROTTLE
        self.SIMPLE_CAN_TABLE["BSPD_THROTTLE"]["BSPD Throttle"] = self.CAN_BUS_DATA_TYPES["BSPD_THROTTLE"]["bspd_throttle_byte_1"]

        # Signed Little Endian
        throttle = ((self.CAN_BUS_DATA_TYPES["BSPD_THROTTLE"]["Throttle_byte_0"] << 8) | (self.CAN_BUS_DATA_TYPES["BSPD_THROTTLE"]["Throttle_byte_1"]))
        self.SIMPLE_CAN_TABLE["BSPD_THROTTLE"]["Throttle"] = throttle
        self.SIMPLE_CAN_TABLE["BSPD_THROTTLE"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["BSPD_THROTTLE"]["Timestamp"]//1000.0)

        ##### BSPD_Brake
        # Signed Little Endian
        brake_avg = ((self.CAN_BUS_DATA_TYPES["BSPD_BRAKE"]["brake_avg_byte_0"] << 8) | (self.CAN_BUS_DATA_TYPES["BSPD_BRAKE"]["brake_avg_byte_1"]))
        self.SIMPLE_CAN_TABLE["BSPD_BRAKE"]["Brake Avg"] = brake_avg
        # Signed Little Endian
        brake_rear = ((self.CAN_BUS_DATA_TYPES["BSPD_BRAKE"]["brake_rear_byte_0"] << 8) | (self.CAN_BUS_DATA_TYPES["BSPD_BRAKE"]["brake_rear_byte_1"]))
        self.SIMPLE_CAN_TABLE["BSPD_BRAKE"]["Brake Rear"] = brake_rear
        # Signed Little Endian
        brake_front = ((self.CAN_BUS_DATA_TYPES["BSPD_BRAKE"]["brake_front_byte_0"] << 8) | (self.CAN_BUS_DATA_TYPES["BSPD_BRAKE"]["brake_front_byte_1"]))
        self.SIMPLE_CAN_TABLE["BSPD_BRAKE"]["Brake Front"] = brake_front
        self.SIMPLE_CAN_TABLE["BSPD_BRAKE"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["BSPD_BRAKE"]["Timestamp"]//1000.0)

        ##### Unitek
        self.SIMPLE_CAN_TABLE["UNITEK"]["Unitek Flag 1"] = self.CAN_BUS_DATA_TYPES["UNITEK"]["unitek_byte_0"]
        self.SIMPLE_CAN_TABLE["UNITEK"]["Unitek Flag 2"] = self.CAN_BUS_DATA_TYPES["UNITEK"]["unitek_byte_1"]
        self.SIMPLE_CAN_TABLE["UNITEK"]["Unitek Flag 3"] = self.CAN_BUS_DATA_TYPES["UNITEK"]["unitek_byte_2"]
        self.SIMPLE_CAN_TABLE["UNITEK"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["UNITEK"]["Timestamp"]//1000.0)

        ##### M150_REGEN
        self.SIMPLE_CAN_TABLE["M150_REGEN"]["Regen Flag"] = self.CAN_BUS_DATA_TYPES["M150_REGEN"]["regen_flag"]
        self.SIMPLE_CAN_TABLE["M150_REGEN"]["Timestamp"] = datetime.datetime.fromtimestamp(self.CAN_BUS_DATA_TYPES["M150_REGEN"]["Timestamp"]//1000.0)







            

