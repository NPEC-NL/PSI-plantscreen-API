# coding: utf-8
"""
Auto-generated API client wrapper with direct methods for all endpoints.
"""
from plantscreen.api_client import ApiClient
from plantscreen.configuration import Configuration
import plantscreen.api as api_module
from typing import Any, Optional, Union, Tuple, List, Dict
from datetime import datetime
from plantscreen.models import Action, ActionGroup, ActionProtocol, BufferHistory, Device, Experiment, ExperimentIDWrapper, ExperimentNote, FcImaging, HcImaging, HcRgbImage, Imaging, LeafParameter, LogTag, LogType, MeasureExtendedData, MscCalibration, MscCalibrationLight, MscCalibrationLight200Response, MscLightSet, Owner, OwnerIDWrapper, Parameter, ParameterImage, Plant, PlantHeight, PlantLeaf, PlantMask, PlantParameter, PlantWeightReference, Probe, Probe200Response, ProbeValue, ProfileIDWrapper, RgbGreeningMaskImage, Round, RoundOrder, ScalesData, ScalesMapping, Scan3DAnalyzedModel, Scan3DImaging, SpectrumDevice, SpectrumDeviceID, SpectrumDeviceWavelengthsJSONWrapper, SpectrumValues, SprayAction, StatisticLeafParameter, StatisticPlantParameter, SystemLog, SystemProfile, Tray, TrayProfile, TrayType, VersionInfo



class CompleteAPIClient(ApiClient):
    def __init__(self, url: str, *args: Any, **kwargs: Any) -> None:
        self.file_api = ApiClient(Configuration(host=url + "/RestService"))
        super().__init__(Configuration(host=url + "/RestService/json"), *args, **kwargs)
        self._ActionApi: api_module.ActionApi = api_module.ActionApi(self)
        self._BufferApi: api_module.BufferApi = api_module.BufferApi(self)
        self._DeviceApi: api_module.DeviceApi = api_module.DeviceApi(self)
        self._ExperimentApi: api_module.ExperimentApi = api_module.ExperimentApi(self)
        self._FcApi: api_module.FcApi = api_module.FcApi(self)
        self._FileApi: api_module.FileApi = api_module.FileApi(self.file_api)
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

    def action(self, id: int) -> Action:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Action
        """
        result = self._ActionApi.action(id)
        return getattr(result, "json_action_result", None)

    def action_experiment(self, id: int) -> List[Action]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Action]
        """
        result = self._ActionApi.action_experiment(id)
        return getattr(result, "json_action_by_experiment_id_result", None)

    def action_group(self, id: int) -> ActionGroup:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            ActionGroup
        """
        result = self._ActionApi.action_group(id)
        return getattr(result, "json_action_group_result", None)

    def action_group_round(self, id: int) -> ActionGroup:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            ActionGroup
        """
        result = self._ActionApi.action_group_round(id)
        return getattr(result, "json_action_group_by_round_id_result", None)

    def action_not_done_experiment(self, id: int) -> List[Action]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Action]
        """
        result = self._ActionApi.action_not_done_experiment(id)
        return getattr(result, "json_action_by_experiment_id_not_done_result", None)

    def action_protocol(self, id: int) -> ActionProtocol:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            ActionProtocol
        """
        result = self._ActionApi.action_protocol(id)
        return getattr(result, "json_action_protocol_result", None)

    def action_protocol_round(self, id: int) -> ActionProtocol:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            ActionProtocol
        """
        result = self._ActionApi.action_protocol_round(id)
        return getattr(result, "json_action_protocol_by_round_id_result", None)

    def buffer_history(self, id: int) -> BufferHistory:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            BufferHistory
        """
        result = self._BufferApi.buffer_history(id)
        return getattr(result, "json_buffer_history_result", None)

    def buffer_history_date(self, start: datetime, stop: datetime) -> List[BufferHistory]:
        """
        Args:
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[BufferHistory]
        """
        result = self._BufferApi.buffer_history_date(start, stop)
        return getattr(result, "json_buffer_history_by_date_result", None)

    def device(self, id: int) -> Device:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Device
        """
        result = self._DeviceApi.device(id)
        return getattr(result, "json_device_result", None)

    def device_active(self) -> List[Device]:
        result = self._DeviceApi.device_active()
        return getattr(result, "json_device_active_result", None)

    def device_profile(self, id: int) -> List[Device]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Device]
        """
        result = self._DeviceApi.device_profile(id)
        return getattr(result, "json_device_by_profile_id_result", None)

    def experiment(self, id: int) -> Experiment:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Experiment
        """
        result = self._ExperimentApi.experiment(id)
        return getattr(result, "json_experiment_result", None)

    def experiment_date(self, start: datetime, stop: datetime) -> List[Experiment]:
        """
        Args:
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[Experiment]
        """
        result = self._ExperimentApi.experiment_date(start, stop)
        return getattr(result, "json_experiment_by_date_result", None)

    def experiment_id(self) -> List[ExperimentIDWrapper]:
        result = self._ExperimentApi.experiment_id()
        return getattr(result, "json_experiment_id_result", None)

    def experiment_owner(self, id: int) -> List[Experiment]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Experiment]
        """
        result = self._ExperimentApi.experiment_owner(id)
        return getattr(result, "json_experiment_by_owner_result", None)

    def note_experiment(self, id: int) -> List[ExperimentNote]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[ExperimentNote]
        """
        result = self._ExperimentApi.note_experiment(id)
        return getattr(result, "json_note_result", None)

    def owner(self, ids: List[int]) -> List[Owner]:
        """
        Args:
            ids (List[int]): list of IDs of the resources.
        Returns:
            List[Owner]
        """
        result = self._ExperimentApi.owner(ids)
        return getattr(result, "json_owner_result", None)

    def owner_id(self) -> List[OwnerIDWrapper]:
        result = self._ExperimentApi.owner_id()
        return getattr(result, "json_owner_id_result", None)

    def fc_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[FcImaging]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[FcImaging]
        """
        result = self._FcApi.fc_imaging(device_id, round_id, tray_id)
        return getattr(result, "json_fc_imaging_result", None)

    def fc_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> MeasureExtendedData:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            MeasureExtendedData
        """
        result = self._FcApi.fc_imaging_extended_data(device_id, round_id, tray_id)
        return getattr(result, "json_fc_measure_extended_data_result", None)

    def fc_imaging_extended_data_measure(self, id: int) -> MeasureExtendedData:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            MeasureExtendedData
        """
        result = self._FcApi.fc_imaging_extended_data_measure(id)
        return getattr(result, "json_fc_measure_extended_data_by_id_result", None)

    def fc_imaging_measure(self, id: int) -> FcImaging:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            FcImaging
        """
        result = self._FcApi.fc_imaging_measure(id)
        return getattr(result, "json_fc_imaging_by_id_result", None)

    def fc_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[LeafParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[LeafParameter]
        """
        result = self._FcApi.fc_leaf_param(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_fc_leaf_param_result", None)

    def fc_leaf_param_analyse(self, id: int, param_id: int) -> List[LeafParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[LeafParameter]
        """
        result = self._FcApi.fc_leaf_param_analyse(id, param_id)
        return getattr(result, "json_fc_leaf_param_by_analyse_id_result", None)

    def fc_param(self, id: int) -> Parameter:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Parameter
        """
        result = self._FcApi.fc_param(id)
        return getattr(result, "json_fc_param_result", None)

    def fc_param_image(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[ParameterImage]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[ParameterImage]
        """
        result = self._FcApi.fc_param_image(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_fc_parameter_image_result", None)

    def fc_param_image_analyse(self, id: int, param_id: int) -> ParameterImage:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            ParameterImage
        """
        result = self._FcApi.fc_param_image_analyse(id, param_id)
        return getattr(result, "json_fc_parameter_image_by_analyse_id_result", None)

    def fc_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[Parameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Parameter]
        """
        result = self._FcApi.fc_param_used(device_id, round_id, tray_id)
        return getattr(result, "json_fc_used_param_result", None)

    def fc_param_used_analyse(self, id: int) -> List[Parameter]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Parameter]
        """
        result = self._FcApi.fc_param_used_analyse(id)
        return getattr(result, "json_fc_used_param_by_analyse_id_result", None)

    def fc_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> List[PlantMask]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[PlantMask]
        """
        result = self._FcApi.fc_plant_mask(device_id, round_id, tray_id)
        return getattr(result, "json_fc_plant_mask_result", None)

    def fc_plant_mask_measure(self, id: int) -> PlantMask:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            PlantMask
        """
        result = self._FcApi.fc_plant_mask_measure(id)
        return getattr(result, "json_fc_plant_mask_by_measure_id_result", None)

    def fc_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[PlantParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[PlantParameter]
        """
        result = self._FcApi.fc_plant_param(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_fc_plant_param_result", None)

    def fc_plant_param_analyse(self, id: int, param_id: int) -> List[PlantParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[PlantParameter]
        """
        result = self._FcApi.fc_plant_param_analyse(id, param_id)
        return getattr(result, "json_fc_plant_param_by_analyse_id_result", None)

    def file(self, path: str) -> None:
        """
        Args:
            path (str):
        Returns:
            None
        """
        return self._FileApi.file(path)

    def file_changelog(self) -> str:
        return self._FileApi.file_changelog()

    def hc_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[HcImaging]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[HcImaging]
        """
        result = self._HcApi.hc_imaging(device_id, round_id, tray_id)
        return getattr(result, "json_hc_imaging_result", None)

    def hc_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> MeasureExtendedData:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            MeasureExtendedData
        """
        result = self._HcApi.hc_imaging_extended_data(device_id, round_id, tray_id)
        return getattr(result, "json_hc_measure_extended_data_result", None)

    def hc_imaging_extended_data_measure(self, id: int) -> MeasureExtendedData:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            MeasureExtendedData
        """
        result = self._HcApi.hc_imaging_extended_data_measure(id)
        return getattr(result, "json_hc_measure_extended_data_by_id_result", None)

    def hc_imaging_measure(self, id: int) -> HcImaging:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            HcImaging
        """
        result = self._HcApi.hc_imaging_measure(id)
        return getattr(result, "json_hc_imaging_by_id_result", None)

    def hc_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[StatisticLeafParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[StatisticLeafParameter]
        """
        result = self._HcApi.hc_leaf_param(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_hc_leaf_param_result", None)

    def hc_leaf_param_analyse(self, id: int, param_id: int) -> List[StatisticLeafParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[StatisticLeafParameter]
        """
        result = self._HcApi.hc_leaf_param_analyse(id, param_id)
        return getattr(result, "json_hc_leaf_param_by_analyse_id_result", None)

    def hc_param(self, id: int) -> Parameter:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Parameter
        """
        result = self._HcApi.hc_param(id)
        return getattr(result, "json_hc_param_result", None)

    def hc_param_image(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[ParameterImage]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[ParameterImage]
        """
        result = self._HcApi.hc_param_image(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_hc_parameter_image_result", None)

    def hc_param_image_analyse(self, id: int, param_id: int) -> ParameterImage:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            ParameterImage
        """
        result = self._HcApi.hc_param_image_analyse(id, param_id)
        return getattr(result, "json_hc_parameter_image_by_analyse_id_result", None)

    def hc_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[Parameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Parameter]
        """
        result = self._HcApi.hc_param_used(device_id, round_id, tray_id)
        return getattr(result, "json_hc_used_param_result", None)

    def hc_param_used_analyse(self, id: int) -> List[Parameter]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Parameter]
        """
        result = self._HcApi.hc_param_used_analyse(id)
        return getattr(result, "json_hc_used_param_by_analyse_id_result", None)

    def hc_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> List[PlantMask]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[PlantMask]
        """
        result = self._HcApi.hc_plant_mask(device_id, round_id, tray_id)
        return getattr(result, "json_hc_plant_mask_result", None)

    def hc_plant_mask_measure(self, id: int) -> PlantMask:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            PlantMask
        """
        result = self._HcApi.hc_plant_mask_measure(id)
        return getattr(result, "json_hc_plant_mask_by_measure_id_result", None)

    def hc_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[StatisticPlantParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[StatisticPlantParameter]
        """
        result = self._HcApi.hc_plant_param(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_hc_plant_param_result", None)

    def hc_plant_param_analyse(self, id: int, param_id: int) -> List[StatisticPlantParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[StatisticPlantParameter]
        """
        result = self._HcApi.hc_plant_param_analyse(id, param_id)
        return getattr(result, "json_hc_plant_param_by_analyse_id_result", None)

    def hc_rgb_image(self, device_id: int, round_id: int, tray_id: int) -> List[HcRgbImage]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[HcRgbImage]
        """
        result = self._HcApi.hc_rgb_image(device_id, round_id, tray_id)
        return getattr(result, "json_hc_rgb_image_result", None)

    def hc_rgb_image_measure(self, id: int) -> HcRgbImage:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            HcRgbImage
        """
        result = self._HcApi.hc_rgb_image_measure(id)
        return getattr(result, "json_hc_rgb_image_by_measure_id_result", None)

    def ir_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[Imaging]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Imaging]
        """
        result = self._IrApi.ir_imaging(device_id, round_id, tray_id)
        return getattr(result, "json_ir_imaging_result", None)

    def ir_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> MeasureExtendedData:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            MeasureExtendedData
        """
        result = self._IrApi.ir_imaging_extended_data(device_id, round_id, tray_id)
        return getattr(result, "json_ir_measure_extended_data_result", None)

    def ir_imaging_extended_data_measure(self, id: int) -> MeasureExtendedData:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            MeasureExtendedData
        """
        result = self._IrApi.ir_imaging_extended_data_measure(id)
        return getattr(result, "json_ir_measure_extended_data_by_id_result", None)

    def ir_imaging_measure(self, id: int) -> Imaging:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Imaging
        """
        result = self._IrApi.ir_imaging_measure(id)
        return getattr(result, "json_ir_imaging_by_id_result", None)

    def ir_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[StatisticLeafParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[StatisticLeafParameter]
        """
        result = self._IrApi.ir_leaf_param(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_ir_leaf_param_result", None)

    def ir_leaf_param_analyse(self, id: int, param_id: int) -> List[StatisticLeafParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[StatisticLeafParameter]
        """
        result = self._IrApi.ir_leaf_param_analyse(id, param_id)
        return getattr(result, "json_ir_leaf_param_by_analyse_id_result", None)

    def ir_param(self, id: int) -> Parameter:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Parameter
        """
        result = self._IrApi.ir_param(id)
        return getattr(result, "json_ir_param_result", None)

    def ir_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[Parameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Parameter]
        """
        result = self._IrApi.ir_param_used(device_id, round_id, tray_id)
        return getattr(result, "json_ir_used_param_result", None)

    def ir_param_used_analyse(self, id: int) -> List[Parameter]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Parameter]
        """
        result = self._IrApi.ir_param_used_analyse(id)
        return getattr(result, "json_ir_used_param_by_analyse_id_result", None)

    def ir_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> List[PlantMask]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[PlantMask]
        """
        result = self._IrApi.ir_plant_mask(device_id, round_id, tray_id)
        return getattr(result, "json_ir_plant_mask_result", None)

    def ir_plant_mask_image(self, device_id: int, round_id: int, tray_id: int) -> List[Imaging]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Imaging]
        """
        result = self._IrApi.ir_plant_mask_image(device_id, round_id, tray_id)
        return getattr(result, "json_ir_plant_mask_image_result", None)

    def ir_plant_mask_image_measure(self, id: int) -> Imaging:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Imaging
        """
        result = self._IrApi.ir_plant_mask_image_measure(id)
        return getattr(result, "json_ir_plant_mask_image_by_measure_id_result", None)

    def ir_plant_mask_measure(self, id: int) -> PlantMask:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            PlantMask
        """
        result = self._IrApi.ir_plant_mask_measure(id)
        return getattr(result, "json_ir_plant_mask_by_measure_id_result", None)

    def ir_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[StatisticPlantParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[StatisticPlantParameter]
        """
        result = self._IrApi.ir_plant_param(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_ir_plant_param_result", None)

    def ir_plant_param_analyse(self, id: int, param_id: int) -> List[StatisticPlantParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[StatisticPlantParameter]
        """
        result = self._IrApi.ir_plant_param_analyse(id, param_id)
        return getattr(result, "json_ir_plant_param_by_analyse_id_result", None)

    def msc_calibration(self, id: int) -> MscCalibration:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            MscCalibration
        """
        result = self._MscApi.msc_calibration(id)
        return getattr(result, "json_msc_calibration_result", None)

    def msc_calibration_light(self, id: Optional[int] = None) -> JsonMscCalibrationLightByIDResult:
        """
        Args:
            id (Optional[int]): ID of the resource.
        Returns:
            JsonMscCalibrationLightByIDResult
        """
        result = self._MscApi.msc_calibration_light(id)
        return getattr(result, "oneof_schema_1_validator", None)

    def msc_calibration_light_set(self, id: int) -> MscCalibration:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            MscCalibration
        """
        result = self._MscApi.msc_calibration_light_set(id)
        return getattr(result, "json_msc_calibration_by_light_set_id_result", None)

    def msc_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[Imaging]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Imaging]
        """
        result = self._MscApi.msc_imaging(device_id, round_id, tray_id)
        return getattr(result, "json_msc_imaging_result", None)

    def msc_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> MeasureExtendedData:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            MeasureExtendedData
        """
        result = self._MscApi.msc_imaging_extended_data(device_id, round_id, tray_id)
        return getattr(result, "json_msc_measure_extended_data_result", None)

    def msc_imaging_extended_data_measure(self, id: int) -> MeasureExtendedData:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            MeasureExtendedData
        """
        result = self._MscApi.msc_imaging_extended_data_measure(id)
        return getattr(result, "json_msc_measure_extended_data_by_id_result", None)

    def msc_imaging_measure(self, id: int) -> List[Imaging]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Imaging]
        """
        result = self._MscApi.msc_imaging_measure(id)
        return getattr(result, "json_msc_imaging_by_id_result", None)

    def msc_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[StatisticLeafParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[StatisticLeafParameter]
        """
        result = self._MscApi.msc_leaf_param(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_msc_leaf_param_result", None)

    def msc_leaf_param_analyse(self, id: int, param_id: int) -> List[StatisticLeafParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[StatisticLeafParameter]
        """
        result = self._MscApi.msc_leaf_param_analyse(id, param_id)
        return getattr(result, "json_msc_leaf_param_by_analyse_id_result", None)

    def msc_light_set(self, id: int) -> MscLightSet:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            MscLightSet
        """
        result = self._MscApi.msc_light_set(id)
        return getattr(result, "json_msc_light_set_result", None)

    def msc_light_set_used(self, device_id: int, round_id: int, tray_id: int) -> List[MscLightSet]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[MscLightSet]
        """
        result = self._MscApi.msc_light_set_used(device_id, round_id, tray_id)
        return getattr(result, "json_msc_light_set_used_result", None)

    def msc_param(self, id: int) -> Parameter:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Parameter
        """
        result = self._MscApi.msc_param(id)
        return getattr(result, "json_msc_param_result", None)

    def msc_param_image(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[ParameterImage]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[ParameterImage]
        """
        result = self._MscApi.msc_param_image(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_msc_parameter_image_result", None)

    def msc_param_image_analyse(self, id: int, param_id: int) -> ParameterImage:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            ParameterImage
        """
        result = self._MscApi.msc_param_image_analyse(id, param_id)
        return getattr(result, "json_msc_parameter_image_by_analyse_id_result", None)

    def msc_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[Parameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Parameter]
        """
        result = self._MscApi.msc_param_used(device_id, round_id, tray_id)
        return getattr(result, "json_msc_used_param_result", None)

    def msc_param_used_analyse(self, id: int) -> List[Parameter]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Parameter]
        """
        result = self._MscApi.msc_param_used_analyse(id)
        return getattr(result, "json_msc_used_param_by_analyse_id_result", None)

    def msc_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> List[PlantMask]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[PlantMask]
        """
        result = self._MscApi.msc_plant_mask(device_id, round_id, tray_id)
        return getattr(result, "json_msc_plant_mask_result", None)

    def msc_plant_mask_measure(self, id: int) -> PlantMask:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            PlantMask
        """
        result = self._MscApi.msc_plant_mask_measure(id)
        return getattr(result, "json_msc_plant_mask_by_measure_id_result", None)

    def msc_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[StatisticPlantParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[StatisticPlantParameter]
        """
        result = self._MscApi.msc_plant_param(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_msc_plant_param_result", None)

    def msc_plant_param_analyse(self, id: int, param_id: int) -> List[StatisticPlantParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[StatisticPlantParameter]
        """
        result = self._MscApi.msc_plant_param_analyse(id, param_id)
        return getattr(result, "json_msc_plant_param_by_analyse_id_result", None)

    def plant(self, ids: List[int]) -> List[Plant]:
        """
        Args:
            ids (List[int]): list of IDs of the resources.
        Returns:
            List[Plant]
        """
        result = self._PlantApi.plant(ids)
        return getattr(result, "json_plant_result", None)

    def plant_height_round(self, id: int) -> List[PlantHeight]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[PlantHeight]
        """
        result = self._PlantApi.plant_height_round(id)
        return getattr(result, "json_plant_height_by_round_id_result", None)

    def plant_leaf(self, plant_id: int, tray_id: int) -> List[PlantLeaf]:
        """
        Args:
            plant_id (int):
            tray_id (int): ID of the tray.
        Returns:
            List[PlantLeaf]
        """
        result = self._PlantApi.plant_leaf(plant_id, tray_id)
        return getattr(result, "json_plant_leaves_by_plant_and_tray_id_result", None)

    def plant_tray(self, id: int) -> List[Plant]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Plant]
        """
        result = self._PlantApi.plant_tray(id)
        return getattr(result, "json_plant_by_tray_id_result", None)

    def plant_tray_profile(self, id: int) -> List[Plant]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Plant]
        """
        result = self._PlantApi.plant_tray_profile(id)
        return getattr(result, "json_plant_by_tray_profile_id_result", None)

    def plant_tray_profile_tray(self, id: int, start: datetime, stop: datetime) -> List[Plant]:
        """
        Args:
            id (int): ID of the resource.
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[Plant]
        """
        result = self._PlantApi.plant_tray_profile_tray(id, start, stop)
        return getattr(result, "json_plant_by_tray_id_and_dates_result", None)

    def probe(self, id: Optional[int] = None) -> JsonProbeResult:
        """
        Args:
            id (Optional[int]): ID of the resource.
        Returns:
            JsonProbeResult
        """
        result = self._ProbeApi.probe(id)
        return getattr(result, "oneof_schema_1_validator", None)

    def probe_value_date(self, start: datetime, stop: datetime) -> List[ProbeValue]:
        """
        Args:
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[ProbeValue]
        """
        result = self._ProbeApi.probe_value_date(start, stop)
        return getattr(result, "json_probe_value_by_date_result", None)

    def probe_value_date_probe(self, id: int, start: datetime, stop: datetime) -> List[ProbeValue]:
        """
        Args:
            id (int): ID of the resource.
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[ProbeValue]
        """
        result = self._ProbeApi.probe_value_date_probe(id, start, stop)
        return getattr(result, "json_probe_value_by_id_and_date_result", None)

    def profile(self, id: int) -> SystemProfile:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            SystemProfile
        """
        result = self._ProfileApi.profile(id)
        return getattr(result, "json_system_profile_result", None)

    def profile_active(self) -> SystemProfile:
        result = self._ProfileApi.profile_active()
        return getattr(result, "json_system_profile_active_result", None)

    def profile_id(self) -> List[ProfileIDWrapper]:
        result = self._ProfileApi.profile_id()
        return getattr(result, "json_system_profile_id_result", None)

    def rgb_greening_mask_image(self, device_id: int, round_id: int, tray_id: int) -> List[RgbGreeningMaskImage]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[RgbGreeningMaskImage]
        """
        result = self._RgbApi.rgb_greening_mask_image(device_id, round_id, tray_id)
        return getattr(result, "json_rgb_greening_mask_image_result", None)

    def rgb_greening_mask_image_measure(self, id: int) -> RgbGreeningMaskImage:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            RgbGreeningMaskImage
        """
        result = self._RgbApi.rgb_greening_mask_image_measure(id)
        return getattr(result, "json_rgb_greening_mask_image_by_measure_id_result", None)

    def rgb_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[Imaging]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Imaging]
        """
        result = self._RgbApi.rgb_imaging(device_id, round_id, tray_id)
        return getattr(result, "json_rgb_imaging_result", None)

    def rgb_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> MeasureExtendedData:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            MeasureExtendedData
        """
        result = self._RgbApi.rgb_imaging_extended_data(device_id, round_id, tray_id)
        return getattr(result, "json_rgb_measure_extended_data_result", None)

    def rgb_imaging_extended_data_measure(self, id: int) -> MeasureExtendedData:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            MeasureExtendedData
        """
        result = self._RgbApi.rgb_imaging_extended_data_measure(id)
        return getattr(result, "json_rgb_measure_extended_data_by_id_result", None)

    def rgb_imaging_measure(self, id: int) -> Imaging:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Imaging
        """
        result = self._RgbApi.rgb_imaging_measure(id)
        return getattr(result, "json_rgb_imaging_by_id_result", None)

    def rgb_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[LeafParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[LeafParameter]
        """
        result = self._RgbApi.rgb_leaf_param(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_rgb_leaf_param_result", None)

    def rgb_leaf_param_analyse(self, id: int, param_id: int) -> List[LeafParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[LeafParameter]
        """
        result = self._RgbApi.rgb_leaf_param_analyse(id, param_id)
        return getattr(result, "json_rgb_leaf_param_by_analyse_id_result", None)

    def rgb_leaf_param_color(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[LeafParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[LeafParameter]
        """
        result = self._RgbApi.rgb_leaf_param_color(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_rgb_leaf_param_color_result", None)

    def rgb_leaf_param_color_analyse(self, id: int, param_id: int) -> List[LeafParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[LeafParameter]
        """
        result = self._RgbApi.rgb_leaf_param_color_analyse(id, param_id)
        return getattr(result, "json_rgb_leaf_param_color_by_analyse_id_result", None)

    def rgb_param(self, id: int) -> Parameter:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Parameter
        """
        result = self._RgbApi.rgb_param(id)
        return getattr(result, "json_rgb_param_result", None)

    def rgb_param_color_used(self, device_id: int, round_id: int, tray_id: int) -> List[Parameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Parameter]
        """
        result = self._RgbApi.rgb_param_color_used(device_id, round_id, tray_id)
        return getattr(result, "json_rgb_used_param_color_result", None)

    def rgb_param_color_used_analyse(self, id: int) -> List[Parameter]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Parameter]
        """
        result = self._RgbApi.rgb_param_color_used_analyse(id)
        return getattr(result, "json_rgb_used_param_color_by_analyse_id_result", None)

    def rgb_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[Parameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Parameter]
        """
        result = self._RgbApi.rgb_param_used(device_id, round_id, tray_id)
        return getattr(result, "json_rgb_used_params_result", None)

    def rgb_param_used_analyse(self, id: int) -> List[Parameter]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Parameter]
        """
        result = self._RgbApi.rgb_param_used_analyse(id)
        return getattr(result, "json_rgb_used_param_by_analyse_id_result", None)

    def rgb_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> List[PlantMask]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[PlantMask]
        """
        result = self._RgbApi.rgb_plant_mask(device_id, round_id, tray_id)
        return getattr(result, "json_rgb_plant_mask_result", None)

    def rgb_plant_mask_measure(self, id: int) -> PlantMask:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            PlantMask
        """
        result = self._RgbApi.rgb_plant_mask_measure(id)
        return getattr(result, "json_rgb_plant_mask_by_measure_id_result", None)

    def rgb_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[PlantParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[PlantParameter]
        """
        result = self._RgbApi.rgb_plant_param(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_rgb_plant_param_result", None)

    def rgb_plant_param_analyse(self, id: int, param_id: int) -> List[PlantParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[PlantParameter]
        """
        result = self._RgbApi.rgb_plant_param_analyse(id, param_id)
        return getattr(result, "json_rgb_plant_param_by_analyse_id_result", None)

    def rgb_plant_param_color(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[PlantParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[PlantParameter]
        """
        result = self._RgbApi.rgb_plant_param_color(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_rgb_plant_param_color_result", None)

    def rgb_plant_param_color_analyse(self, id: int, param_id: int) -> List[PlantParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[PlantParameter]
        """
        result = self._RgbApi.rgb_plant_param_color_analyse(id, param_id)
        return getattr(result, "json_rgb_plant_param_color_by_analyse_id_result", None)

    def round(self, id: int) -> Round:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Round
        """
        result = self._RoundApi.round(id)
        return getattr(result, "json_round_result", None)

    def round_date_experiment(self, id: int, start: datetime, stop: datetime) -> List[Round]:
        """
        Args:
            id (int): ID of the resource.
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[Round]
        """
        result = self._RoundApi.round_date_experiment(id, start, stop)
        return getattr(result, "json_round_by_experiment_id_and_date_result", None)

    def round_experiment(self, id: int) -> List[Round]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Round]
        """
        result = self._RoundApi.round_experiment(id)
        return getattr(result, "json_round_by_experiment_id_result", None)

    def round_order_date_experiment(self, id: int, start: datetime, stop: datetime) -> List[RoundOrder]:
        """
        Args:
            id (int): ID of the resource.
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[RoundOrder]
        """
        result = self._RoundApi.round_order_date_experiment(id, start, stop)
        return getattr(result, "json_round_order_by_experiment_id_and_date_result", None)

    def round_order_experiment(self, id: int) -> List[RoundOrder]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[RoundOrder]
        """
        result = self._RoundApi.round_order_experiment(id)
        return getattr(result, "json_round_order_by_experiment_id_result", None)

    def round_order_round(self, id: int) -> RoundOrder:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            RoundOrder
        """
        result = self._RoundApi.round_order_round(id)
        return getattr(result, "json_round_order_result", None)

    def scales_plant_weight(self, device_id: int, round_id: int, tray_id: int) -> List[ScalesData]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[ScalesData]
        """
        result = self._ScalesApi.scales_plant_weight(device_id, round_id, tray_id)
        return getattr(result, "json_scales_measure_result", None)

    def scales_plant_weight_measure(self, id: int) -> ScalesData:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            ScalesData
        """
        result = self._ScalesApi.scales_plant_weight_measure(id)
        return getattr(result, "json_scales_measure_by_id_result", None)

    def scales_weight_reference_plant(self, id: int) -> PlantWeightReference:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            PlantWeightReference
        """
        result = self._ScalesApi.scales_weight_reference_plant(id)
        return getattr(result, "json_plant_weight_reference_by_plant_id_result", None)

    def scales_weight_reference_to_date_tray(self, id: int, var_date: datetime) -> List[PlantWeightReference]:
        """
        Args:
            id (int): ID of the resource.
            var_date (datetime):
        Returns:
            List[PlantWeightReference]
        """
        result = self._ScalesApi.scales_weight_reference_to_date_tray(id, var_date)
        return getattr(result, "json_plant_weight_reference_by_tray_idto_date_result", None)

    def scales_weight_reference_tray(self, id: int) -> List[PlantWeightReference]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[PlantWeightReference]
        """
        result = self._ScalesApi.scales_weight_reference_tray(id)
        return getattr(result, "json_plant_weight_reference_by_tray_id_result", None)

    def scan3d(self, device_id: int, round_id: int, tray_id: int) -> List[Scan3DImaging]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Scan3DImaging]
        """
        result = self._Scan3dApi.scan3d(device_id, round_id, tray_id)
        return getattr(result, "json_scan3d_imaging_result", None)

    def scan3d_analyzed_model(self, device_id: int, round_id: int, tray_id: int) -> List[Scan3DAnalyzedModel]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Scan3DAnalyzedModel]
        """
        result = self._Scan3dApi.scan3d_analyzed_model(device_id, round_id, tray_id)
        return getattr(result, "json_scan3d_analyzed_model_result", None)

    def scan3d_analyzed_model_analyse(self, id: int) -> List[Scan3DAnalyzedModel]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Scan3DAnalyzedModel]
        """
        result = self._Scan3dApi.scan3d_analyzed_model_analyse(id)
        return getattr(result, "json_scan3d_analyzed_model_by_analyse_id_result", None)

    def scan3d_analyzed_model_measure(self, id: int) -> List[Scan3DAnalyzedModel]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Scan3DAnalyzedModel]
        """
        result = self._Scan3dApi.scan3d_analyzed_model_measure(id)
        return getattr(result, "json_scan3d_analyzed_model_by_measure_id_result", None)

    def scan3d_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> MeasureExtendedData:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            MeasureExtendedData
        """
        result = self._Scan3dApi.scan3d_imaging_extended_data(device_id, round_id, tray_id)
        return getattr(result, "json_scan3d_measure_extended_data_result", None)

    def scan3d_imaging_extended_data_measure(self, id: int) -> MeasureExtendedData:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            MeasureExtendedData
        """
        result = self._Scan3dApi.scan3d_imaging_extended_data_measure(id)
        return getattr(result, "json_scan3d_measure_extended_data_by_id_result", None)

    def scan3d_imaging_measure(self, id: int) -> Scan3DImaging:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Scan3DImaging
        """
        result = self._Scan3dApi.scan3d_imaging_measure(id)
        return getattr(result, "json_scan3d_imaging_by_id_result", None)

    def scan3d_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[LeafParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[LeafParameter]
        """
        result = self._Scan3dApi.scan3d_leaf_param(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_scan3d_leaf_param_result", None)

    def scan3d_leaf_param_analyse(self, id: int, param_id: int) -> List[LeafParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[LeafParameter]
        """
        result = self._Scan3dApi.scan3d_leaf_param_analyse(id, param_id)
        return getattr(result, "json_scan3d_leaf_param_by_analyse_id_result", None)

    def scan3d_param(self, id: int) -> Parameter:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Parameter
        """
        result = self._Scan3dApi.scan3d_param(id)
        return getattr(result, "json_scan3d_param_result", None)

    def scan3d_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[Parameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[Parameter]
        """
        result = self._Scan3dApi.scan3d_param_used(device_id, round_id, tray_id)
        return getattr(result, "json_scan3d_used_param_result", None)

    def scan3d_param_used_analyse(self, id: int) -> List[Parameter]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Parameter]
        """
        result = self._Scan3dApi.scan3d_param_used_analyse(id)
        return getattr(result, "json_scan3d_used_param_by_analyse_id_result", None)

    def scan3d_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[PlantParameter]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
            param_id (int): ID of the parameter.
        Returns:
            List[PlantParameter]
        """
        result = self._Scan3dApi.scan3d_plant_param(device_id, round_id, tray_id, param_id)
        return getattr(result, "json_scan3d_plant_param_result", None)

    def scan3d_plant_param_analyse(self, id: int, param_id: int) -> List[PlantParameter]:
        """
        Args:
            id (int): ID of the resource.
            param_id (int): ID of the parameter.
        Returns:
            List[PlantParameter]
        """
        result = self._Scan3dApi.scan3d_plant_param_analyse(id, param_id)
        return getattr(result, "json_scan3d_plant_param_by_analyse_id_result", None)

    def spectrum_device(self, id: int) -> SpectrumDevice:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            SpectrumDevice
        """
        result = self._SpectrumDeviceApi.spectrum_device(id)
        return getattr(result, "json_spectrum_device_result", None)

    def spectrum_device_id(self) -> List[SpectrumDeviceID]:
        result = self._SpectrumDeviceApi.spectrum_device_id()
        return getattr(result, "json_spectrum_device_id_result", None)

    def spectrum_values_date_device(self, id: int, start: datetime, stop: datetime) -> List[SpectrumValues]:
        """
        Args:
            id (int): ID of the resource.
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[SpectrumValues]
        """
        result = self._SpectrumDeviceApi.spectrum_values_date_device(id, start, stop)
        return getattr(result, "json_spectrum_values_result", None)

    def spray_action(self, device_id: int, round_id: int, tray_id: int) -> List[SprayAction]:
        """
        Args:
            device_id (int): ID of the device.
            round_id (int): ID of the round.
            tray_id (int): ID of the tray.
        Returns:
            List[SprayAction]
        """
        result = self._SprayApi.spray_action(device_id, round_id, tray_id)
        return getattr(result, "json_spray_action_result", None)

    def system_log_date_log_tag(self, tag: str, start: datetime, stop: datetime) -> List[SystemLog]:
        """
        Args:
            tag (str):
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[SystemLog]
        """
        result = self._SystemLogApi.system_log_date_log_tag(tag, start, stop)
        return getattr(result, "json_system_log_by_log_tag_and_date_result", None)

    def system_log_date_log_type(self, type: str, start: datetime, stop: datetime) -> List[SystemLog]:
        """
        Args:
            type (str):
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[SystemLog]
        """
        result = self._SystemLogApi.system_log_date_log_type(type, start, stop)
        return getattr(result, "json_system_log_by_log_type_and_date_result", None)

    def system_log_date_round(self, id: int, start: datetime, stop: datetime) -> List[SystemLog]:
        """
        Args:
            id (int): ID of the resource.
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[SystemLog]
        """
        result = self._SystemLogApi.system_log_date_round(id, start, stop)
        return getattr(result, "json_system_log_by_round_id_and_date_result", None)

    def system_log_date_tray(self, id: int, start: datetime, stop: datetime) -> List[SystemLog]:
        """
        Args:
            id (int): ID of the resource.
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[SystemLog]
        """
        result = self._SystemLogApi.system_log_date_tray(id, start, stop)
        return getattr(result, "json_system_log_by_tray_id_and_date_result", None)

    def system_log_log_tag(self) -> List[LogTag]:
        result = self._SystemLogApi.system_log_log_tag()
        return getattr(result, "json_system_log_tag_result", None)

    def system_log_log_type(self) -> List[LogType]:
        result = self._SystemLogApi.system_log_log_type()
        return getattr(result, "json_system_log_type_result", None)

    def system_log_round(self, id: int) -> List[SystemLog]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[SystemLog]
        """
        result = self._SystemLogApi.system_log_round(id)
        return getattr(result, "json_system_log_by_round_id_result", None)

    def system_log_tray(self, id: int) -> List[SystemLog]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[SystemLog]
        """
        result = self._SystemLogApi.system_log_tray(id)
        return getattr(result, "json_system_log_by_tray_id_result", None)

    def scales_mapping_tray(self, id: int) -> List[ScalesMapping]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[ScalesMapping]
        """
        result = self._TrayApi.scales_mapping_tray(id)
        return getattr(result, "json_scales_mapping_by_tray_id_result", None)

    def tray(self, id: int) -> Tray:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            Tray
        """
        result = self._TrayApi.tray(id)
        return getattr(result, "json_tray_result", None)

    def tray_profile(self, id: int) -> TrayProfile:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            TrayProfile
        """
        result = self._TrayApi.tray_profile(id)
        return getattr(result, "json_tray_profile_by_id_result", None)

    def tray_profile_to_date_tray(self, id: int, var_date: datetime) -> TrayProfile:
        """
        Args:
            id (int): ID of the resource.
            var_date (datetime):
        Returns:
            TrayProfile
        """
        result = self._TrayApi.tray_profile_to_date_tray(id, var_date)
        return getattr(result, "json_tray_profile_by_tray_idto_date_result", None)

    def tray_profile_tray(self, id: int) -> List[TrayProfile]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[TrayProfile]
        """
        result = self._TrayApi.tray_profile_tray(id)
        return getattr(result, "json_tray_profile_by_tray_id_result", None)

    def tray_profile_used_tray(self, id: int, start: datetime, stop: datetime) -> List[TrayProfile]:
        """
        Args:
            id (int): ID of the resource.
            start (datetime): Start datetime for filtering results.
            stop (datetime): Stop datetime for filtering results.
        Returns:
            List[TrayProfile]
        """
        result = self._TrayApi.tray_profile_used_tray(id, start, stop)
        return getattr(result, "json_used_tray_profile_by_tray_id_result", None)

    def tray_round(self, id: int) -> List[Tray]:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            List[Tray]
        """
        result = self._TrayApi.tray_round(id)
        return getattr(result, "json_tray_by_round_id_result", None)

    def tray_type(self, id: int) -> TrayType:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            TrayType
        """
        result = self._TrayApi.tray_type(id)
        return getattr(result, "json_tray_type_result", None)

    def tray_type_tray(self, id: int) -> TrayType:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            TrayType
        """
        result = self._TrayApi.tray_type_tray(id)
        return getattr(result, "json_tray_type_by_tray_id_result", None)

    def tray_type_tray_profile(self, id: int) -> TrayType:
        """
        Args:
            id (int): ID of the resource.
        Returns:
            TrayType
        """
        result = self._TrayApi.tray_type_tray_profile(id)
        return getattr(result, "json_tray_type_by_tray_profile_id_result", None)

    def version_info(self) -> VersionInfo:
        result = self._VersionInfoApi.version_info()
        return getattr(result, "json_version_info_result", None)
