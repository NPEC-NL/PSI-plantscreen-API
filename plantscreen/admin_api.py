import plantscreen.swagger_client as swagger_client
import plantscreen.models as models
from typing import List


class AdminAPI():
    """ Wrapper around the automatically  generated swagger client.
       return class instances instead of dictionaries """
    def __init__(self, server, poort):
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
        """ returns a list of all experiment IDs in the database

        Args:
            -

        Return:
            List[int] """
        api_response = self.exp_api.experiment_id()
        reply = models.experiment.ExperimentIDs.from_dict(api_response.to_dict())
        return reply

    def experiment(self, exp_id: int) -> swagger_client.Experiment:
        """ returns one experiment by experiment ID

        Args:
            exp_id (int): Experiment ID

        Return:
            swagger_client.Experiment """
        api_response = self.exp_api.experiment(exp_id)
        return api_response.json_experiment_result

    def experiment_date(self, start: str, stop: str) -> List[swagger_client.Experiment]:
        """ returns all experiments whose rounds took place between defined times.
        Times is entered as the start and end time of the required interval.
        All experiments with at least one round between these times will be returned

        Args:
            start (string): Startdate
            stop (string): Stopdate

        Return:
            List[swagger_client.Experiment] """
        api_response = self.exp_api.experiment_date(start, stop)
        if api_response.JsonExperimentByDateResult is None:
            return []
        else:
            return api_response.JsonExperimentByDateResult

    def experiment_owner(self, owner_id: int) -> List[swagger_client.Experiment]:
        """ returns all experiments that belong to the user defined by ID

        Args:
            owner_id (int): Owner ID

        Return:
            List[swagger_client.Experiment] """
        api_response = self.exp_api.experiment_owner(owner_id)
        if api_response.JsonExperimentByOwnerResult is None:
            return []
        else:
            return api_response.JsonExperimentByOwnerResult

    def owner_id(self) -> List[int]:
        """ returns a list of all experiment owner IDs in the database

        Args:
            -

        Return:
            List[int] """
        api_response = self.exp_api.owner_id()
        return models.experiment.OwnerID.from_dict(api_response.to_dict())

    def owner(self, exp_ids: List[int]) -> List[swagger_client.Owner]:
        """ returns the owner(s) of the experiment by ID

        Args:
            exp_ids (List(int)): List of experiment IDs

        Return:
            List[swagger_client.Owner] """
        api_response = self.exp_api.owner(exp_ids)
        if api_response.JsonOwnerResult is None:
            return []
        else:
            return api_response.JsonOwnerResult

    def note_experiment(self, exp_id: int) -> List[swagger_client.ExperimentNote]:
        """ returns the experiment notes that the user saved for the experiment defined by ID

        Args:
            exp_id (int): Experiment ID

        Return:
            List[swagger_client.ExperimentNote] """
        api_response = self.exp_api.note_experiment(exp_id)
        if api_response.JsonNoteResult is None:
            return []
        else:
            return api_response.JsonNoteResult

# Round API
    def round(self, round_id: int) -> swagger_client.Round:
        """ returns one round by round ID

        Args:
            round_id (int): Round ID

        Return:
            swagger_client.Round """
        api_response = self.round_api.round(round_id)
        return api_response.JsonRoundResult

    def round_experiment(self, exp_id: int) -> List[swagger_client.Round]:
        """ returns all rounds measured in the experiment defined by ID

        Args:
            exp_id (int): Experiment ID

        Return:
            List[swagger_client.Round] """
        api_response = self.round_api.round_experiment(exp_id)
        if api_response.JsonRoundByExperimentIDResult is None:
            return []
        else:
            return api_response.JsonRoundByExperimentIDResult

    def round_date_experiment(self, exp_id: str, start: str, stop: str) -> List[swagger_client.Round]:
        """ returns all rounds measured in the experiment defined by ID between defined times.
        Times is entered as the start and end time of the required interval

        Args:
            exp_id (int): Experiment ID
            start (str): Startdate
            stop (str): Stopdate

        Return:
            List[swagger_client.Round] """
        api_response = self.round_api.round_date_experiment(exp_id, start, stop)
        if api_response.JsonRoundByExperimentIDAndDateResult is None:
            return []
        else:
            return api_response.JsonRoundByExperimentIDAndDateResult

    def round_order_round(self, round_id: int) -> swagger_client.RoundOrder:
        """ returns the round order in the experiment by round ID

        Args:
            round_id (int): Round ID

        Return:
            swagger_client.RoundOrder """
        api_response = self.round_api.round_order_round(round_id)
        return api_response.JsonRoundOrderResult

    def round_order_experiment(self, exp_id: int) -> List[swagger_client.RoundOrder]:
        """ returns all rounds measured in the experiment defined by ID

        Args:
            exp_id (int): Experiment ID

        Return:
            List[swagger_client.RoundOrder] """
        api_response = self.round_api.round_order_experiment(exp_id)
        if api_response.JsonRoundOrderByExperimentIDResult is None:
            return []
        else:
            return api_response.JsonRoundOrderByExperimentIDResult

    def round_order_date_experiment(self, exp_id: int, start: str, stop: str) -> List[swagger_client.RoundOrder]:
        """ returns all rounds measured in the experiment defined by ID

        Args:
            exp_id (int): Experiment ID
            start (str): Startdate
            stop (str): Stopdate

        Return:
            List[swagger_client.RoundOrder] """
        api_response = self.round_api.round_order_date_experiment(exp_id, start, stop)
        if api_response.JsonRoundOrderByExperimentIDAndDateResult is None:
            return []
        else:
            return api_response.JsonRoundOrderByExperimentIDAndDateResult

# Action API
    def action(self, action_id: int) -> swagger_client.Action:
        """ returns one scheduled action by action ID

        Args:
            action_id (int): Action ID

        Return:
            swagger_client.Action """
        api_response = self.action_api.action(action_id)
        return api_response.JsonActionResult

    def action_experiment(self, exp_id: int) -> List[swagger_client.Action]:
        """ returns all scheduled actions in the experiment defined by ID

        Args:
            exp_id (int): Experiment ID

        Return:
            List[swagger_client.Action] """
        api_response = self.action_api.action_experiment(exp_id)
        if api_response.JsonActionByExperimentIDResult is None:
            return []
        else:
            return api_response.JsonActionByExperimentIDResult

    def action_not_done_experiment(self, exp_id: int) -> List[swagger_client.Action]:
        """ returns all unfinished scheduled actions (with pending and running action state)
        in the experiment defined by ID

        Args:
            exp_id (int): experiment ID

        Return:
            List[swagger_client.Action] """
        api_response = self.action_api.action_not_done_experiment(exp_id)
        if api_response.JsonActionByExperimentIDNotDoneResult is None:
            return []
        else:
            return api_response.JsonActionByExperimentIDNotDoneResult

    def action_group(self, group_id: int) -> swagger_client.ActionGroup:
        """ returns one group of scheduled actions by action group ID

        Args:
            group_id (int): Group ID

        Return:
            swagger_client.ActionGroup """
        api_response = self.action_api.action_group(group_id)
        return api_response.JsonActionGroupResult

    def action_group_round(self, round_id: int) -> swagger_client.ActionGroup:
        """ returns one group of scheduled actions to which a round defined by ID belongs

        Args:
            round_id (int): Round ID

        Return:
            swagger_client.ActionGroup """
        api_response = self.action_api.action_group_round(round_id)
        return api_response.JsonActionGroupByRoundIDResult

    def action_protocol(self, prot_id: int) -> swagger_client.ActionProtocol:
        """ returns one protocol of scheduled action by protocol ID

        Args:
            prot_id (int): Protocol ID

        Return:
            swagger_client.ActionProtocol """
        api_response = self.action_api.action_protocol(prot_id)
        return api_response.JsonActionProtocolResult

    def action_protocol_round(self, round_id: int) -> swagger_client.ActionProtocol:
        """ returns one group of scheduled actions that belong to round defined by ID

        Args:
            round_id (int): Round ID

        Return:
            swagger_client.ActionProtocol """
        api_response = self.action_api.action_protocol_round(round_id)
        return api_response.JsonActionProtocolByRoundIDResult

# Device API
    def device(self, device_id: int) -> swagger_client.Device:
        """ returns one device by device ID

        Args:
            device_id (int): Device ID

        Return:
            swagger_client.Device """
        api_response = self.device_api.device(device_id)
        return api_response.JsonDeviceResult

    def device_active(self) -> List[swagger_client.Device]:
        """ returns all active devices that have not ended validity

        Args:
            -

        Return:
            List[swagger_client.Device] """
        api_response = self.device_api.device_active()
        if api_response.JsonDeviceActiveResult is None:
            return []
        else:
            return api_response.JsonDeviceActiveResult

    def device_profile(self, prof_id: int) -> List[swagger_client.Device]:
        """ returns all devices that contains the system profile defined by ID

        Args:
            prof_id (int): Profile ID

        Return:
            List[swagger_client.Device] """
        api_response = self.device_api.device_profile(prof_id)
        if api_response.JsonDeviceByProfileIDResult is None:
            return []
        else:
            return api_response.JsonDeviceByProfileIDResult

# Profile API
    def profile_id(self) -> List[swagger_client.ProfileIDWrapper]:
        """ returns a list of all system profile IDs in the database

        Args:
            -

        Return:
            List[swagger_client.ProfileIDWrapper] """
        api_response = self.profile_api.profile_id()
        if api_response.JsonSystemProfileIDResult is None:
            return []
        else:
            return api_response.JsonSystemProfileIDResult

    def profile(self, prof_id: int) -> swagger_client.SystemProfile:
        """ returns one system profile by profile ID

        Args:
            prof_id (int): Profile ID

        Return:
            swagger_client.SystemProfile """
        api_response = self.profile_api.profile(prof_id)
        return api_response.JsonSystemProfileResult

    def profile_active(self) -> swagger_client.SystemProfile:
        """ returns the active system profile

        Args:
            -

        Return:
            swagger_client.SystemProfile """
        api_response = self.profile_api.profile_active()
        return api_response.JsonSystemProfileActiveResult

# Tray API
    def tray(self, tray_id: int) -> swagger_client.Tray:
        """ returns one tray by tray ID

        Args:
            tray_id (int): Tray ID

        Return:
            swagger_client.Tray """
        api_response = self.tray_api.tray(tray_id)
        return api_response.JsonTrayResult

    def tray_round(self, round_id: int) -> List[swagger_client.Tray]:
        """ returns all trays measured in the round defined by ID

        Args:
            round_id (int): Round ID

        Return:
            List[swagger_client.Tray] """
        api_response = self.tray_api.tray_round(round_id)
        if api_response.JsonTrayByRoundIDResult is None:
            return []
        else:
            return api_response.JsonTrayByRoundIDResult

    def tray_type(self, tray_id: int) -> swagger_client.TrayType:
        """ returns one tray type by tray type ID

        Args:
            tray_id (int): Tray ID

        Return:
            swagger_client.TrayType """
        api_response = self.tray_api.tray_type(tray_id)
        return api_response.JsonTrayTypeResult

    def tray_type_tray(self, tray_id: int) -> swagger_client.TrayType:
        """ returns one tray type which is assigned to the tray defined by ID

        Args:
            tray_id (int): Tray ID

        Return:
            swagger_client.TrayType """
        api_response = self.tray_api.tray_type_tray(tray_id)
        return api_response.JsonTrayTypeByTrayIDResult

    def tray_type_tray_profile(self, tray_prof_id: int) -> swagger_client.TrayType:
        """ returns one tray type which is assigned to the tray profile defined by ID

        Args:
            tray_prof_id (int): Tray profile ID

        Return:
            swagger_client.TrayType """
        api_response = self.tray_api.tray_type_tray_profile(tray_prof_id)
        return api_response.JsonTrayTypeByTrayProfileIDResult

    def tray_profile(self, prof_id: int) -> swagger_client.TrayProfile:
        """ returns one tray profile by tray profile ID

        Args:
            prof_id (int): Profile ID

        Return:
            swagger_client.TrayProfile """
        api_response = self.tray_api.tray_profile(prof_id)
        return api_response.JsonTrayProfileByIDResult

    def tray_profile_tray(self, tray_id: int) -> swagger_client.TrayProfile:
        """ returns one tray profile to which tray defined by ID is assigned

        Args:
            tray_id (int): Tray ID

        Return:
            swagger_client.TrayProfile """
        api_response = self.tray_api.tray_profile_tray(tray_id)
        return api_response.JsonTrayProfileByTrayIDResult

    def tray_profile_used_tray(self, tray_id: int, start: str, stop: str) -> List[swagger_client.TrayProfile]:
        """ returns tray profiles to which tray defined by ID was assigned between defined times.
        Times is entered as the start and end time of the required interval.
        All tray profiles assigned to tray between these times will be returned

        Args:
            tray_id (int): Tray ID
            start (string): Startdate
            stop (string): Stopdate

        Return:
            List[swagger_client.TrayProfile] """
        api_response = self.tray_api.tray_profile_used_tray(tray_id, start, stop)
        if api_response.JsonUsedTrayProfileByTrayIDResult is None:
            return []
        else:
            return api_response.JsonUsedTrayProfileByTrayIDResult

    def tray_profile_to_date_tray(self, tray_id: int, date: str) -> swagger_client.TrayProfile:
        """ returns one tray profile to which tray defined by ID was assigned on the defined time

        Args:
            tray_id (int): Tray ID
            date (string): Timestamp

        Return:
            swagger_client.TrayProfile """
        api_response = self.tray_api.tray_profile_to_date_tray(tray_id, date)
        return api_response.JsonTrayProfileByTrayIDToDateResult

    def scales_mapping_tray(self, tray_id: int) -> List[swagger_client.ScalesMapping]:
        """ returns tray profiles to which tray defined by ID was assigned between defined times.
        Times is entered as the start and end time of the required interval.
        All tray profiles assigned to tray between these times will be returned

        Args:
            tray_id (int): Tray ID

        Return:
            List[swagger_client.ScalesMapping] """
        api_response = self.tray_api.scales_mapping_tray(tray_id)
        if api_response.JsonScalesMappingByTrayIDResult is None:
            return []
        else:
            return api_response.JsonScalesMappingByTrayIDResult

# Plant API
    def plant(self, plant_ids: List[int]) -> List[swagger_client.Plant]:
        """ returns a list of plants by the list of plant IDs

        Args:
            plant_ids (List[int]): plant IDs

        Return:
            List[swagger_client.Plant] """
        api_response = self.plant_api.plant(plant_ids)
        if api_response.JsonPlantResult is None:
            return []
        else:
            return api_response.JsonPlantResult

    def plant_tray(self, tray_id: int) -> List[swagger_client.Plant]:
        """ returns list of plants which are assigned to the tray defined by ID

        Args:
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Plant] """
        api_response = self.plant_api.plant_tray(tray_id)
        if api_response.JsonPlantByTrayIDResult is None:
            return []
        else:
            return api_response.JsonPlantByTrayIDResult

    def plant_tray_profile_tray(self, tray_id: int, start: str, stop: str) -> List[swagger_client.Plant]:
        """ returns plants that were assigned to the tray defined by tray ID between defined times.
        Times is entered as the start and end time of the required interval.
        All plants assigned to tray between these times will be returned

        Args:
            tray_id (int): Tray ID
            start (string): Startdate
            stop (string): Stopdate

        Return:
            List[swagger_client.Plant] """
        api_response = self.plant_api.plant_tray_profile_tray(tray_id, start, stop)
        if api_response.JsonPlantByTrayIDAndDatesResult is None:
            return []
        else:
            return api_response.JsonPlantByTrayIDAndDatesResult

    def plant_tray_profile(self, tray_prof_id: int) -> List[swagger_client.Plant]:
        """ returns plants that were assigned to the tray profile defined by tray profile ID without time limit

        Args:
            tray_prof_id (int): Tray profile ID

        Return:
            List[swagger_client.Plant] """
        api_response = self.plant_api.plant_tray_profile(tray_prof_id)
        if api_response.JsonPlantByTrayProfileIDResult is None:
            return []
        else:
            return api_response.JsonPlantByTrayProfileIDResult

    def plant_height_round(self, round_id: int) -> List[swagger_client.PlantHeight]:
        """ returns all plant heights measured in the round defined by ID

        Args:
            round_id (int): Round ID

        Return:
            List[swagger_client.PlantHeight] """
        api_response = self.plant_api.plant_height_round(round_id)
        if api_response.JsonPlantHeightByRoundIDResult is None:
            return []
        else:
            return api_response.JsonPlantHeightByRoundIDResult

    def plant_leaf(self, plant_id: int, tray_id: int) -> List[swagger_client.PlantLeaf]:
        """ returns all plant heights measured in the round defined by ID

        Args:
            plant_id (int): Plant ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.PlantLeaf] """
        api_response = self.plant_api.plant_leaf(plant_id, tray_id)
        if api_response.JsonPlantLeavesByPlantAndTrayIDResult is None:
            return []
        else:
            return api_response.JsonPlantLeavesByPlantAndTrayIDResult

# Buffer API
    def get_buffer_history(self, buff_id: int) -> swagger_client.BufferHistory:
        """ returns one buffer history state defined by buffer state ID

        Args:
            buff_id (int): Buffer state ID

        Return:
            swagger_client.BufferHistory """
        api_response = self.buffer_api.buffer_history(buff_id)
        return api_response.JsonBufferHistoryResult

    def get_buffer_history_date(self, start: str, stop: str) -> List[swagger_client.BufferHistory]:
        """ returns buffer history states between times.
        Times is entered as the start and end time of the required interval.

        Args:
            start (string) Startdate
            stop (string) Stopdate

        Return:
            List[swagger_client.BufferHistory] """
        api_response = self.buffer_api.buffer_history_date(start, stop)
        if api_response.JsonBufferHistoryByDateResult is None:
            return []
        else:
            return api_response.JsonBufferHistoryByDateResult

# System Log API
    def get_system_log_round(self, round_id: int) -> List[swagger_client.SystemLog]:
        """ Returns important events as system logs by round ID. System logs are only optionally assigned to the round

        Args:
            round_id (int): Round ID

        Return:
            List[swagger_client.SystemLog] """
        api_response = self.system_log_api.system_log_round(round_id)
        if api_response.JsonSystemLogByRoundIDResult is None:
            return []
        else:
            return api_response.JsonSystemLogByRoundIDResult

    def get_system_log_date_round(self, round_id: int, start: str, stop: str) -> List[swagger_client.SystemLog]:
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
        if api_response.JsonSystemLogByRoundIDAndDateResult is None:
            return []
        else:
            return api_response.JsonSystemLogByRoundIDAndDateResult

    def get_system_log_tray(self, tray_id: int) -> List[swagger_client.SystemLog]:
        """ Returns important events as system logs by tray ID.
        System logs are only optionally assigned to the tray

        Args:
            tray_id (int): Tray ID

        Return:
            List[swagger_client.SystemLog]
        """
        api_response = self.system_log_api.system_log_tray(tray_id)
        if api_response.JsonSystemLogByTrayIDResult is None:
            return []
        else:
            return api_response.JsonSystemLogByTrayIDResult

    def get_system_log_date_tray(self, tray_id: int, start: str, stop: str) -> List[swagger_client.SystemLog]:
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
        if api_response.JsonSystemLogByTrayIDAndDateResult is None:
            return []
        else:
            return api_response.JsonSystemLogByTrayIDAndDateResult

    def get_system_log_log_type(self) -> List[swagger_client.LogType]:
        """ Returns a list of all used system log types

        Args:
            -

        Return:
            List[swagger_client.LogType]
        """
        api_response = self.system_log_api.system_log_log_type()
        if api_response.JsonSystemLogTypeResult is None:
            return []
        else:
            return api_response.JsonSystemLogTypeResult

    def get_system_log_date_log_type(self, type: str, start: str, stop: str) -> List[swagger_client.SystemLog]:
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
        if api_response.JsonSystemLogByLogTypeAndDateResult is None:
            return []
        else:
            return api_response.JsonSystemLogByLogTypeAndDateResult

    def get_system_log_log_tag(self) -> List[swagger_client.LogTag]:
        """ Returns a list of all used system log tag

        Args:
            -

        Return:
            List[swagger_client.LogTag]
        """
        api_response = self.system_log_api.system_log_log_tag()
        if api_response.JsonSystemLogTagResult is None:
            return []
        else:
            return api_response.JsonSystemLogTagResult

    def get_system_log_date_log_tag(self, tag: str, start: str, stop: str) -> List[swagger_client.SystemLog]:
        """ Returns a list of all used system log tag

        Args:
            tag (str): Log tag
            start (str): Startdate
            stop (str): Stopdate

        Return:
            List[swagger_client.SystemLog]
        """
        api_response = self.system_log_api.system_log_date_log_tag(tag, start, stop)
        if api_response.JsonSystemLogByLogTagAndDateResult is None:
            return []
        else:
            return api_response.JsonSystemLogByLogTagAndDateResult

# Version Info API
    def version_info(self) -> swagger_client.VersionInfo:
        """ Returns version of the database and the PlantScreen Data REST API used

        Args:
            -

        Return:
            swagger_client.VersionInfo
        """
        api_response = self.version_info_api.version_info()
        return api_response.JsonVersionInfoResult
