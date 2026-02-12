"""
Auto-generated API client wrapper with direct methods for all endpoints.
"""
from plantscreen.api_client import ApiClient
import plantscreen.api as api_module
from typing import Any, Optional, Union, Tuple, List, Dict
from datetime import datetime
from plantscreen.models import Action, ActionGroup, ActionProtocol, BufferHistory, Device, Experiment, ExperimentIDWrapper, ExperimentNote, FcImaging, HcImaging, HcRgbImage, Imaging, LeafParameter, LogTag, LogType, MeasureExtendedData, MscCalibration, MscCalibrationLight, MscCalibrationLight200Response, MscLightSet, Owner, OwnerIDWrapper, Parameter, ParameterImage, Plant, PlantHeight, PlantLeaf, PlantMask, PlantParameter, PlantWeightReference, Probe, Probe200Response, ProbeValue, ProfileIDWrapper, RgbGreeningMaskImage, Round, RoundOrder, ScalesData, ScalesMapping, Scan3DAnalyzedModel, Scan3DImaging, SpectrumDevice, SpectrumDeviceID, SpectrumDeviceWavelengthsJSONWrapper, SpectrumValues, SprayAction, StatisticLeafParameter, StatisticPlantParameter, SystemLog, SystemProfile, Tray, TrayProfile, TrayType, VersionInfo

class CompleteAPIClient(ApiClient):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        '''
        Parameters:
        Returns:
            None
        """'''
        super().__init__(*args, **kwargs)
        self._ActionApi: api_module.ActionApi = api_module.ActionApi(self)
        self._BufferApi: api_module.BufferApi = api_module.BufferApi(self)
        self._DeviceApi: api_module.DeviceApi = api_module.DeviceApi(self)
        self._ExperimentApi: api_module.ExperimentApi = api_module.ExperimentApi(self)
        self._FcApi: api_module.FcApi = api_module.FcApi(self)
        self._FileApi: api_module.FileApi = api_module.FileApi(self)
        self._HcApi: api_module.HcApi = api_module.HcApi(self)
        self._IrApi: api_module.IrApi = api_module.IrApi(self)
        self._MscApi: api_module.MscApi = api_module.MscApi(self)
        self._PlantApi: api_module.PlantApi = api_module.PlantApi(self)
        self._ProbeApi: api_module.ProbeApi = api_module.ProbeApi(self)
        self._ProfileApi: api_module.ProfileApi = api_module.ProfileApi(self)
        self._RgbApi: api_module.RgbApi = api_module.RgbApi(self)
        self._RoundApi: api_module.RoundApi = api_module.RoundApi(self)
        self._ScalesApi: api_module.ScalesApi = api_module.ScalesApi(self)
        self._Scan3dApi: api_module.Scan3dApi = api_module.Scan3dApi(self)
        self._SpectrumDeviceApi: api_module.SpectrumDeviceApi = api_module.SpectrumDeviceApi(self)
        self._SprayApi: api_module.SprayApi = api_module.SprayApi(self)
        self._SystemLogApi: api_module.SystemLogApi = api_module.SystemLogApi(self)
        self._TrayApi: api_module.TrayApi = api_module.TrayApi(self)
        self._VersionInfoApi: api_module.VersionInfoApi = api_module.VersionInfoApi(self)

    def action(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Action:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Action
        """'''
        result = self._ActionApi.action(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_action_result', None)

    def action_experiment(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Action]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Action]
        """'''
        result = self._ActionApi.action_experiment(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_action_by_experiment_id_result', None)

    def action_group(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> ActionGroup:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            ActionGroup
        """'''
        result = self._ActionApi.action_group(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_action_group_result', None)

    def action_group_round(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> ActionGroup:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            ActionGroup
        """'''
        result = self._ActionApi.action_group_round(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_action_group_by_round_id_result', None)

    def action_not_done_experiment(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Action]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Action]
        """'''
        result = self._ActionApi.action_not_done_experiment(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_action_by_experiment_id_not_done_result', None)

    def action_protocol(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> ActionProtocol:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            ActionProtocol
        """'''
        result = self._ActionApi.action_protocol(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_action_protocol_result', None)

    def action_protocol_round(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> ActionProtocol:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            ActionProtocol
        """'''
        result = self._ActionApi.action_protocol_round(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_action_protocol_by_round_id_result', None)

    def buffer_history(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> BufferHistory:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            BufferHistory
        """'''
        result = self._BufferApi.buffer_history(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_buffer_history_result', None)

    def buffer_history_date(self, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[BufferHistory]:
        '''
        Parameters:
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[BufferHistory]
        """'''
        result = self._BufferApi.buffer_history_date(start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_buffer_history_by_date_result', None)

    def device(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Device:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Device
        """'''
        result = self._DeviceApi.device(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_device_result', None)

    def device_active(self, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Device]:
        '''
        Parameters:
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Device]
        """'''
        result = self._DeviceApi.device_active(_request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_device_active_result', None)

    def device_profile(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Device]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Device]
        """'''
        result = self._DeviceApi.device_profile(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_device_by_profile_id_result', None)

    def experiment(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Experiment:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Experiment
        """'''
        result = self._ExperimentApi.experiment(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_experiment_result', None)

    def experiment_date(self, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Experiment]:
        '''
        Parameters:
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Experiment]
        """'''
        result = self._ExperimentApi.experiment_date(start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_experiment_by_date_result', None)

    def experiment_id(self, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> list[int]:
        '''
        Parameters:
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            list[int]
        """'''
        result = self._ExperimentApi.experiment_id(_request_timeout, _request_auth, _content_type, _headers, _host_index)
        temp = getattr(result, 'json_experiment_id_result', None)
        if temp is not None:
            return [x.experiment_id for x in temp]
        else:
            return []

    def experiment_owner(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Experiment]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Experiment]
        """'''
        result = self._ExperimentApi.experiment_owner(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_experiment_by_owner_result', None)

    def note_experiment(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[ExperimentNote]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[ExperimentNote]
        """'''
        result = self._ExperimentApi.note_experiment(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_note_result', None)

    def owner(self, ids: List[int], _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Owner]:
        '''
        Parameters:
            ids (List[int])
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Owner]
        """'''
        result = self._ExperimentApi.owner(ids, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_owner_result', None)

    def owner_id(self, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[int]:
        '''
        Parameters:
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[int]
        """'''
        result = self._ExperimentApi.owner_id(_request_timeout, _request_auth, _content_type, _headers, _host_index)
        temp = getattr(result, 'json_owner_id_result', None)
        if temp is not None:
            return [x.owner_id for x in temp]
        else:
            return []

    def fc_imaging(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[FcImaging]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[FcImaging]
        """'''
        result = self._FcApi.fc_imaging(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_imaging_result', None)

    def fc_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MeasureExtendedData:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MeasureExtendedData
        """'''
        result = self._FcApi.fc_imaging_extended_data(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_measure_extended_data_result', None)

    def fc_imaging_extended_data_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MeasureExtendedData:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MeasureExtendedData
        """'''
        result = self._FcApi.fc_imaging_extended_data_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_measure_extended_data_by_id_result', None)

    def fc_imaging_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> FcImaging:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            FcImaging
        """'''
        result = self._FcApi.fc_imaging_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_imaging_by_id_result', None)

    def fc_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[LeafParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[LeafParameter]
        """'''
        result = self._FcApi.fc_leaf_param(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_leaf_param_result', None)

    def fc_leaf_param_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[LeafParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[LeafParameter]
        """'''
        result = self._FcApi.fc_leaf_param_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_leaf_param_by_analyse_id_result', None)

    def fc_param(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Parameter:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Parameter
        """'''
        result = self._FcApi.fc_param(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_param_result', None)

    def fc_param_image(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[ParameterImage]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[ParameterImage]
        """'''
        result = self._FcApi.fc_param_image(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_parameter_image_result', None)

    def fc_param_image_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> ParameterImage:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            ParameterImage
        """'''
        result = self._FcApi.fc_param_image_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_parameter_image_by_analyse_id_result', None)

    def fc_param_used(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._FcApi.fc_param_used(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_used_param_result', None)

    def fc_param_used_analyse(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._FcApi.fc_param_used_analyse(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_used_param_by_analyse_id_result', None)

    def fc_plant_mask(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantMask]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantMask]
        """'''
        result = self._FcApi.fc_plant_mask(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_plant_mask_result', None)

    def fc_plant_mask_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> PlantMask:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            PlantMask
        """'''
        result = self._FcApi.fc_plant_mask_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_plant_mask_by_measure_id_result', None)

    def fc_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantParameter]
        """'''
        result = self._FcApi.fc_plant_param(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_plant_param_result', None)

    def fc_plant_param_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantParameter]
        """'''
        result = self._FcApi.fc_plant_param_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_fc_plant_param_by_analyse_id_result', None)

    def file(self, path: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> None:
        '''
        Parameters:
            path (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            None
        """'''
        return self._FileApi.file(path, _request_timeout, _request_auth, _content_type, _headers, _host_index)

    def file_changelog(self, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> str:
        '''
        Parameters:
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            str
        """'''
        return self._FileApi.file_changelog(_request_timeout, _request_auth, _content_type, _headers, _host_index)

    def hc_imaging(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[HcImaging]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[HcImaging]
        """'''
        result = self._HcApi.hc_imaging(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_imaging_result', None)

    def hc_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MeasureExtendedData:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MeasureExtendedData
        """'''
        result = self._HcApi.hc_imaging_extended_data(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_measure_extended_data_result', None)

    def hc_imaging_extended_data_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MeasureExtendedData:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MeasureExtendedData
        """'''
        result = self._HcApi.hc_imaging_extended_data_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_measure_extended_data_by_id_result', None)

    def hc_imaging_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> HcImaging:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            HcImaging
        """'''
        result = self._HcApi.hc_imaging_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_imaging_by_id_result', None)

    def hc_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[StatisticLeafParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[StatisticLeafParameter]
        """'''
        result = self._HcApi.hc_leaf_param(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_leaf_param_result', None)

    def hc_leaf_param_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[StatisticLeafParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[StatisticLeafParameter]
        """'''
        result = self._HcApi.hc_leaf_param_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_leaf_param_by_analyse_id_result', None)

    def hc_param(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Parameter:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Parameter
        """'''
        result = self._HcApi.hc_param(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_param_result', None)

    def hc_param_image(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[ParameterImage]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[ParameterImage]
        """'''
        result = self._HcApi.hc_param_image(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_parameter_image_result', None)

    def hc_param_image_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> ParameterImage:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            ParameterImage
        """'''
        result = self._HcApi.hc_param_image_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_parameter_image_by_analyse_id_result', None)

    def hc_param_used(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._HcApi.hc_param_used(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_used_param_result', None)

    def hc_param_used_analyse(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._HcApi.hc_param_used_analyse(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_used_param_by_analyse_id_result', None)

    def hc_plant_mask(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantMask]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantMask]
        """'''
        result = self._HcApi.hc_plant_mask(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_plant_mask_result', None)

    def hc_plant_mask_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> PlantMask:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            PlantMask
        """'''
        result = self._HcApi.hc_plant_mask_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_plant_mask_by_measure_id_result', None)

    def hc_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[StatisticPlantParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[StatisticPlantParameter]
        """'''
        result = self._HcApi.hc_plant_param(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_plant_param_result', None)

    def hc_plant_param_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[StatisticPlantParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[StatisticPlantParameter]
        """'''
        result = self._HcApi.hc_plant_param_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_plant_param_by_analyse_id_result', None)

    def hc_rgb_image(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[HcRgbImage]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[HcRgbImage]
        """'''
        result = self._HcApi.hc_rgb_image(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_rgb_image_result', None)

    def hc_rgb_image_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> HcRgbImage:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            HcRgbImage
        """'''
        result = self._HcApi.hc_rgb_image_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_hc_rgb_image_by_measure_id_result', None)

    def ir_imaging(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Imaging]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Imaging]
        """'''
        result = self._IrApi.ir_imaging(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_imaging_result', None)

    def ir_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MeasureExtendedData:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MeasureExtendedData
        """'''
        result = self._IrApi.ir_imaging_extended_data(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_measure_extended_data_result', None)

    def ir_imaging_extended_data_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MeasureExtendedData:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MeasureExtendedData
        """'''
        result = self._IrApi.ir_imaging_extended_data_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_measure_extended_data_by_id_result', None)

    def ir_imaging_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Imaging:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Imaging
        """'''
        result = self._IrApi.ir_imaging_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_imaging_by_id_result', None)

    def ir_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[StatisticLeafParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[StatisticLeafParameter]
        """'''
        result = self._IrApi.ir_leaf_param(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_leaf_param_result', None)

    def ir_leaf_param_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[StatisticLeafParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[StatisticLeafParameter]
        """'''
        result = self._IrApi.ir_leaf_param_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_leaf_param_by_analyse_id_result', None)

    def ir_param(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Parameter:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Parameter
        """'''
        result = self._IrApi.ir_param(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_param_result', None)

    def ir_param_used(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._IrApi.ir_param_used(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_used_param_result', None)

    def ir_param_used_analyse(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._IrApi.ir_param_used_analyse(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_used_param_by_analyse_id_result', None)

    def ir_plant_mask(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantMask]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantMask]
        """'''
        result = self._IrApi.ir_plant_mask(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_plant_mask_result', None)

    def ir_plant_mask_image(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Imaging]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Imaging]
        """'''
        result = self._IrApi.ir_plant_mask_image(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_plant_mask_image_result', None)

    def ir_plant_mask_image_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Imaging:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Imaging
        """'''
        result = self._IrApi.ir_plant_mask_image_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_plant_mask_image_by_measure_id_result', None)

    def ir_plant_mask_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> PlantMask:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            PlantMask
        """'''
        result = self._IrApi.ir_plant_mask_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_plant_mask_by_measure_id_result', None)

    def ir_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[StatisticPlantParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[StatisticPlantParameter]
        """'''
        result = self._IrApi.ir_plant_param(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_plant_param_result', None)

    def ir_plant_param_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[StatisticPlantParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[StatisticPlantParameter]
        """'''
        result = self._IrApi.ir_plant_param_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_ir_plant_param_by_analyse_id_result', None)

    def msc_calibration(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MscCalibration:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MscCalibration
        """'''
        result = self._MscApi.msc_calibration(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_calibration_result', None)

    def msc_calibration_light(self, id: int=None, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MscCalibrationLight:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MscCalibrationLight
        """'''
        result = self._MscApi.msc_calibration_light(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        value = getattr(result, 'json_msc_calibration_light_by_id_result', None)
        if value is None:
            value = getattr(result, 'json_msc_calibration_light_result', None)
        return value

    def msc_calibration_light_set(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MscCalibration:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MscCalibration
        """'''
        result = self._MscApi.msc_calibration_light_set(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_calibration_by_light_set_id_result', None)

    def msc_imaging(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Imaging]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Imaging]
        """'''
        result = self._MscApi.msc_imaging(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_imaging_result', None)

    def msc_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MeasureExtendedData:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MeasureExtendedData
        """'''
        result = self._MscApi.msc_imaging_extended_data(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_measure_extended_data_result', None)

    def msc_imaging_extended_data_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MeasureExtendedData:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MeasureExtendedData
        """'''
        result = self._MscApi.msc_imaging_extended_data_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_measure_extended_data_by_id_result', None)

    def msc_imaging_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Imaging]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Imaging]
        """'''
        result = self._MscApi.msc_imaging_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_imaging_by_id_result', None)

    def msc_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[StatisticLeafParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[StatisticLeafParameter]
        """'''
        result = self._MscApi.msc_leaf_param(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_leaf_param_result', None)

    def msc_leaf_param_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[StatisticLeafParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[StatisticLeafParameter]
        """'''
        result = self._MscApi.msc_leaf_param_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_leaf_param_by_analyse_id_result', None)

    def msc_light_set(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MscLightSet:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MscLightSet
        """'''
        result = self._MscApi.msc_light_set(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_light_set_result', None)

    def msc_light_set_used(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[MscLightSet]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[MscLightSet]
        """'''
        result = self._MscApi.msc_light_set_used(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_light_set_used_result', None)

    def msc_param(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Parameter:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Parameter
        """'''
        result = self._MscApi.msc_param(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_param_result', None)

    def msc_param_image(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[ParameterImage]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[ParameterImage]
        """'''
        result = self._MscApi.msc_param_image(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_parameter_image_result', None)

    def msc_param_image_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> ParameterImage:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            ParameterImage
        """'''
        result = self._MscApi.msc_param_image_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_parameter_image_by_analyse_id_result', None)

    def msc_param_used(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._MscApi.msc_param_used(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_used_param_result', None)

    def msc_param_used_analyse(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._MscApi.msc_param_used_analyse(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_used_param_by_analyse_id_result', None)

    def msc_plant_mask(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantMask]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantMask]
        """'''
        result = self._MscApi.msc_plant_mask(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_plant_mask_result', None)

    def msc_plant_mask_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> PlantMask:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            PlantMask
        """'''
        result = self._MscApi.msc_plant_mask_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_plant_mask_by_measure_id_result', None)

    def msc_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[StatisticPlantParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[StatisticPlantParameter]
        """'''
        result = self._MscApi.msc_plant_param(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_plant_param_result', None)

    def msc_plant_param_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[StatisticPlantParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[StatisticPlantParameter]
        """'''
        result = self._MscApi.msc_plant_param_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_msc_plant_param_by_analyse_id_result', None)

    def plant(self, ids: List[int], _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Plant]:
        '''
        Parameters:
            ids (List[int])
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Plant]
        """'''
        result = self._PlantApi.plant(ids, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_plant_result', None)

    def plant_height_round(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantHeight]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantHeight]
        """'''
        result = self._PlantApi.plant_height_round(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_plant_height_by_round_id_result', None)

    def plant_leaf(self, plant_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantLeaf]:
        '''
        Parameters:
            plant_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantLeaf]
        """'''
        result = self._PlantApi.plant_leaf(plant_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_plant_leaves_by_plant_and_tray_id_result', None)

    def plant_tray(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Plant]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Plant]
        """'''
        result = self._PlantApi.plant_tray(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_plant_by_tray_id_result', None)

    def plant_tray_profile(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Plant]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Plant]
        """'''
        result = self._PlantApi.plant_tray_profile(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_plant_by_tray_profile_id_result', None)

    def plant_tray_profile_tray(self, id: int, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Plant]:
        '''
        Parameters:
            id (int)
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Plant]
        """'''
        result = self._PlantApi.plant_tray_profile_tray(id, start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_plant_by_tray_id_and_dates_result', None)

    def probe(self, id: int=None, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Probe:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Probe
        """'''
        result = self._ProbeApi.probe(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        value = getattr(result, 'json_probe_result', None)
        if value is None:
            value = getattr(result, 'json_probe_by_id_result', None)
        return value

    def probe_value_date(self, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[ProbeValue]:
        '''
        Parameters:
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[ProbeValue]
        """'''
        result = self._ProbeApi.probe_value_date(start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_probe_value_by_date_result', None)

    def probe_value_date_probe(self, id: int, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[ProbeValue]:
        '''
        Parameters:
            id (int)
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[ProbeValue]
        """'''
        result = self._ProbeApi.probe_value_date_probe(id, start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_probe_value_by_id_and_date_result', None)

    def profile(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> SystemProfile:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            SystemProfile
        """'''
        result = self._ProfileApi.profile(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_system_profile_result', None)

    def profile_active(self, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> SystemProfile:
        '''
        Parameters:
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            SystemProfile
        """'''
        result = self._ProfileApi.profile_active(_request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_system_profile_active_result', None)

    def profile_id(self, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> list[int]:
        '''
        Parameters:
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            list[int]
        """'''
        result = self._ProfileApi.profile_id(_request_timeout, _request_auth, _content_type, _headers, _host_index)
        temp = getattr(result, 'json_system_profile_id_result', None)
        if temp is not None:
            return [x.profile_id for x in temp]
        else:
            return []

    def rgb_greening_mask_image(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[RgbGreeningMaskImage]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[RgbGreeningMaskImage]
        """'''
        result = self._RgbApi.rgb_greening_mask_image(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_greening_mask_image_result', None)

    def rgb_greening_mask_image_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> RgbGreeningMaskImage:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            RgbGreeningMaskImage
        """'''
        result = self._RgbApi.rgb_greening_mask_image_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_greening_mask_image_by_measure_id_result', None)

    def rgb_imaging(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Imaging]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Imaging]
        """'''
        result = self._RgbApi.rgb_imaging(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_imaging_result', None)

    def rgb_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MeasureExtendedData:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MeasureExtendedData
        """'''
        result = self._RgbApi.rgb_imaging_extended_data(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_measure_extended_data_result', None)

    def rgb_imaging_extended_data_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MeasureExtendedData:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MeasureExtendedData
        """'''
        result = self._RgbApi.rgb_imaging_extended_data_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_measure_extended_data_by_id_result', None)

    def rgb_imaging_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Imaging:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Imaging
        """'''
        result = self._RgbApi.rgb_imaging_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_imaging_by_id_result', None)

    def rgb_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[LeafParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[LeafParameter]
        """'''
        result = self._RgbApi.rgb_leaf_param(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_leaf_param_result', None)

    def rgb_leaf_param_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[LeafParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[LeafParameter]
        """'''
        result = self._RgbApi.rgb_leaf_param_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_leaf_param_by_analyse_id_result', None)

    def rgb_leaf_param_color(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[LeafParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[LeafParameter]
        """'''
        result = self._RgbApi.rgb_leaf_param_color(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_leaf_param_color_result', None)

    def rgb_leaf_param_color_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[LeafParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[LeafParameter]
        """'''
        result = self._RgbApi.rgb_leaf_param_color_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_leaf_param_color_by_analyse_id_result', None)

    def rgb_param(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Parameter:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Parameter
        """'''
        result = self._RgbApi.rgb_param(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_param_result', None)

    def rgb_param_color_used(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._RgbApi.rgb_param_color_used(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_used_param_color_result', None)

    def rgb_param_color_used_analyse(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._RgbApi.rgb_param_color_used_analyse(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_used_param_color_by_analyse_id_result', None)

    def rgb_param_used(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._RgbApi.rgb_param_used(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_used_params_result', None)

    def rgb_param_used_analyse(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._RgbApi.rgb_param_used_analyse(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_used_param_by_analyse_id_result', None)

    def rgb_plant_mask(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantMask]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantMask]
        """'''
        result = self._RgbApi.rgb_plant_mask(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_plant_mask_result', None)

    def rgb_plant_mask_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> PlantMask:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            PlantMask
        """'''
        result = self._RgbApi.rgb_plant_mask_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_plant_mask_by_measure_id_result', None)

    def rgb_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantParameter]
        """'''
        result = self._RgbApi.rgb_plant_param(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_plant_param_result', None)

    def rgb_plant_param_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantParameter]
        """'''
        result = self._RgbApi.rgb_plant_param_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_plant_param_by_analyse_id_result', None)

    def rgb_plant_param_color(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantParameter]
        """'''
        result = self._RgbApi.rgb_plant_param_color(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_plant_param_color_result', None)

    def rgb_plant_param_color_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantParameter]
        """'''
        result = self._RgbApi.rgb_plant_param_color_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_rgb_plant_param_color_by_analyse_id_result', None)

    def round(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Round:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Round
        """'''
        result = self._RoundApi.round(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_round_result', None)

    def round_date_experiment(self, id: int, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Round]:
        '''
        Parameters:
            id (int)
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Round]
        """'''
        result = self._RoundApi.round_date_experiment(id, start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_round_by_experiment_id_and_date_result', None)

    def round_experiment(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Round]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Round]
        """'''
        result = self._RoundApi.round_experiment(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_round_by_experiment_id_result', None)

    def round_order_date_experiment(self, id: int, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[RoundOrder]:
        '''
        Parameters:
            id (int)
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[RoundOrder]
        """'''
        result = self._RoundApi.round_order_date_experiment(id, start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_round_order_by_experiment_id_and_date_result', None)

    def round_order_experiment(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[RoundOrder]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[RoundOrder]
        """'''
        result = self._RoundApi.round_order_experiment(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_round_order_by_experiment_id_result', None)

    def round_order_round(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> RoundOrder:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            RoundOrder
        """'''
        result = self._RoundApi.round_order_round(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_round_order_result', None)

    def scales_plant_weight(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[ScalesData]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[ScalesData]
        """'''
        result = self._ScalesApi.scales_plant_weight(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scales_measure_result', None)

    def scales_plant_weight_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> ScalesData:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            ScalesData
        """'''
        result = self._ScalesApi.scales_plant_weight_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scales_measure_by_id_result', None)

    def scales_weight_reference_plant(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> PlantWeightReference:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            PlantWeightReference
        """'''
        result = self._ScalesApi.scales_weight_reference_plant(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_plant_weight_reference_by_plant_id_result', None)

    def scales_weight_reference_to_date_tray(self, id: int, var_date: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantWeightReference]:
        '''
        Parameters:
            id (int)
            var_date (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantWeightReference]
        """'''
        result = self._ScalesApi.scales_weight_reference_to_date_tray(id, var_date, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_plant_weight_reference_by_tray_idto_date_result', None)

    def scales_weight_reference_tray(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantWeightReference]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantWeightReference]
        """'''
        result = self._ScalesApi.scales_weight_reference_tray(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_plant_weight_reference_by_tray_id_result', None)

    def scan3d(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Scan3DImaging]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Scan3DImaging]
        """'''
        result = self._Scan3dApi.scan3d(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_imaging_result', None)

    def scan3d_analyzed_model(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Scan3DAnalyzedModel]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Scan3DAnalyzedModel]
        """'''
        result = self._Scan3dApi.scan3d_analyzed_model(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_analyzed_model_result', None)

    def scan3d_analyzed_model_analyse(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Scan3DAnalyzedModel]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Scan3DAnalyzedModel]
        """'''
        result = self._Scan3dApi.scan3d_analyzed_model_analyse(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_analyzed_model_by_analyse_id_result', None)

    def scan3d_analyzed_model_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Scan3DAnalyzedModel]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Scan3DAnalyzedModel]
        """'''
        result = self._Scan3dApi.scan3d_analyzed_model_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_analyzed_model_by_measure_id_result', None)

    def scan3d_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MeasureExtendedData:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MeasureExtendedData
        """'''
        result = self._Scan3dApi.scan3d_imaging_extended_data(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_measure_extended_data_result', None)

    def scan3d_imaging_extended_data_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> MeasureExtendedData:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            MeasureExtendedData
        """'''
        result = self._Scan3dApi.scan3d_imaging_extended_data_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_measure_extended_data_by_id_result', None)

    def scan3d_imaging_measure(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Scan3DImaging:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Scan3DImaging
        """'''
        result = self._Scan3dApi.scan3d_imaging_measure(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_imaging_by_id_result', None)

    def scan3d_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[LeafParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[LeafParameter]
        """'''
        result = self._Scan3dApi.scan3d_leaf_param(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_leaf_param_result', None)

    def scan3d_leaf_param_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[LeafParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[LeafParameter]
        """'''
        result = self._Scan3dApi.scan3d_leaf_param_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_leaf_param_by_analyse_id_result', None)

    def scan3d_param(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Parameter:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Parameter
        """'''
        result = self._Scan3dApi.scan3d_param(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_param_result', None)

    def scan3d_param_used(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._Scan3dApi.scan3d_param_used(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_used_param_result', None)

    def scan3d_param_used_analyse(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Parameter]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Parameter]
        """'''
        result = self._Scan3dApi.scan3d_param_used_analyse(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_used_param_by_analyse_id_result', None)

    def scan3d_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantParameter]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantParameter]
        """'''
        result = self._Scan3dApi.scan3d_plant_param(device_id, round_id, tray_id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_plant_param_result', None)

    def scan3d_plant_param_analyse(self, id: int, param_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[PlantParameter]:
        '''
        Parameters:
            id (int)
            param_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[PlantParameter]
        """'''
        result = self._Scan3dApi.scan3d_plant_param_analyse(id, param_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scan3d_plant_param_by_analyse_id_result', None)

    def spectrum_device(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> SpectrumDevice:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            SpectrumDevice
        """'''
        result = self._SpectrumDeviceApi.spectrum_device(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_spectrum_device_result', None)

    def spectrum_device_id(self, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[SpectrumDeviceID]:
        '''
        Parameters:
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[SpectrumDeviceID]
        """'''
        result = self._SpectrumDeviceApi.spectrum_device_id(_request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_spectrum_device_id_result', None)

    def spectrum_values_date_device(self, id: int, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[SpectrumValues]:
        '''
        Parameters:
            id (int)
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[SpectrumValues]
        """'''
        result = self._SpectrumDeviceApi.spectrum_values_date_device(id, start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_spectrum_values_result', None)

    def spray_action(self, device_id: int, round_id: int, tray_id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[SprayAction]:
        '''
        Parameters:
            device_id (int)
            round_id (int)
            tray_id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[SprayAction]
        """'''
        result = self._SprayApi.spray_action(device_id, round_id, tray_id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_spray_action_result', None)

    def system_log_date_log_tag(self, tag: str, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[SystemLog]:
        '''
        Parameters:
            tag (str)
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[SystemLog]
        """'''
        result = self._SystemLogApi.system_log_date_log_tag(tag, start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_system_log_by_log_tag_and_date_result', None)

    def system_log_date_log_type(self, type: str, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[SystemLog]:
        '''
        Parameters:
            type (str)
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[SystemLog]
        """'''
        result = self._SystemLogApi.system_log_date_log_type(type, start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_system_log_by_log_type_and_date_result', None)

    def system_log_date_round(self, id: int, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[SystemLog]:
        '''
        Parameters:
            id (int)
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[SystemLog]
        """'''
        result = self._SystemLogApi.system_log_date_round(id, start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_system_log_by_round_id_and_date_result', None)

    def system_log_date_tray(self, id: int, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[SystemLog]:
        '''
        Parameters:
            id (int)
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[SystemLog]
        """'''
        result = self._SystemLogApi.system_log_date_tray(id, start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_system_log_by_tray_id_and_date_result', None)

    def system_log_log_tag(self, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[LogTag]:
        '''
        Parameters:
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[LogTag]
        """'''
        result = self._SystemLogApi.system_log_log_tag(_request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_system_log_tag_result', None)

    def system_log_log_type(self, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[LogType]:
        '''
        Parameters:
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[LogType]
        """'''
        result = self._SystemLogApi.system_log_log_type(_request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_system_log_type_result', None)

    def system_log_round(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[SystemLog]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[SystemLog]
        """'''
        result = self._SystemLogApi.system_log_round(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_system_log_by_round_id_result', None)

    def system_log_tray(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[SystemLog]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[SystemLog]
        """'''
        result = self._SystemLogApi.system_log_tray(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_system_log_by_tray_id_result', None)

    def scales_mapping_tray(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[ScalesMapping]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[ScalesMapping]
        """'''
        result = self._TrayApi.scales_mapping_tray(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_scales_mapping_by_tray_id_result', None)

    def tray(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> Tray:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            Tray
        """'''
        result = self._TrayApi.tray(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_tray_result', None)

    def tray_profile(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> TrayProfile:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            TrayProfile
        """'''
        result = self._TrayApi.tray_profile(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_tray_profile_by_id_result', None)

    def tray_profile_to_date_tray(self, id: int, var_date: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> TrayProfile:
        '''
        Parameters:
            id (int)
            var_date (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            TrayProfile
        """'''
        result = self._TrayApi.tray_profile_to_date_tray(id, var_date, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_tray_profile_by_tray_idto_date_result', None)

    def tray_profile_tray(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[TrayProfile]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[TrayProfile]
        """'''
        result = self._TrayApi.tray_profile_tray(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_tray_profile_by_tray_id_result', None)

    def tray_profile_used_tray(self, id: int, start: datetime, stop: datetime, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[TrayProfile]:
        '''
        Parameters:
            id (int)
            start (datetime)
            stop (datetime)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[TrayProfile]
        """'''
        result = self._TrayApi.tray_profile_used_tray(id, start, stop, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_used_tray_profile_by_tray_id_result', None)

    def tray_round(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> List[Tray]:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            List[Tray]
        """'''
        result = self._TrayApi.tray_round(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_tray_by_round_id_result', None)

    def tray_type(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> TrayType:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            TrayType
        """'''
        result = self._TrayApi.tray_type(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_tray_type_result', None)

    def tray_type_tray(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> TrayType:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            TrayType
        """'''
        result = self._TrayApi.tray_type_tray(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_tray_type_by_tray_id_result', None)

    def tray_type_tray_profile(self, id: int, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> TrayType:
        '''
        Parameters:
            id (int)
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            TrayType
        """'''
        result = self._TrayApi.tray_type_tray_profile(id, _request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_tray_type_by_tray_profile_id_result', None)

    def version_info(self, _request_timeout: Optional[Union[float, Tuple[float, float]]]=None, _request_auth: Optional[Dict[str, Any]]=None, _content_type: Optional[str]=None, _headers: Optional[Dict[str, Any]]=None, _host_index: int=0) -> VersionInfo:
        '''
        Parameters:
            _request_timeout (Optional[Union[float, Tuple[float, float]]])
            _request_auth (Optional[Dict[str, Any]])
            _content_type (Optional[str])
            _headers (Optional[Dict[str, Any]])
            _host_index (int)
        Returns:
            VersionInfo
        """'''
        result = self._VersionInfoApi.version_info(_request_timeout, _request_auth, _content_type, _headers, _host_index)
        return getattr(result, 'json_version_info_result', None)