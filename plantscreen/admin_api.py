import plantscreen.swagger_client as swagger_client
import plantscreen.models as models
from typing import List


class AdminAPI():
    """ Wrapper around the automatically  generated swagger client.
       return class instances instead of dictionaries """
    def __init__(self, server, poort):
        """ Initialises the API connection

        Args:
            server (str): Server url
            poort (str): Poort number

        Return:
            AdminAPI instance """
        configuration = swagger_client.Configuration()
        configuration.host = f'{server}:{poort}/RestService/json'
        self.exp_api = swagger_client.ExperimentApi(swagger_client.ApiClient(configuration))
        self.round_api = swagger_client.RoundApi(swagger_client.ApiClient(configuration))
        self.action_api = swagger_client.ActionApi(swagger_client.ApiClient(configuration))
        self.device_api = swagger_client.DeviceApi(swagger_client.ApiClient(configuration))
        self.profile_api = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
        self.tray_api = swagger_client.TrayApi(swagger_client.ApiClient(configuration))
        self.plant_api = swagger_client.PlantApi(swagger_client.ApiClient(configuration))
        self.buffer_api = swagger_client.BufferApi(swagger_client.ApiClient(configuration))
        self.system_log_api = swagger_client.SystemLogApi(swagger_client.ApiClient(configuration))
        self.file_api = swagger_client.FileApi(swagger_client.ApiClient(configuration))
        self.version_info_api = swagger_client.VersionInfoApi(swagger_client.ApiClient(configuration))

    def experimentID(self) -> List[int]:
        """ Returns a list of all experiment IDs in the database

        Return:
            List[int] """
        api_response = self.exp_api.experiment_id()
        return models.experiment.ExperimentIDs.from_dict(api_response.to_dict())

    def experiment(self, exp_id: int) -> swagger_client.Experiment:
        """ Returns one experiment by experiment ID

        Args:
            exp_id (int): Experiment ID

        Return:
            swagger_client.Experiment """
        api_response = self.exp_api.experiment(exp_id)
        return api_response.json_experiment_result

    def experiment_date(self, start: str, stop: str) -> List[swagger_client.Experiment]:
        """ Returns all experiments whose rounds took place between defined times.
        Times is entered as the start and end time of the required interval.
        All experiments with at least one round between these times will be returned

        Args:
            start (string): Startdate
            stop (string): Stopdate

        Return:
            List[swagger_client.Experiment] """
        api_response = self.exp_api.experiment_date(start, stop)
        return api_response.json_experiment_by_date_result

    def experiment_owner(self, owner_id: int) -> List[swagger_client.Experiment]:
        """ Returns all experiments that belong to the user defined by ID

        Args:
            owner_id (int): Owner ID

        Return:
            List[swagger_client.Experiment] """
        api_response = self.exp_api.experiment_owner(owner_id)
        return api_response.json_experiment_by_owner_result

    def owner_id(self) -> List[int]:
        """ Returns a list of all experiment owner IDs in the database

        Return:
            List[int] """
        api_response = self.exp_api.owner_id()
        return models.experiment.OwnerID.from_dict(api_response.to_dict())

    def owner(self, exp_ids: List[int]) -> List[swagger_client.Owner]:
        """ Returns the owner(s) of the experiment by ID

        Args:
            exp_ids (List(int)): List of experiment IDs

        Return:
            List[swagger_client.Owner] """
        api_response = self.exp_api.owner(exp_ids)
        return api_response.json_owner_result

    def note_experiment(self, exp_id: int) -> List[swagger_client.ExperimentNote]:
        """ Returns the experiment notes that the user saved for the experiment defined by ID

        Args:
            exp_id (int): Experiment ID

        Return:
            List[swagger_client.ExperimentNote] """
        api_response = self.exp_api.note_experiment(exp_id)
        return api_response.json_note_result

# Round API
    def round(self, round_id: int) -> swagger_client.Round:
        """ Returns one round by round ID

        Args:
            round_id (int): Round ID

        Return:
            swagger_client.Round """
        api_response = self.round_api.round(round_id)
        return api_response.json_round_result

    def round_experiment(self, exp_id: int) -> List[swagger_client.Round]:
        """ Returns all rounds measured in the experiment defined by ID

        Args:
            exp_id (int): Experiment ID

        Return:
            List[swagger_client.Round] """
        api_response = self.round_api.round_experiment(exp_id)
        return api_response.json_round_by_experiment_id_result

    def round_date_experiment(self, exp_id: str, start: str, stop: str) -> List[swagger_client.Round]:
        """ Returns all rounds measured in the experiment defined by ID between defined times.
        Times is entered as the start and end time of the required interval

        Args:
            exp_id (int): Experiment ID
            start (str): Startdate
            stop (str): Stopdate

        Return:
            List[swagger_client.Round] """
        api_response = self.round_api.round_date_experiment(exp_id, start, stop)
        return api_response.json_round_by_experiment_id_and_date_result

    def round_order_round(self, round_id: int) -> swagger_client.RoundOrder:
        """ Returns the round order in the experiment by round ID

        Args:
            round_id (int): Round ID

        Return:
            swagger_client.RoundOrder """
        api_response = self.round_api.round_order_round(round_id)
        return api_response.json_round_order_result

    def round_order_experiment(self, exp_id: int) -> List[swagger_client.RoundOrder]:
        """ Returns all rounds measured in the experiment defined by ID

        Args:
            exp_id (int): Experiment ID

        Return:
            List[swagger_client.RoundOrder] """
        api_response = self.round_api.round_order_experiment(exp_id)
        return api_response.json_round_order_by_experiment_id_result

    def round_order_date_experiment(self, exp_id: int, start: str, stop: str) -> List[swagger_client.RoundOrder]:
        """ Returns all rounds measured in the experiment defined by ID

        Args:
            exp_id (int): Experiment ID
            start (str): Startdate
            stop (str): Stopdate

        Return:
            List[swagger_client.RoundOrder] """
        api_response = self.round_api.round_order_date_experiment(exp_id, start, stop)
        return api_response.json_round_order_by_experiment_id_and_date_result

# Action API
    def action(self, action_id: int) -> swagger_client.Action:
        """ Returns one scheduled action by action ID

        Args:
            action_id (int): Action ID

        Return:
            swagger_client.Action """
        api_response = self.action_api.action(action_id)
        return api_response.json_action_result

    def action_experiment(self, exp_id: int) -> List[swagger_client.Action]:
        """ Returns all scheduled actions in the experiment defined by ID

        Args:
            exp_id (int): Experiment ID

        Return:
            List[swagger_client.Action] """
        api_response = self.action_api.action_experiment(exp_id)
        return api_response.json_action_by_experiment_id_result

    def action_not_done_experiment(self, exp_id: int) -> List[swagger_client.Action]:
        """ Returns all unfinished scheduled actions (with pending and running action state)
        in the experiment defined by ID

        Args:
            exp_id (int): experiment ID

        Return:
            List[swagger_client.Action] """
        api_response = self.action_api.action_not_done_experiment(exp_id)
        return api_response.json_action_by_experiment_id_not_done_result

    def action_group(self, group_id: int) -> swagger_client.ActionGroup:
        """ Returns one group of scheduled actions by action group ID

        Args:
            group_id (int): Group ID

        Return:
            swagger_client.ActionGroup """
        api_response = self.action_api.action_group(group_id)
        return api_response.json_action_group_result

    def action_group_round(self, round_id: int) -> swagger_client.ActionGroup:
        """ Returns one group of scheduled actions to which a round defined by ID belongs

        Args:
            round_id (int): Round ID

        Return:
            swagger_client.ActionGroup """
        api_response = self.action_api.action_group_round(round_id)
        return api_response.json_action_group_by_round_id_result

    def action_protocol(self, prot_id: int) -> swagger_client.ActionProtocol:
        """ Returns one protocol of scheduled action by protocol ID

        Args:
            prot_id (int): Protocol ID

        Return:
            swagger_client.ActionProtocol """
        api_response = self.action_api.action_protocol(prot_id)
        return api_response.json_action_protocol_result

    def action_protocol_round(self, round_id: int) -> swagger_client.ActionProtocol:
        """ Returns one group of scheduled actions that belong to round defined by ID

        Args:
            round_id (int): Round ID

        Return:
            swagger_client.ActionProtocol """
        api_response = self.action_api.action_protocol_round(round_id)
        return api_response.json_action_protocol_by_round_id_result

# Device API
    def device(self, device_id: int) -> swagger_client.Device:
        """ Returns one device by device ID

        Args:
            device_id (int): Device ID

        Return:
            swagger_client.Device """
        api_response = self.device_api.device(device_id)
        return api_response.json_device_result

    def device_active(self) -> List[swagger_client.Device]:
        """ Returns all active devices that have not ended validity

        Return:
            List[swagger_client.Device] """
        api_response = self.device_api.device_active()
        return api_response.json_device_active_result

    def device_profile(self, prof_id: int) -> List[swagger_client.Device]:
        """ Returns all devices that contains the system profile defined by ID

        Args:
            prof_id (int): Profile ID

        Return:
            List[swagger_client.Device] """
        api_response = self.device_api.device_profile(prof_id)
        return api_response.json_device_by_profile_id_result

# Profile API
    def profile_id(self) -> List[int]:
        """ Returns a list of all system profile IDs in the database

        Return:
            List[int] """
        api_response = self.profile_api.profile_id()
        return models.profile_models.ProfileIDs.from_dict(api_response.to_dict())

    def profile(self, prof_id: int) -> swagger_client.SystemProfile:
        """ Returns one system profile by profile ID

        Args:
            prof_id (int): Profile ID

        Return:
            swagger_client.SystemProfile """
        api_response = self.profile_api.profile(prof_id)
        return api_response.json_system_profile_result

    def profile_active(self) -> swagger_client.SystemProfile:
        """ Returns the active system profile

        Return:
            swagger_client.SystemProfile """
        api_response = self.profile_api.profile_active()
        return api_response.json_system_profile_active_result

# Tray API
    def tray(self, tray_id: int) -> swagger_client.Tray:
        """ Returns one tray by tray ID

        Args:
            tray_id (int): Tray ID

        Return:
            swagger_client.Tray """
        api_response = self.tray_api.tray(tray_id)
        return api_response.json_tray_result

    def tray_round(self, round_id: int) -> List[swagger_client.Tray]:
        """ Returns all trays measured in the round defined by ID

        Args:
            round_id (int): Round ID

        Return:
            List[swagger_client.Tray] """
        api_response = self.tray_api.tray_round(round_id)
        return api_response.json_tray_by_round_id_result

    def tray_type(self, tray_id: int) -> swagger_client.TrayType:
        """ Returns one tray type by tray type ID

        Args:
            tray_id (int): Tray ID

        Return:
            swagger_client.TrayType """
        api_response = self.tray_api.tray_type(tray_id)
        return api_response.json_tray_type_result

    def tray_type_tray(self, tray_id: int) -> swagger_client.TrayType:
        """ Returns one tray type which is assigned to the tray defined by ID

        Args:
            tray_id (int): Tray ID

        Return:
            swagger_client.TrayType """
        api_response = self.tray_api.tray_type_tray(tray_id)
        return api_response.json_tray_type_by_tray_id_result

    def tray_type_tray_profile(self, tray_prof_id: int) -> swagger_client.TrayType:
        """ Returns one tray type which is assigned to the tray profile defined by ID

        Args:
            tray_prof_id (int): Tray profile ID

        Return:
            swagger_client.TrayType """
        api_response = self.tray_api.tray_type_tray_profile(tray_prof_id)
        return api_response.json_tray_type_by_tray_profile_id_result

    def tray_profile(self, prof_id: int) -> swagger_client.TrayProfile:
        """ Returns one tray profile by tray profile ID

        Args:
            prof_id (int): Profile ID

        Return:
            swagger_client.TrayProfile """
        api_response = self.tray_api.tray_profile(prof_id)
        return api_response.json_tray_profile_by_id_result

    def tray_profile_tray(self, tray_id: int) -> swagger_client.TrayProfile:
        """ Returns one tray profile to which tray defined by ID is assigned

        Args:
            tray_id (int): Tray ID

        Return:
            swagger_client.TrayProfile """
        api_response = self.tray_api.tray_profile_tray(tray_id)
        return api_response.json_tray_profile_by_tray_id_result

    def tray_profile_used_tray(self, tray_id: int, start: str, stop: str) -> List[swagger_client.TrayProfile]:
        """ Returns tray profiles to which tray defined by ID was assigned between defined times.
        Times is entered as the start and end time of the required interval.
        All tray profiles assigned to tray between these times will be returned

        Args:
            tray_id (int): Tray ID
            start (string): Startdate
            stop (string): Stopdate

        Return:
            List[swagger_client.TrayProfile] """
        api_response = self.tray_api.tray_profile_used_tray(tray_id, start, stop)
        return api_response.json_used_tray_profile_by_tray_id_result

    def tray_profile_to_date_tray(self, tray_id: int, date: str) -> swagger_client.TrayProfile:
        """ Returns one tray profile to which tray defined by ID was assigned on the defined time

        Args:
            tray_id (int): Tray ID
            date (string): Timestamp

        Return:
            swagger_client.TrayProfile """
        api_response = self.tray_api.tray_profile_to_date_tray(tray_id, date)
        return api_response.json_tray_profile_by_tray_idto_date_result

    def scales_mapping_tray(self, tray_id: int) -> List[swagger_client.ScalesMapping]:
        """ Returns tray profiles to which tray defined by ID was assigned between defined times.
        Times is entered as the start and end time of the required interval.
        All tray profiles assigned to tray between these times will be returned

        Args:
            tray_id (int): Tray ID

        Return:
            List[swagger_client.ScalesMapping] """
        api_response = self.tray_api.scales_mapping_tray(tray_id)
        return api_response.json_scales_mapping_by_tray_id_result

# Plant API
    def plant(self, plant_ids: List[int]) -> List[swagger_client.Plant]:
        """ Returns a list of plants by the list of plant IDs

        Args:
            plant_ids (List[int]): plant IDs

        Return:
            List[swagger_client.Plant] """
        api_response = self.plant_api.plant(plant_ids)
        return api_response.json_plant_result

    def plant_tray(self, tray_id: int) -> List[swagger_client.Plant]:
        """ Returns list of plants which are assigned to the tray defined by ID

        Args:
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Plant] """
        api_response = self.plant_api.plant_tray(tray_id)
        return api_response.json_plant_by_tray_id_result

    def plant_tray_profile_tray(self, tray_id: int, start: str, stop: str) -> List[swagger_client.Plant]:
        """ Returns plants that were assigned to the tray defined by tray ID between defined times.
        Times is entered as the start and end time of the required interval.
        All plants assigned to tray between these times will be returned

        Args:
            tray_id (int): Tray ID
            start (string): Startdate
            stop (string): Stopdate

        Return:
            List[swagger_client.Plant] """
        api_response = self.plant_api.plant_tray_profile_tray(tray_id, start, stop)
        return api_response.json_plant_by_tray_id_and_dates_result

    def plant_tray_profile(self, tray_prof_id: int) -> List[swagger_client.Plant]:
        """ Returns plants that were assigned to the tray profile defined by tray profile ID without time limit

        Args:
            tray_prof_id (int): Tray profile ID

        Return:
            List[swagger_client.Plant] """
        api_response = self.plant_api.plant_tray_profile(tray_prof_id)
        return api_response.json_plant_by_tray_profile_id_result

    def plant_height_round(self, round_id: int) -> List[swagger_client.PlantHeight]:
        """ Returns all plant heights measured in the round defined by ID

        Args:
            round_id (int): Round ID

        Return:
            List[swagger_client.PlantHeight] """
        api_response = self.plant_api.plant_height_round(round_id)
        return api_response.json_plant_height_by_round_id_result

    def plant_leaf(self, plant_id: int, tray_id: int) -> List[swagger_client.PlantLeaf]:
        """ Returns all plant heights measured in the round defined by ID

        Args:
            plant_id (int): Plant ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.PlantLeaf] """
        api_response = self.plant_api.plant_leaf(plant_id, tray_id)
        return api_response.json_plant_leaves_by_plant_and_tray_id_result

# Buffer API
    def buffer_history(self, buff_id: int) -> swagger_client.BufferHistory:
        """ Returns one buffer history state defined by buffer state ID

        Args:
            buff_id (int): Buffer state ID

        Return:
            swagger_client.BufferHistory """
        api_response = self.buffer_api.buffer_history(buff_id)
        return api_response.json_buffer_history_result

    def buffer_history_date(self, start: str, stop: str) -> List[swagger_client.BufferHistory]:
        """ Returns buffer history states between times.
        Times is entered as the start and end time of the required interval.

        Args:
            start (string): Startdate
            stop (string): Stopdate

        Return:
            List[swagger_client.BufferHistory] """
        api_response = self.buffer_api.buffer_history_date(start, stop)
        return api_response.json_buffer_history_by_date_result

# System Log API
    def system_log_round(self, round_id: int) -> List[swagger_client.SystemLog]:
        """ Returns important events as system logs by round ID. System logs are only optionally assigned to the round

        Args:
            round_id (int): Round ID

        Return:
            List[swagger_client.SystemLog] """
        api_response = self.system_log_api.system_log_round(round_id)
        return api_response.json_system_log_by_round_id_result

    def system_log_date_round(self, round_id: int, start: str, stop: str) -> List[swagger_client.SystemLog]:
        """ Returns important events as system logs by round ID between defined times.
        Times is entered as the start and end time of the required interval.
        System logs are only optionally assigned to the round

        Args:
            round_id (int): Round ID
            start (str): Startdate
            stop (str): Stopdate

        Return:
            List[swagger_client.SystemLog]
        """
        api_response = self.system_log_api.system_log_date_round(round_id, start, stop)
        return api_response.json_system_log_by_round_id_and_date_result

    def system_log_tray(self, tray_id: int) -> List[swagger_client.SystemLog]:
        """ Returns important events as system logs by tray ID.
        System logs are only optionally assigned to the tray

        Args:
            tray_id (int): Tray ID

        Return:
            List[swagger_client.SystemLog]
        """
        api_response = self.system_log_api.system_log_tray(tray_id)
        return api_response.json_system_log_by_tray_id_result

    def system_log_date_tray(self, tray_id: int, start: str, stop: str) -> List[swagger_client.SystemLog]:
        """ Returns important events as system logs by tray ID between defined times.
        Times is entered as the start and end time of the required interval.
        System logs are only optionally assigned to the tray

        Args:
            tray_id (int): Tray ID
            start (str): Startdate
            stop (str): Stopdate

        Return:
            List[swagger_client.SystemLog]
        """
        api_response = self.system_log_api.system_log_date_tray(tray_id, start, stop)
        return api_response.json_system_log_by_tray_id_and_date_result

    def system_log_type(self) -> List[swagger_client.LogType]:
        """ Returns a list of all used system log types

        Return:
            List[swagger_client.LogType]
        """
        api_response = self.system_log_api.system_log_log_type()
        return api_response.json_system_log_type_result

    def system_log_date_log_type(self, type: str, start: str, stop: str) -> List[swagger_client.SystemLog]:
        """ Returns important events as system logs by log type between defined times.
        Times is entered as the start and end time of the required interval

        Args:
            type (int): Log type
            start (str): Startdate
            stop (str): Stopdate

        Return:
            List[swagger_client.SystemLog]
        """
        api_response = self.system_log_api.system_log_date_log_type(type, start, stop)
        return api_response.json_system_log_by_log_type_and_date_result

    def system_log_tag(self) -> List[swagger_client.LogTag]:
        """ Returns a list of all used system log tag

        Return:
            List[swagger_client.LogTag]
        """
        api_response = self.system_log_api.system_log_log_tag()
        return api_response.json_system_log_tag_result

    def system_log_date_log_tag(self, tag: str, start: str, stop: str) -> List[swagger_client.SystemLog]:
        """ Returns a list of all used system log tag

        Args:
            tag (str): Log tag
            start (str): Startdate
            stop (str): Stopdate

        Return:
            List[swagger_client.SystemLog]
        """
        api_response = self.system_log_api.system_log_date_log_tag(tag, start, stop)
        return api_response.json_system_log_by_log_tag_and_date_result

# Version Info API
    def version_info(self) -> swagger_client.VersionInfo:
        """ Returns version of the database and the PlantScreen Data REST API used

        Return:
            swagger_client.VersionInfo
        """
        api_response = self.version_info_api.version_info()
        return api_response.json_version_info_result
