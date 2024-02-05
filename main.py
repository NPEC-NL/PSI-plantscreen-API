from __future__ import print_function
from plantscreen.swagger_client.rest import ApiException
from pprint import pprint
import datetime
from plantscreen.PSI_api import PSI_API

# create an instance of the API class

# G6
#api = PSI_API('192.168.80.8', 8061) 
# G7
api = PSI_API('192.168.80.9', 8061) 

try:
    # Returns a list of all experiment IDs in the database.
    #api_response = api.ExperimentID()
    #print(api_response.IDs)

    # Returns one experiment by experiment ID.
    #api_response = api.Experiment(13)
    #print(api_response)

    # Returns all experiments whose rounds took place between defined times.
    #start=datetime.datetime(year=2023, month=9, day=1)
    #stop=datetime.datetime(year=2023, month=10, day=25)
    #experiment_list = api.ExperimentDate(start, stop)
    #print(experiment_list[0].CreatedDate)
    
    
    # Returns all experiments that belong to the user defined by ID
    #experiment_list = api.experiment_owner(6)
    #print(experiment_list)
    #for exp in experiment_list:
         #print(exp.CreatedDate)
    #print(experiment_list[0].CreatedDate)


    # Returns a list of all experiment owner IDs in the database
    #experiment_list = api.owner_id()
    #print(experiment_list)

    # Returns the owner(s) of the experiment by ID
    #experiment_list = api.owner([6, 7])
    #print(experiment_list)

    # Returns the experiment notes that the user saved for the experiment defined by ID
    #note_list = api.note_experiment(6)
    #print(note_list)


    # Returns one round by round ID
    #round = api.round(5)
    #print(round)

    # Returns all rounds measured in the experiment defined by ID
    #round_list = api.round_experiment(5)
    #print(round_list)

    # Returns all rounds measured in the experiment defined by ID between defined times
    #start="2023-04-04T00:00:00"
    #stop="2023-04-04T10:00:00"
    #round_list = api.round_date_experiment(5, start, stop)
    #print(round_list)

    # Returns the round order in the experiment by round ID.
    #round_list = api.round_order_round(12)
    #print(round_list)

    # Returns all rounds measured in the experiment defined by ID
    #round_list = api.round_order_experiment(5)
    #print(round_list)

    # Returns all rounds measured in the experiment defined by ID between defined times.
    #start = "2023-04-04T08:00:00"
    #stop = "2023-04-04T10:00:00"
    #round_list = api.round_order_date_experiment(5, start, stop)
    #print(round_list)
    

    # Rturns one scheduled action by action ID.
    #action = api.action(4)
    #print(action)

    # Returns all scheduled actions in the experiment defined by ID
    #action_list = api.action_experiment(4)
    #print(action_list)

    # Returns all unfinished scheduled actions (with pending and running action state) in the experiment defined by ID
    #action_list = api.action_not_done_experiment(12)
    #print(action_list)

    # Returns one group of scheduled actions by action group ID.
    #action_list = api.action_group(4)
    #print(action_list)

    # Returns one group of scheduled actions to which a round defined by ID belongs.
    #action_list = api.action_group_round(4)
    #print(action_list)

    # Returns one protocol of scheduled action by protocol ID.
    #action_list = api.action_protocol(4)
    #print(action_list)

    # Returns one group of scheduled actions that belong to round defined by ID.
    #action_list = api.action_protocol_round(4)
    #print(action_list)

    # Returns one device by device ID.
    #device = api.device(3)
    #print(device)

    # Returns all active devices that have not ended validity.
    #device_list = api.device_active()
    #print(device_list)

    # Returns all devices that contains the system profile defined by ID.
    #device_list = api.device_profile(1)
    #print(device_list)

    # Returns a list of all system profile IDs in the database
    #profile_list = api.profile_id()
    #print(profile_list)

    # Returns one system profile by profile ID.
    #profile_list = api.profile(1)
    #print(profile_list)

    # Returns the active system profile.
    #profile_list = api.profile_active()
    #print(profile_list)

    # Returns one tray by tray ID.
    #tray = api.tray(1)
    #print(tray)

    # Returns all trays measured in the round defined by ID.
    #tray_list = api.tray_round(1)
    #print(tray_list)

    # Returns one tray type by tray type ID.
    #tray_type = api.tray_type(32)
    #print(tray_type)

    # Returns one tray type which is assigned to the tray defined by ID.
    #tray_type = api.tray_type_tray(1)
    #print(tray_type)

    # Returns one tray type which is assigned to the tray profile defined by ID.
    #tray_type = api.tray_type_tray_profile(1)
    #print(tray_type)

    # Returns one tray profile by tray profile ID.
    #tray_profile = api.tray_profile(11)
    #print(tray_profile)

    # Returns one tray profile to which tray defined by ID is assigned.
    #start = "2021-12-23T08:00:00"
    #stop= "2024-01-01T08:00:00"
    #tray_profile = api.tray_profile_used_tray(11, start, stop)
    #print(tray_profile)

    # Returns one tray profile to which tray defined by ID was assigned on the defined time.
    #date = "2022-09-24T19:10:19"
    #tray_profile = api.tray_profile_to_date_tray(11, date)
    #print(tray_profile)

    # Returns a scales mapping for tray defined by ID.
    #scales_mapping = api.scales_mapping_tray(1) 
    #print(scales_mapping)

    # Returns a list of plants by the list of plant IDs.
    #plant_list = api.plant([1,2]) 
    #print(plant_list)

    # Returns list of plants which are assigned to the tray defined by ID.
    #plant_list = api.plant_tray(2)
    #print(plant_list)

    # Returns plants that were assigned to the tray defined by tray ID between defined times.
    #start = "2021-12-23T08:00:00"
    #stop= "2024-01-01T08:00:00"
    #plant_list = api.plant_tray_profile_tray(2, start, stop)
    #print(plant_list)

    # Returns plants that were assigned to the tray profile defined by tray profile ID without time limit.
    #plant_list = api.plant_tray_profile(1)
    #print(plant_list)

    # Returns all plant heights measured in the round defined by ID.
    #plant_heights = api.plant_height_round(1)
    #print(plant_heights)

    # Returns all plant leaves for the plant assigned to the tray defined by the plant and tray ID.
    #plant_leaves = api.plant_leaf(1, 2)
    #print(plant_leaves)

    # Returns FluorCam imaging data by FC measure ID.
    #fc_imag = api.fc_imaging_measure(1)
    #print(fc_imag)

    # Returns FluorCam imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    #fc_imag = api.fc_imaging(1, 1, 1)
    #print(fc_imag)
   
    # Returns FluorCam imaging extended data by FC measure ID. (Only available for field systems.)
    #fc_img = api.fc_imaging_extended_data_measure(1)
    #print(fc_img)

    # Returns FluorCam extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. (Only available for field systems.)
    #fc_img = api.fc_imaging_extended_data(1, 1, 1)
    #print(fc_img)

    # Returns the FluorCam plant mask created for the measured tray defined by FC measure ID.
    #fc_mask = api.fc_plant_mask_measure(1)
    #print(fc_mask)

    # Returns FluorCam plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    #fc_mask = api.fc_plant_mask(1, 1, 1)
    #print(fc_mask)

    # Returns one FluorCam parameter by parameter ID.
    #fc_param = api.fc_param(10)
    #print(fc_param)

    # Returns the FluorCam plant and leaf parameters used in the analysis defined by analyse ID.
    #fc_param = api.i_fc_param_used_analyse(10)
    #print(fc_param)

    # Returns the FluorCam plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    #fc_param = api.fc_param_used(1, 1, 1)
    #print(fc_param)

    # Returns the FluorCam parameter image for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    #fc_paramimg = api.fc_param_image_analyse(1, 1)
    #print(fc_paramimg)

    # Returns the FluorCam parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    #fc_paramimg = api.fc_param_image(1, 1, 1, 1)
    #print(fc_paramimg)

    #  Returns the FluorCam plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    #fc_param= api.fc_plant_param_analyse(1, 1)
    #print(fc_param)

    # Returns the FluorCam plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    #fc_param= api.fc_plant_param(1, 1, 1, 1)
    #print(fc_param)

    # Returns the FluorCam leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    #fc_param= api.fc_leaf_param_analyse(1, 1)
    #print(fc_param)

    # Returns the FluorCam leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    #fc_param= api.fc_leaf_param(1, 1, 1, 1)
    #print(fc_param)

    # Returns Hyperspectral imaging data by HC measure ID.
    #hc_img= api.hc_imaging_measure(1)
    #print(hc_img)
   
    # Returns Hyperspectral imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    #hc_img= api.hc_imaging(1, 1, 1)
    #print(hc_img)

    # Returns Hyperspectral imaging extended data by HC measure ID. (Only available for field systems.)
    #hc_img= api.hc_imaging_extended_data_measure(200)
    #print(hc_img)

    # Returns Hyperspectral extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. (Only available for field systems.)
    #hc_img= api.hc_imaging_extended_data(1, 1, 1)
    #print(hc_img)

    # Returns the Hyperspectral RGB image created for the measured tray by HC measure ID. 
    #hc_img = api.hc_rgb_image_measure(1)
    #print(hc_img)

    # Returns the Hyperspectral RGB image created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    #hc_img = api.hc_rgb_image(1, 1, 1)
    #print(hc_img)   

    # Returns the Hyperspectral plant mask created for the measured tray defined by HC measure ID.
    #hc_mask = api.hc_plant_mask_measure(200)
    #print(hc_mask) 

    # Returns Hyperspectral plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    #hc_mask = api.hc_plant_mask(1, 1, 1)
    #print(hc_mask) 

    # Returns one Hyperspectral parameter by parameter ID.
    #hc_param = api.hc_param(10)
    #print(hc_param) 

    # Returns the Hyperspectral plant and leaf parameters used in the analysis defined by analyse ID.
    #hc_param = api.hc_param_used_analyse(10)
    #print(hc_param) 

    # Returns the Hyperspectral plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    #hc_param = api.hc_param_used(1, 1, 1)
    #print(hc_param)   

    # Returns the Hyperspectral parameter image for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    #hc_param = api.hc_param_image_analyse(1, 1)
    #print(hc_param)     

    # Returns the Hyperspectral parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    #hc_param = api.hc_param_image(1, 1, 1, 1)
    #print(hc_param)    

    # Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    #hc_param = api.hc_plant_param_analyse(1, 1)
    #print(hc_param)    

    # Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    #hc_param = api.hc_plant_param(1, 1, 1, 1)
    #print(hc_param)    

    # Returns the Hyperspectral statistic leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    #hc_param = api.hc_leaf_param_analyse(1, 1)
    #print(hc_param)    

    # Returns the Hyperspectral Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    #hc_param = api.hc_leaf_param(1, 1, 1, 1)
    #print(hc_param)    

    # Returns Thermal imaging data by IR measure ID.
    #ir_imag = api.ir_imaging_measure(1)
    #print(ir_imag)    

    # Returns Thermal imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    #ir_imag = api.ir_imaging(1, 1, 1)
    #print(ir_imag)    

    # Returns Thermal imaging extended data by IR measure ID. 
    #ir_imag = api.ir_imaging_extended_data_measure(1)
    #print(ir_imag) 

    # Returns Thermal extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID. (Only available for field systems.)
    #ir_imag = api.ir_imaging_extended_data(1, 1, 1)
    #print(ir_imag) 

    # Returns the Thermal plant mask created for the measured tray defined by IR measure ID.
    #ir_mask = api.ir_plant_mask_measure(1)
    #print(ir_mask) 

    # Returns Thermal plant masks created for the tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    #ir_mask = api.ir_plant_mask(1, 1, 1)
    #print(ir_mask) 

    # Returns Thermal imaging data masked by the plant mask defined by IR measure ID.
    #ir_imag = api.ir_plant_mask_image_measure(1)
    #print(ir_imag) 

    # Returns Thermal imaging data masked by the plant mask for tray defined by tray ID, by round ID of round in which the tray was measured and by device defined by device ID.
    #ir_imag = api.ir_plant_mask_image(1, 1, 1)
    #print(ir_imag) 

    # Returns one Thermal parameter by parameter ID.
    #ir_param = api.ir_param(1)
    #print(ir_param) 

    # Returns the Thermalplant and leaf parameters used in the analysis defined by analyse ID.
    #ir_param = api.ir_param_used_analyse(1)
    #print(ir_param)   

    # Returns the Thermal plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    #ir_param = api.ir_param_used(1, 1, 1)
    #print(ir_param)  

    # Returns the Thermal plant parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    #ir_param = api.ir_plant_param_analyse(1, 1)
    #print(ir_param)  
    
    # Returns the Thermal statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    #ir_param = api.ir_plant_param(1, 1, 1, 1)
    #print(ir_param) 

    # eturns the Thermal statistic leaf parameter values for the parameter defined by parameter ID and calculated in the analysis defined by analyse ID.
    #ir_param = api.ir_leaf_param_analyse(1, 1)
    #print(ir_param) 

    # Returns the Thermal Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID.
    ir_param = api.ir_leaf_param(1, 1, 1, 1)
    print(ir_param) 



    # Returns all used probe.
    #probe_list = api.probe()
    #print(probe_list)

    # Returns all probe values measured between times.
    #start=datetime.datetime(year=2023, month=9, day=1, hour = 1)
    #stop=datetime.datetime(year=2023, month=9, day=1, hour= 2)
    #probe_values = api.probe_value_date(start, stop)
    #print(probe_values)

    # Returns all probe values for probe defined by probe ID measured between times.
    #id=8
    #start=datetime.datetime(year=2023, month=9, day=1, hour = 1)
    #stop=datetime.datetime(year=2023, month=9, day=1, hour= 2)
    #probe_values = api.probe_value_date_probe(id,start, stop)
    #print(probe_values)

except ApiException as e:
    print("Exception when calling ActionApi->get_action: %s\n" % e)
    


