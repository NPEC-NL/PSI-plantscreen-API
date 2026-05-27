import datetime
import traceback
from os import getenv
from dotenv import load_dotenv
from pprint import pprint

import plantscreen
from plantscreen.rest import ApiException


if __name__ == "__main__":
    """Ëxample implementation of all plantscreen endpoints"""
    load_dotenv()
    # Create an instance of the API class
    api = plantscreen.CompleteAPIClient(getenv('HOST'))

    try:
        # Returns a list of all experiment IDs in the database
        api_response = api.experiment_id()
        pprint(f"Experiments list: {api_response}")

        # Returns one experiment by experiment ID
        api_response = api.experiment(2)
        pprint(f"Experiment by ID: {api_response}")

        # Returns all experiments whose rounds took place between defined times
        start = datetime.datetime(year=2023, month=9, day=1)
        stop = datetime.datetime(year=2023, month=10, day=25)
        experiment_list = api.experiment_date(start, stop)
        pprint(f"All experiments between {start} and {stop}: {experiment_list}")

        # Returns all experiments that belong to the user defined by ID
        experiment_list = api.experiment_owner(6)
        pprint(f"Experiments by owner: {experiment_list}")

        # Returns a list of all experiment owner IDs in the database
        owner_list = api.owner_id()
        pprint(f"Owners list: {owner_list}")

        # Returns the owner(s) of the experiment by ID
        experiment_list = api.owner([6, 7])
        pprint(f"Owners of experiment: {experiment_list}")

        # Returns the experiment notes that the user saved for the experiment defined by ID
        note_list = api.note_experiment(1)
        pprint(f"Notes for experiment: {note_list}")

        """-----------------------------------------------------------------------------------------------------------------
            Rounds
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns one round by round ID
        round = api.round(5)
        pprint(f"Round: {round}")

        # Returns all rounds measured in the experiment defined by ID
        round_list = api.round_experiment(5)
        pprint(f"All rounds of experiment: {round_list}")

        # Returns all rounds measured in the experiment defined by ID between defined times
        start = "2023-04-04T00:00:00"
        stop = "2023-04-04T10:00:00"
        round_list = api.round_date_experiment(5, start, stop)
        pprint(f"All rounds between {start} and {stop}: {round_list}")

        # Returns the round order in the experiment by round ID
        round_list = api.round_order_round(12)
        pprint(f"Round order of experiment: {round_list}")

        # Returns all rounds measured in the experiment defined by ID
        round_list = api.round_order_experiment(5)
        pprint(f"Measured rounds of experiment: {round_list}")

        # Returns all rounds measured in the experiment defined by ID between defined times
        start = "2023-04-04T08:00:00"
        stop = "2023-04-04T10:00:00"
        round_list = api.round_order_date_experiment(5, start, stop)
        pprint(f"All measured rounds between {start} and {stop}: {round_list}")

        """-----------------------------------------------------------------------------------------------------------------
            Actions
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns one scheduled action by action ID
        action = api.action(4)
        pprint(f"Action: {action}")

        # Returns all scheduled actions in the experiment defined by ID
        action_list = api.action_experiment(4)
        pprint(f"Action list: {action_list}")

        # Returns all unfinished scheduled actions (with pending and running action state) in the experiment defined by ID
        action_list = api.action_not_done_experiment(12)
        pprint(f"Unfinished action list: {action_list}")

        # Returns one group of scheduled actions by action group ID
        action_list = api.action_group(4)
        pprint(f"Scheduled actions for group id: {action_list}")

        # Returns one group of scheduled actions to which a round defined by ID belongs
        action_list = api.action_group_round(4)
        pprint(f"Scheduled actions for a round: {action_list}")

        # Returns one protocol of scheduled action by protocol ID
        action_list = api.action_protocol(4)
        pprint(f"Scheduled actions for a protocol: {action_list}")

        # Returns one group of scheduled actions that belong to round defined by ID
        action_list = api.action_protocol_round(4)
        pprint(f"Scheduled actions for a round: {action_list}")

        """-----------------------------------------------------------------------------------------------------------------
            Devices
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns one device by device ID
        device = api.device(11)
        pprint(f"Device: {device}")

        # Returns all active devices that have not ended validity
        device_list = api.device_active()
        pprint(f"Active devices: {device_list}")

        # Returns all devices that contains the system profile defined by ID
        device_list = api.device_profile(1)
        pprint(f"Devices for profile ID: {device_list}")

        """-----------------------------------------------------------------------------------------------------------------
            Profiles
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns a list of all system profile IDs in the database
        profile_list = api.profile_id()
        pprint(f"Profiles list: {profile_list}")

        # Returns one system profile by profile ID
        profile = api.profile(1)
        pprint(f"Profiles bij profile ID: {profile}")

        # Returns the active system profile
        profile_list = api.profile_active()
        pprint(f"Active profiles: {profile_list}")

        """-----------------------------------------------------------------------------------------------------------------
            Trays
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns one tray by tray ID
        tray = api.tray(1)
        pprint(f"Tray bij tray ID: {tray}")

        # Returns all trays measured in the round defined by ID
        tray_list = api.tray_round(1)
        pprint(f"Trays by round ID: {tray_list}")

        # Returns one tray type by tray type ID
        tray_type = api.tray_type(32)
        pprint(f"Trays by tray type ID: {tray_type}")

        # Returns one tray type which is assigned to the tray defined by ID
        tray_type = api.tray_type_tray(1)
        pprint(f"Tray type for tray ID: {tray_type}")

        # Returns one tray type which is assigned to the tray profile defined by ID
        tray_type = api.tray_type_tray_profile(1)
        pprint(f"Tray type for profile ID: {tray_type}")

        # Returns one tray profile by tray profile ID
        tray_profile = api.tray_profile(11)
        pprint(f"Tray profile for profile ID: {tray_profile}")

        # Returns tray profiles to which tray defined by ID is assigned
        start = "2021-12-23T08:00:00"
        stop = "2024-01-01T08:00:00"
        tray_profile_list = api.tray_profile_used_tray(11, start, stop)
        pprint(f"Tray profiles for tray between {start} till {stop}: {tray_profile_list}")

        # Returns one tray profile to which tray defined by ID was assigned on the defined time
        date = "2022-09-24T19:10:19"
        tray_profile = api.tray_profile_to_date_tray(11, date)
        pprint(f"Tray profiles for tray on {date}: {tray_profile}")

        # Returns a scales mapping for tray defined by ID
        scales_mapping = api.scales_mapping_tray(1)
        pprint(f"Scales mapping for tray ID: {scales_mapping}")

        """-----------------------------------------------------------------------------------------------------------------
            Plant
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns a list of plants by the list of plant IDs
        plant_list = api.plant([1, 2])
        pprint(f"Plants by plant ID: {plant_list}")

        # Returns list of plants which are assigned to the tray defined by ID
        plant_list = api.plant_tray(2)
        pprint(f"Plants by tray ID: {plant_list}")

        # Returns plants that were assigned to the tray defined by tray ID between defined times
        start = "2021-12-23T08:00:00"
        stop = "2024-01-01T08:00:00"
        plant_list = api.plant_tray_profile_tray(2, start, stop)
        pprint(f"Plants by tray ID between {start} till {stop}:{plant_list}")

        # Returns plants that were assigned to the tray profile defined by tray profile ID without time limit
        plant_list = api.plant_tray_profile(1)
        pprint(f"Plants by tray profile ID: {plant_list}")

        # Returns all plant heights measured in the round defined by ID
        plant_heights = api.plant_height_round(1)
        pprint(f"Plants height during round: {plant_heights}")

        # Returns all plant leaves for the plant assigned to the tray defined by the plant and tray ID
        plant_leaves = api.plant_leaf(1, 2)
        pprint(f"Leaves of plant by plant and tray ID: {plant_heights}")

        """-----------------------------------------------------------------------------------------------------------------
            FluorCam
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns FluorCam imaging data by measure ID
        fc_img = api.fc_imaging_measure(1)
        pprint(f"imaging information for measurement ID: {fc_img}")

        # Returns FluorCam imaging data for tray defined by tray ID, by round ID of round in which the tray was measured
        # and by device defined by device ID
        fc_img = api.fc_imaging(1, 1, 1)
        pprint(f"imaging information for device, Round, tray ID: {fc_img}")

        # Returns FluorCam imaging extended data by measure ID
        fc_ext_img = api.fc_imaging_extended_data_measure(1)
        pprint(f"imaging extended measurement info for measurement ID: {fc_ext_img}")

        # Returns FluorCam extended data for tray defined by tray ID, by round ID of round in which the tray was measured
        # and by device defined by device ID
        fc_ext_img = api.fc_imaging_extended_data(1, 1, 1)
        pprint(f"imaging extended measurement info for device, Round, tray ID: {fc_ext_img}")

        # Returns the FluorCam plant mask created for the measured tray defined by measure ID
        fc_mask = api.fc_plant_mask_measure(1)
        pprint(f"Plant mask for measurement ID: {fc_mask}")

        # Returns FluorCam plant masks created for the tray defined by tray ID, by round ID of round in which the tray was
        # measured and by device defined by device ID
        fc_mask = api.fc_plant_mask(1, 1, 1)
        pprint(f"Plant mask for device, Round, tray ID: {fc_mask}")

        # Returns one FluorCam parameter by parameter ID
        fc_param = api.fc_param(10)
        pprint(f"Param by param ID: {fc_param}")

        # Returns the FluorCam plant and leaf parameters used in the analysis defined by analyse ID
        fc_param = api.fc_param_used_analyse(10)
        pprint(f"Used param by analysis ID: {fc_param}")

        # Returns the FluorCam plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray
        # was analyzed and by device defined by device ID
        fc_param = api.fc_param_used(1, 1, 1)
        pprint(f"Plant & leaf params by device, tray, round ID: {fc_param}")

        # Returns the FluorCam parameter image for the parameter defined by parameter ID and calculated in the analysis defined
        # by analyse ID
        fc_paramimg = api.fc_param_image_analyse(1, 1)
        pprint(f"Analysis params for param and analysis ID: {fc_param}")

        # Returns the FluorCam parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round in
        # which the tray was analyzed and by device defined by device ID
        fc_paramimg = api.fc_param_image(1, 1, 1, 1)
        pprint(f"Params by device, tray, round, param ID: {fc_param}")

        #  Returns the FluorCam plant parameter values for the parameter defined by parameter ID and calculated in the analysis
        # defined by analyse ID
        fc_param = api.fc_plant_param_analyse(1, 1)
        pprint(f"Plant params by parameter and analysis ID: {fc_param}")

        # Returns the FluorCam plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round
        # in which the tray was analyzed and by device defined by device ID
        fc_param = api.fc_plant_param(1, 1, 1, 1)
        pprint(f"Plant params by device, tray, round, param ID: {fc_param}")

        # Returns the FluorCam leaf parameter values for the parameter defined by parameter ID and calculated in the analysis
        # defined by analyse ID
        fc_param = api.fc_leaf_param_analyse(1, 1)
        pprint(f"Leaf params by parameter and analysis ID: {fc_param}")

        # Returns the FluorCam leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round
        # in which the tray was analyzed and by device defined by device ID
        fc_param = api.fc_leaf_param(1, 1, 1, 1)
        pprint(f"Leaf params by device, tray, round, param ID: {fc_param}")

        """-----------------------------------------------------------------------------------------------------------------
            Hyperspectral
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns Hyperspectral imaging data by measure ID
        hc_img = api.hc_imaging_measure(1)
        pprint(f"imaging information for measurement ID: {hc_img}")

        # Returns Hyperspectral imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and
        # by device defined by device ID
        hc_img = api.hc_imaging(1, 1, 1)
        pprint(f"imaging information for device, Round, tray ID: {hc_img}")

        # Returns Hyperspectral imaging extended data by measure ID
        hc_ext_img = api.hc_imaging_extended_data_measure(200)
        pprint(f"imaging extended measurement info for measurement ID: {hc_ext_img}")

        # Returns Hyperspectral extended data for tray defined by tray ID, by round ID of round in which the tray was measured
        # and by device defined by device ID
        hc_ext_img = api.hc_imaging_extended_data(1, 1, 1)
        pprint(f"imaging extended measurement info for device, Round, tray ID: {hc_ext_img}")

        # Returns the Hyperspectral RGB image created for the measured tray by measure ID
        hc_rgb_img = api.hc_rgb_image_measure(1)
        pprint(f"RGB image for measurement ID: {hc_rgb_img}")

        # Returns the Hyperspectral RGB image created for the tray defined by tray ID, by round ID of round in which the tray was
        # measured and by device defined by device ID
        hc_rgb_img = api.hc_rgb_image(1, 1, 1)
        pprint(f"RGB image for device, Round, tray ID: {hc_rgb_img}")

        # Returns the Hyperspectral plant mask created for the measured tray defined by measure ID
        hc_mask = api.hc_plant_mask_measure(200)
        pprint(f"Plant mask for measurement ID: {hc_mask}")

        # Returns Hyperspectral plant masks created for the tray defined by tray ID, by round ID of round in which the tray was
        # measured and by device defined by device ID
        hc_mask = api.hc_plant_mask(1, 1, 1)
        pprint(f"Plant mask for device, Round, tray ID: {hc_mask}")

        # Returns one Hyperspectral parameter by parameter ID
        hc_param = api.hc_param(10)
        pprint(f"Param by param ID: {hc_param}")

        # Returns the Hyperspectral plant and leaf parameters used in the analysis defined by analyse ID
        hc_param = api.hc_param_used_analyse(10)
        pprint(f"Used param by analysis ID: {hc_param}")

        # Returns the Hyperspectral plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the
        # tray was analyzed and by device defined by device ID
        hc_param = api.hc_param_used(1, 1, 1)
        pprint(f"Plant & leaf params by device, tray, round ID: {hc_param}")

        # Returns the Hyperspectral parameter image for the parameter defined by parameter ID and calculated in the analysis
        # defined by analyse ID
        hc_param = api.hc_param_image_analyse(1, 1)
        pprint(f"Analysis params for param and analysis ID: {hc_param}")

        # Returns the Hyperspectral parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round
        # in which the tray was analyzed and by device defined by device ID
        hc_param = api.hc_param_image(1, 1, 1, 1)
        pprint(f"Params by device, tray, round, param ID: {hc_param}")

        # Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID and calculated in
        # the analysis defined by analyse ID
        hc_param = api.hc_plant_param_analyse(1, 1)
        pprint(f"Plant params by parameter and analysis ID: {hc_param}")

        # Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by
        # round ID of round in which the tray was analyzed and by device defined by device ID
        hc_param = api.hc_plant_param(1, 1, 1, 1)
        pprint(f"Plant params by device, tray, round, param ID: {hc_param}")

        # Returns the Hyperspectral statistic leaf parameter values for the parameter defined by parameter ID and calculated in
        # the analysis defined by analyse ID
        hc_param = api.hc_leaf_param_analyse(1, 1)
        pprint(f"Leaf params by parameter and analysis ID: {hc_param}")

        # Returns the Hyperspectral Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by
        # round ID of round in which the tray was analyzed and by device defined by device ID
        hc_param = api.hc_leaf_param(1, 1, 1, 1)
        pprint(f"Leaf params by device, tray, round, param ID: {hc_param}")

        """-----------------------------------------------------------------------------------------------------------------
            Thermal
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns Thermal imaging data by measure ID
        ir_img = api.ir_imaging_measure(1)
        pprint(f"imaging information for measurement ID: {ir_img}")

        # Returns Thermal imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by
        # device defined by device ID
        ir_img = api.ir_imaging(1, 1, 1)
        pprint(f"imaging information for device, Round, tray ID: {ir_img}")

        # Returns Thermal imaging extended data by measure ID
        ir_ext_img = api.ir_imaging_extended_data_measure(1)
        pprint(f"imaging extended measurement info for measurement ID: {ir_ext_img}")

        # Returns Thermal extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by
        # device defined by device ID
        ir_ext_img = api.ir_imaging_extended_data(1, 1, 1)
        pprint(f"imaging extended measurement info for device, Round, tray ID: {ir_ext_img}")

        # Returns the Thermal plant mask created for the measured tray defined by measure ID
        ir_mask = api.ir_plant_mask_measure(1)
        pprint(f"Plant mask for measurement ID: {ir_mask}")

        # Returns Thermal plant masks created for the tray defined by tray ID, by round ID of round in which the tray was
        # measured and by device defined by device ID
        ir_mask = api.ir_plant_mask(1, 1, 1)
        pprint(f"Plant mask for device, Round, tray ID: {ir_mask}")

        # Returns Thermal imaging data masked by the plant mask defined by measure ID
        ir_imag = api.ir_plant_mask_image_measure(1)
        pprint(f"Masked Plant for measurement ID: {fc_mask}")

        # Returns Thermal imaging data masked by the plant mask for tray defined by tray ID, by round ID of round in which the
        # tray was measured and by device defined by device ID
        ir_imag = api.ir_plant_mask_image(1, 1, 1)
        pprint(f"Masked Plant for device, Round, tray ID: {fc_mask}")

        # Returns one Thermal parameter by parameter ID
        ir_param = api.ir_param(1)
        pprint(f"Param by param ID: {ir_param}")

        # Returns the Thermalplant and leaf parameters used in the analysis defined by analyse ID
        ir_param = api.ir_param_used_analyse(1)
        pprint(f"Used param by analysis ID: {ir_param}")

        # Returns the Thermal plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray
        # was analyzed and by device defined by device ID
        ir_param = api.ir_param_used(1, 1, 1)
        pprint(f"Plant & leaf params by device, tray, round ID: {ir_param}")

        # Returns the Thermal plant parameter values for the parameter defined by parameter ID and calculated in the analysis
        # defined by analyse ID
        ir_param = api.ir_plant_param_analyse(1, 1)
        pprint(f"Plant params by parameter and analysis ID: {ir_param}")

        # Returns the Thermal statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by
        # round ID of round in which the tray was analyzed and by device defined by device ID
        ir_param = api.ir_plant_param(1, 1, 1, 1)
        pprint(f"Params by device, tray, round, param ID: {ir_param}")

        # Returns the Thermal statistic leaf parameter values for the parameter defined by parameter ID and calculated in the
        # analysis defined by analyse ID
        ir_param = api.ir_leaf_param_analyse(1, 1)
        pprint(f"Leaf params by parameter and analysis ID: {ir_param}")

        # Returns the Thermal Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by
        # round ID of round in which the tray was analyzed and by device defined by device ID
        ir_param = api.ir_leaf_param(1, 1, 1, 1)
        pprint(f"Leaf params by device, tray, round, param ID: {ir_param}")

        """-----------------------------------------------------------------------------------------------------------------
            Multispectral
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns Multispectral imaging data by measure ID
        msc_img = api.msc_imaging_measure(1)
        pprint(f"imaging information for measurement ID: {msc_img}")

        # Returns Multispectral imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and
        # by device defined by device ID
        msc_img = api.msc_imaging(1, 1, 1)
        pprint(f"imaging information for device, Round, tray ID: {msc_img}")

        # Returns Multispectral imaging extended data by HC measure ID
        msc_ext_img = api.hc_imaging_extended_data_measure(200)
        pprint(f"imaging extended measurement info for measurement ID: {msc_ext_img}")

        # Returns Multispectral extended data for tray defined by tray ID, by round ID of round in which the tray was measured
        # and by device defined by device ID
        msc_ext_img = api.hc_imaging_extended_data(1, 1, 1)
        pprint(f"imaging extended measurement info for device, Round, tray ID: {msc_ext_img}")

        # Returns the Multispectral plant mask created for the measured tray defined by HC measure ID
        msc_mask = api.msc_plant_mask_measure(200)
        pprint(f"Plant mask for measurement ID: {msc_mask}")

        # Returns Multispectral plant masks created for the tray defined by tray ID, by round ID of round in which the tray was
        # measured and by device defined by device ID
        msc_mask = api.msc_plant_mask(1, 1, 1)
        pprint(f"Plant mask for device, Round, tray ID: {msc_mask}")

        # Returns one Multispectral parameter by parameter ID
        msc_param = api.msc_param(10)
        pprint(f"Param by param ID: {msc_param}")

        # Returns the Multispectral plant and leaf parameters used in the analysis defined by analyse ID
        msc_param = api.msc_param_used_analyse(10)
        pprint(f"Used param by analysis ID: {msc_param}")

        # Returns the Multispectral plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the
        # tray was analyzed and by device defined by device ID
        msc_param = api.msc_param_used(1, 1, 1)
        pprint(f"Plant & leaf params by device, tray, round ID: {msc_param}")

        # Returns the Multispectral parameter image for the parameter defined by parameter ID and calculated in the analysis
        # defined by analyse ID
        msc_param = api.msc_param_image_analyse(1, 1)
        pprint(f"Analysis params for param and analysis ID: {msc_param}")

        # Returns the Multispectral parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round
        # in which the tray was analyzed and by device defined by device ID
        msc_param = api.msc_param_image(1, 1, 1, 1)
        pprint(f"Params by device, tray, round, param ID: {msc_param}")

        # Returns the Multispectral statistic plant parameter values for the parameter defined by parameter ID and calculated in
        # the analysis defined by analyse ID
        msc_param = api.msc_plant_param_analyse(1, 1)
        pprint(f"Plant params by parameter and analysis ID: {msc_param}")

        # Returns the Multispectral statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by
        # round ID of round in which the tray was analyzed and by device defined by device ID
        msc_param = api.msc_plant_param(1, 1, 1, 1)
        pprint(f"Plant params by device, tray, round, param ID: {msc_param}")

        # Returns the Multispectral statistic leaf parameter values for the parameter defined by parameter ID and calculated in
        # the analysis defined by analyse ID
        msc_param = api.msc_leaf_param_analyse(1, 1)
        pprint(f"Leaf params by parameter and analysis ID: {msc_param}")

        # Returns the Multispectral Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by
        # round ID of round in which the tray was analyzed and by device defined by device ID
        msc_param = api.msc_leaf_param(1, 1, 1, 1)
        pprint(f"Leaf params by device, tray, round, param ID: {msc_param}")

        # Returns the Multispectral lightset by ID
        msc_lightset = api.msc_light_set(1)
        pprint(f"Lightset by ID: {msc_lightset}")

        # Returns Multispectral lightset used by tray ID, by round ID of round in which the tray was measured and
        # by device defined by device ID
        msc_lightset = api.msc_light_set_used(1, 1, 1)
        pprint(f"Lightset for device, Round, tray ID: {msc_lightset}")

        # Returns the Multispectral calibration by ID
        msc_lightset = api.msc_light_set(1)
        pprint(f"Calibration by ID: {msc_lightset}")

        # Returns the Multispectral calibration by device, round and tray
        msc_lightset = api.msc_light_set_used(1, 1, 1)
        pprint(f"Calibration by lightset ID: {msc_lightset}")

        # Returns all Multispectral calibration lightsettings
        msc_lightset = api.msc_calibration_light()
        pprint(f"Calibration lightsettings: {msc_lightset}")

        # Returns all Multispectral calibration lightsettings by calibration ID
        msc_lightset = api.msc_calibration_light(1)
        pprint(f"Calibration lightsettings by calibration ID: {msc_lightset}")
        """-----------------------------------------------------------------------------------------------------------------
            RGB
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns RGB imaging data by measure ID
        rgb_img = api.rgb_imaging_measure(1)
        pprint(f"imaging information for measurement ID: {rgb_img}")

        # Returns RGB imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by
        # device defined by device ID
        rgb_img = api.rgb_imaging(1, 1, 1)
        pprint(f"imaging information for device, Round, tray ID: {rgb_img}")

        # Returns RGB imaging extended data by measure ID
        rgb_ext_img = api.rgb_imaging_extended_data_measure(1)
        pprint(f"imaging extended measurement info for measurement ID: {rgb_ext_img}")

        # Returns RGB extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by
        # device defined by device ID
        rgb_ext_img = api.rgb_imaging_extended_data(1, 1, 1)
        pprint(f"imaging extended measurement info for device, Round, tray ID: {rgb_ext_img}")

        # Returns the RGB plant mask created for the measured tray defined by measure ID
        rgb_mask = api.rgb_plant_mask_measure(1)
        pprint(f"Plant mask for measurement ID: {rgb_mask}")

        # Returns RGB plant masks created for the tray defined by tray ID, by round ID of round in which the tray was
        # measured and by device defined by device ID
        rgb_mask = api.rgb_plant_mask(1, 1, 1)
        pprint(f"Plant mask for device, Round, tray ID: {rgb_mask}")

        # Returns the RGB greening plant mask created for the measured tray defined by measure ID
        rgb_greening_mask = api.rgb_greening_mask_image_measure(1)
        pprint(f"Greening plant mask for measurement ID: {rgb_greening_mask}")

        # Returns RGB greening plant masks created for the tray defined by tray ID, by round ID of round in which the tray was
        # measured and by device defined by device ID
        rgb_greening_mask = api.rgb_greening_mask_image(1, 1, 1)
        pprint(f"Plant mask for device, Round, tray ID: {rgb_greening_mask}")

        # Returns one RGB parameter by parameter ID
        rgb_param = api.rgb_param(1)
        pprint(f"Param by param ID: {rgb_param}")

        # Returns the RGB plant and leaf parameters used in the analysis defined by analyse ID
        rgb_param = api.rgb_param_used_analyse(1)
        pprint(f"Used param by analysis ID: {rgb_param}")

        # Returns the RGB plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray
        # was analyzed and by device defined by device ID
        rgb_param = api.rgb_param_used(1, 1, 1)
        pprint(f"Plant & leaf params by device, tray, round ID: {rgb_param}")

        # Returns the greening plant and leaf parameters used in the analysis defined by analyse ID
        rgb_param = api.rgb_param_color_used_analyse(1)
        pprint(f"Used greening param by analysis ID: {rgb_param}")

        # Returns the greening plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray
        # was analyzed and by device defined by device ID
        rgb_param = api.rgb_param_color_used(1, 1, 1)
        pprint(f"Greening params by device, tray, round ID: {rgb_param}")

        # Returns the RGB plant parameter values for the parameter defined by parameter ID and calculated in the analysis
        # defined by analyse ID
        rgb_param = api.rgb_plant_param_analyse(1, 1)
        pprint(f"Plant params by parameter and analysis ID: {rgb_param}")

        # Returns the RGB plant parameter values for the parameter defined by parameter ID, by tray ID, by
        # round ID of round in which the tray was analyzed and by device defined by device ID
        rgb_param = api.rgb_plant_param(1, 1, 1, 1)
        pprint(f"Params by device, tray, round, param ID: {rgb_param}")

        # Returns the RGB greening plant parameter values for the parameter defined by parameter ID and calculated in the analysis
        # defined by analyse ID
        rgb_param = api.rgb_plant_param_color_analyse(1, 1)
        pprint(f"Plant params by parameter and analysis ID: {rgb_param}")

        # Returns the RGB greening plant parameter values for the parameter defined by parameter ID, by tray ID, by
        # round ID of round in which the tray was analyzed and by device defined by device ID
        rgb_param = api.rgb_plant_param_color(1, 1, 1, 1)
        pprint(f"Plant params by device, tray, round, param ID: {rgb_param}")

        # Returns the RGB leaf parameter values for the parameter defined by parameter ID and calculated in the analysis
        # defined by analyse ID
        rgb_param = api.rgb_leaf_param_analyse(1, 1)
        pprint(f"Leaf params by parameter and analysis ID: {rgb_param}")

        # Returns the RGB leaf parameter values for the parameter defined by parameter ID, by tray ID, by
        # round ID of round in which the tray was analyzed and by device defined by device ID
        rgb_param = api.rgb_leaf_param(1, 1, 1, 1)
        pprint(f"Leaf Params by device, tray, round, param ID: {rgb_param}")

        # Returns the RGB greening leaf parameter values for the parameter defined by parameter ID and calculated in the analysis
        # defined by analyse ID
        rgb_param = api.rgb_leaf_param_color_analyse(1, 1)
        pprint(f"Leaf params by parameter and analysis ID: {rgb_param}")

        # Returns the RGB greening leaf parameter values for the parameter defined by parameter ID, by tray ID, by
        # round ID of round in which the tray was analyzed and by device defined by device ID
        rgb_param = api.rgb_leaf_param_color(1, 1, 1, 1)
        pprint(f"Leaf params by device, tray, round, param ID: {rgb_param}")

        """-----------------------------------------------------------------------------------------------------------------
            3D
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns 3D scanning imaging data by measure ID
        scan3d_img = api.scan3d_imaging_measure(1)
        pprint(f"imaging information for measurement ID: {scan3d_img}")

        # Returns 3D scanning imaging data for tray defined by tray ID, by round ID of round in which the tray was measured and by
        # device defined by device ID
        scan3d_img = api.scan3d(1, 1, 1)
        pprint(f"imaging information for device, Round, tray ID: {scan3d_img}")

        # Returns 3D scanning imaging extended data by measure ID
        scan3d_ext_img = api.scan3d_imaging_extended_data_measure(1)
        pprint(f"imaging extended measurement info for measurement ID: {scan3d_ext_img}")

        # Returns 3D scanning extended data for tray defined by tray ID, by round ID of round in which the tray was measured and by
        # device defined by device ID
        scan3d_ext_img = api.scan3d_imaging_extended_data(1, 1, 1)
        pprint(f"imaging extended measurement info for device, Round, tray ID: {scan3d_ext_img}")

        # Returns 3D scanning analysed 3D data for the measured tray defined by measure ID
        scan_3d_model = api.scan3d_analyzed_model_measure(1)
        pprint(f"Analyzed model for measurement ID: {scan_3d_model}")

        # Returns 3D scanning analysed 3D data for the measured tray defined by analysis ID
        scan_3d_model = api.scan3d_analyzed_model_analyse(1)
        pprint(f"Analyzed model for analysis ID: {scan_3d_model}")

        # Returns 3D scanning analysed 3D data for tray defined by tray ID, by round ID of round in which the tray was measured and by
        # device defined by device ID
        scan_3d_model = api.scan3d_analyzed_model(1, 1, 1)
        pprint(f"Analyzed model for device, tray, round: {scan_3d_model}")

        # Returns one 3D scanning parameter by parameter ID
        scan3d_param = api.scan3d_param(1)
        pprint(f"Param by param ID: {scan3d_param}")

        # Returns the 3D scanning plant and leaf parameters used in the analysis defined by analyse ID
        scan3d_param = api.scan3d_param_used_analyse(1)
        pprint(f"Used param by analysis ID: {scan3d_param}")

        # Returns the 3D scanning plant and leaf parameters used in the analysis by tray ID, by round ID of round in which the tray
        # was analyzed and by device defined by device ID
        ir_param = api.scan3d_param_used(1, 1, 1)
        pprint(f"Plant & leaf params by device, tray, round ID: {scan3d_param}")

        # Returns the 3D scanning plant parameter values for the parameter defined by parameter ID and calculated in the analysis
        # defined by analyse ID
        scan3d_param = api.scan3d_plant_param_analyse(1, 1)
        pprint(f"Plant params by parameter and analysis ID: {scan3d_param}")

        # Returns the 3D scanning plant parameter values for the parameter defined by parameter ID, by tray ID, by
        # round ID of round in which the tray was analyzed and by device defined by device ID
        scan3d_param = api.scan3d_plant_param(1, 1, 1, 1)
        pprint(f"Params by device, tray, round, param ID: {scan3d_param}")

        # Returns the 3D scanning leaf parameter values for the parameter defined by parameter ID and calculated in the
        # analysis defined by analyse ID
        scan3d_param = api.scan3d_leaf_param_analyse(1, 1)
        pprint(f"Leaf params by parameter and analysis ID: {scan3d_param}")

        # Returns the 3D scanning leaf parameter values for the parameter defined by parameter ID, by tray ID, by
        # round ID of round in which the tray was analyzed and by device defined by device ID
        scan3d_param = api.scan3d_leaf_param(1, 1, 1, 1)
        pprint(f"Leaf params by device, tray, round, param ID: {scan3d_param}")

        """-----------------------------------------------------------------------------------------------------------------
            Spray
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns spray action data for the given device, tray, round ID
        spray_act = api.spray_action(1, 1, 1)
        pprint(f"Spray action by device, tray, round ID: {spray_act}")

        """-----------------------------------------------------------------------------------------------------------------
            Probe
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns all probes
        api_response = api.probe()
        pprint(f"Probe list: {api_response}")

        # Returns one probes by ID
        api_response = api.probe(5)
        pprint(f"Probe by ID: {api_response}")

        # Returns all probe values measured between times
        start = datetime.datetime(year=2023, month=9, day=1, hour=1)
        stop = datetime.datetime(year=2023, month=9, day=1, hour=2)
        probe_value_list = api.probe_value_date(start, stop)
        pprint(f"All probe values between {start} and {stop}: {probe_value_list}")

        # Returns all probe values for probe defined by probe ID measured between times
        start = datetime.datetime(year=2023, month=9, day=1, hour=1)
        stop = datetime.datetime(year=2023, month=9, day=1, hour=2)
        probe_values = api.probe_value_date_probe(8, start, stop)
        pprint(f"All probe values for probe ID between {start} and {stop}: {probe_value_list}")

        """-----------------------------------------------------------------------------------------------------------------
            Spectrum Device
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns all spectrum devices
        api_response = api.spectrum_device_id()
        pprint(f"Spectrum device list: {api_response}")

        # Returns spectrum device by ID
        spectrum_device_list = api.spectrum_device(1)
        pprint(f"Spectrum device by ID: {spectrum_device_list}")

        # Returns spectrum device values by ID between times
        start = datetime.datetime(year=2023, month=9, day=1, hour=1)
        stop = datetime.datetime(year=2023, month=9, day=1, hour=2)
        spectrum_device_value_list = api.spectrum_values_date_device(1, start, stop)
        pprint(f"All spectrum device values for device ID between {start} and {stop}: {spectrum_device_value_list}")

        """-----------------------------------------------------------------------------------------------------------------
            Buffer
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns buffer state by id
        buf_state = api.buffer_history(1)
        pprint(f"Buffer state: {buf_state}")

        # Returns buffer state in period
        start = datetime.datetime(year=2023, month=9, day=1, hour=1)
        stop = datetime.datetime(year=2023, month=9, day=1, hour=2)
        buf_state = api.buffer_history_date(start, stop)
        pprint(f"Buffer state between {start} and {stop}: {buf_state}")

        """-----------------------------------------------------------------------------------------------------------------
            system Log
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns Logs for round
        logs = api.system_log_round(1)
        pprint(f"Logs for round: {logs}")

        # Returns Logs for round during period
        start = datetime.datetime(year=2023, month=9, day=1, hour=1)
        stop = datetime.datetime(year=2023, month=9, day=1, hour=2)
        logs = api.system_log_date_round(1, start, stop)
        pprint(f"Logs for round between {start} and {stop}:  {logs}")

        # Returns Logs for tray
        logs = api.system_log_tray(1)
        pprint(f"Logs for tray: {logs}")

        # Returns Logs for tray during period
        start = datetime.datetime(year=2023, month=9, day=1, hour=1)
        stop = datetime.datetime(year=2023, month=9, day=1, hour=2)
        logs = api.system_log_date_tray(1, start, stop)
        pprint(f"Logs for tray between {start} and {stop}: {logs}")

        # Returns Log types
        log_types = api.system_log_log_type()
        pprint(f"Logs types: {log_types}")

        # Returns Log types during period
        start = datetime.datetime(year=2023, month=9, day=1, hour=1)
        stop = datetime.datetime(year=2023, month=9, day=1, hour=2)
        log_types = api.system_log_date_log_type("1", start, stop)
        pprint(f"Logs for round: {log_types}")

        # Returns Log tags
        log_tags = api.system_log_log_tag()
        pprint(f"Logs tags: {log_tags}")

        # Returns Log types during period
        start = datetime.datetime(year=2023, month=9, day=1, hour=1)
        stop = datetime.datetime(year=2023, month=9, day=1, hour=2)
        log_tags = api.system_log_date_log_tag("1", start, stop)
        pprint(f"Logs for round: {log_tags}")

        """-----------------------------------------------------------------------------------------------------------------
            Version Info
        ---------------------------------------------------------------------------------------------------------------------
        """
        # Returns version info
        api_response = api.version_info()
        pprint(f"Version info: {api_response}")

        # Returns the changelog
        string = api.version_info()
        print(f"Changelog: {string}")

    except ApiException as e:
        print(traceback.format_exc())
        print("Exception: %s\n" % e)
