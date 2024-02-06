import plantscreen.swagger_client as swagger_client
import plantscreen.models as models
from typing import List


class PSI_API():
    """Wrapper around the automatically  generated swagger client.
       return class instances instead of dictionaries."""
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
        self.fc_api = swagger_client.FcApi(swagger_client.ApiClient(configuration))
        self.hc_api = swagger_client.HcApi(swagger_client.ApiClient(configuration))
        self.ir_api = swagger_client.IrApi(swagger_client.ApiClient(configuration))        
        self.probe_api = swagger_client.ProbeApi(swagger_client.ApiClient(configuration))
        self.msc_api = swagger_client.MscApi(swagger_client.ApiClient(configuration))
        self.rgb_api = swagger_client.RgbApi(swagger_client.ApiClient(configuration))
        self.scan3d_api = swagger_client.Scan3dApi(swagger_client.ApiClient(configuration))
        self.scales_api = swagger_client.ScalesApi(swagger_client.ApiClient(configuration))
        self.spray_api = swagger_client.SprayApi(swagger_client.ApiClient(configuration))
        self.spectrum_device_api = swagger_client.SpectrumDeviceApi(swagger_client.ApiClient(configuration))
        self.buffer_api = swagger_client.BufferApi(swagger_client.ApiClient(configuration))
        self.system_log_api = swagger_client.SystemLogApi(swagger_client.ApiClient(configuration))
        self.file_api = swagger_client.FileApi(swagger_client.ApiClient(configuration))
        self.version_info_api = swagger_client.VersionInfoApi(swagger_client.ApiClient(configuration))


    def experimentID(self) -> List[int]:
        api_response = self.exp_api.experiment_id()
        return models.experiment.ExperimentIDs.from_dict(api_response)

    def experiment(self, id) -> models.experiment.Experiment:
        api_response = self.exp_api.experiment(id)
        return models.experiment.ExperimentWrapper.from_dict(api_response)

    def experiment_date(self, start, stop) -> List[models.experiment.Experiment]:
        api_response = self.exp_api.experiment_date(start, stop)
        return models.experiment.ExperimentDate.from_dict(api_response)

    def experiment_owner(self, id) -> List[models.experiment.Experiment]:
        api_response = self.exp_api.experiment_owner(id)
        return models.experiment.ExperimentOwner.from_dict(api_response)

    def owner_id(self) -> List[int]:
        api_response = self.exp_api.owner_id()
        return models.experiment.OwnerID.from_dict(api_response)

    def owner(self, id) -> List[models.experiment.Owner]:
        api_response = self.exp_api.owner(id)
        return models.experiment.OwnerWrapper.from_dict(api_response)

    def note_experiment(self, id) -> List[models.experiment.Note]:
        api_response = self.exp_api.note_experiment(id)
        return models.experiment.NoteExperiment.from_dict(api_response)

# Round API
    def round(self, id) -> models.round.Round:
        api_response = self.round_api.round(id)
        return models.round.RoundWrapper.from_dict(api_response)

    def round_experiment(self, id) -> models.round.RoundExperiment:
        api_response = self.round_api.round_experiment(id)
        return models.round.RoundExperiment.from_dict(api_response)

    def round_date_experiment(self, id, start, stop) -> models.round.RoundDateExperiment:
        api_response = self.round_api.round_date_experiment(id, start, stop)
        return models.round.RoundDateExperiment.from_dict(api_response)

    def round_order_round(self, id) -> models.round.Order:
        api_response = self.round_api.round_order_round(id)
        return models.round.RoundOrderRound.from_dict(api_response)

    def round_order_experiment(self, id) -> models.round.RoundOrderExperiment:
        api_response = self.round_api.round_order_experiment(id)
        return models.round.RoundOrderExperiment.from_dict(api_response)

    def round_order_date_experiment(self, id, start, stop) -> models.round.RoundOrderDateExperiment:
        api_response = self.round_api.round_order_date_experiment(id, start, stop)
        return models.round.RoundOrderDateExperiment.from_dict(api_response)

# Action API
    def action(self, id) -> models.action.Action:
        api_response = self.action_api.action(id)
        return models.action.ActionWrapper.from_dict(api_response)

    def action_experiment(self, id) -> models.action.ActionExperiment:
        api_response = self.action_api.action_experiment(id)
        return models.action.ActionExperiment.from_dict(api_response)

    def action_not_done_experiment(self, id) -> models.action.ActionNotDoneExperiment:
        api_response = self.action_api.action_not_done_experiment(id)
        return models.action.ActionNotDoneExperiment.from_dict(api_response)

    def action_group(self, id) -> models.action.ActionGroup:
        api_response = self.action_api.action_group(id)
        return models.action.ActionGroup.from_dict(api_response)

    def action_group_round(self, id) -> models.action.ActionGroupRound:
        api_response = self.action_api.action_group_round(id)
        return models.action.ActionGroupRound.from_dict(api_response)

    def action_protocol(self, id) -> models.action.ActionProtocol:
        api_response = self.action_api.action_protocol(id)
        return models.action.ActionProtocol.from_dict(api_response)

    def action_protocol_round(self, id) -> models.action.ActionProtocolRound:
        api_response = self.action_api.action_protocol_round(id)
        return models.action.ActionProtocolRound.from_dict(api_response)


# Device API
    def device(self, id) -> models.device.DeviceWrapper:
        api_response = self.device_api.device(id)
        return models.device.DeviceWrapper.from_dict(api_response)

    def device_active(self) -> models.device.DeviceActive:
        api_response = self.device_api.device_active()
        return models.device.DeviceActive.from_dict(api_response)

    def device_profile(self, id) -> models.device.DeviceProfile:
        api_response = self.device_api.device_profile(id)
        return models.device.DeviceProfile.from_dict(api_response)

# Profile API
    def profile_id(self) -> models.profile.ProfileID:
        api_response = self.profile_api.profile_id()
        return models.profile.ProfileID.from_dict(api_response)

    def profile(self, id) -> models.profile.Profile:
        api_response = self.profile_api.profile(id)
        return models.profile.ProfileWrapper.from_dict(api_response)

    def profile_active(self) -> models.profile.ProfileActive:
        api_response = self.profile_api.profile_active()
        return models.profile.ProfileActive.from_dict(api_response)

# Tray API
    def tray(self, id) -> models.tray.TrayWrapper:
        api_response = self.tray_api.tray(id)
        return models.TrayWrapper.from_dict(api_response)

    def tray_round(self, id) -> models.tray.TrayRound:
        api_response = self.tray_api.tray_round(id)
        return models.tray.TrayRound.from_dict(api_response)

    def tray_type(self, id) -> models.tray.TrayType:
        api_response = self.tray_api.tray_type(id)
        return models.tray.TrayType.from_dict(api_response)

    def tray_type_tray(self, id) -> models.tray.TrayTypeTray:
        api_response = self.tray_api.tray_type_tray(id)
        return models.tray.TrayTypeTray.from_dict(api_response)

    def tray_type_tray_profile(self, id) -> models.tray.TrayTypeTrayProfile:
        api_response = self.tray_api.tray_type_tray_profile(id)
        return models.tray.TrayTypeTrayProfile.from_dict(api_response)

    def tray_profile(self, id) -> models.tray.TrayProfile:
        api_response = self.tray_api.tray_profile(id)
        return models.tray.TrayProfileWrapper.from_dict(api_response)

    def tray_profile_tray(self, id) -> models.tray.TrayProfileTray:
        api_response = self.tray_api.tray_profile_tray(id)
        return models.tray.TrayProfileTray.from_dict(api_response)

    def tray_profile_used_tray(self, id, start, stop) -> models.tray.TrayProfileUsedTray:
        api_response = self.tray_api.tray_profile_used_tray(id, start, stop)
        return models.tray.TrayProfileUsedTray.from_dict(api_response)

    def tray_profile_to_date_tray(self, id, date) -> models.tray.TrayProfileToDateTray:
        api_response = self.tray_api.tray_profile_to_date_tray(id, date)
        return models.tray.TrayProfileToDateTray.from_dict(api_response)

    def scales_mapping_tray(self, id) -> models.tray.ScalesMappingTray:
        api_response = self.tray_api.scales_mapping_tray(id)
        return models.tray.ScalesMappingTray.from_dict(api_response)

# # Plant API
#     def plant(self, id) -> models.PlantWrapper:
#         api_response = self.plant_api.plant(id)
#         return models.PlantWrapper.from_dict(api_response)

#     def plant_tray(self, id) -> models.PlantTray:
#         api_response = self.plant_api.plant_tray(id)
#         return models.PlantTray.from_dict(api_response)

#     def plant_tray_profile_tray(self, id, start, stop) -> models.PlantTrayProfileTray:
#         api_response = self.plant_api.plant_tray_profile_tray(id, start, stop)
#         return models.PlantTrayProfileTray.from_dict(api_response)

#     def plant_tray_profile(self, id) -> models.PlantTrayProfile:
#         api_response = self.plant_api.plant_tray_profile(id)
#         return models.PlantTrayProfile.from_dict(api_response)

#     def plant_height_round(self, id) -> models.PlantHeightRound:
#         api_response = self.plant_api.plant_height_round(id)
#         return models.PlantHeightRound.from_dict(api_response)

#     def plant_leaf(self, plant_id, tray_id) -> models.PlantLeaf:
#         api_response = self.plant_api.plant_leaf(plant_id, tray_id)
#         return models.PlantLeaf.from_dict(api_response)

# # Fc API
#     def fc_imaging_measure(self, id) -> models.FcImagingMeasure:
#         api_response = self.fc_api.fc_imaging_measure(id)
#         return models.FcImagingMeasure.from_dict(api_response)

#     def fc_imaging(self, device_id, round_id, tray_id) -> models.FcImagingWrapper:
#         api_response = self.fc_api.fc_imaging(device_id, round_id, tray_id)
#         return models.FcImagingWrapper.from_dict(api_response)

#     def fc_imaging_extended_data_measure(self, id) -> models.FcImagingExtendedDataMeasure:
#         api_response = self.fc_api.fc_imaging_extended_data_measure(id)
#         return models.FcImagingExtendedDataMeasure.from_dict(api_response)

#     def fc_imaging_extended_data(self, device_id, round_id, tray_id) -> models.FcImagingExtendedData:
#         api_response = self.fc_api.fc_imaging_extended_data(device_id, round_id, tray_id)
#         return models.FcImagingExtendedData.from_dict(api_response)

#     def fc_plant_mask_measure(self, id) -> models.FcPlantMaskMeasure:
#         api_response = self.fc_api.fc_plant_mask_measure(id)
#         return models.FcPlantMaskMeasure.from_dict(api_response)

#     def fc_plant_mask(self, device_id, round_id, tray_id) -> models.FcPlantMask:
#         api_response = self.fc_api.fc_plant_mask(device_id, round_id, tray_id)
#         return models.FcPlantMask.from_dict(api_response)

#     def fc_param(self, id) -> models.FcParamWrapper:
#         api_response = self.fc_api.fc_param(id)
#         return models.FcParamWrapper.from_dict(api_response)

#     def i_fc_param_used_analyse(self, id) -> models.IFcParamUsedAnalyse:
#         api_response = self.fc_api.i_fc_param_used_analyse(id)
#         return models.IFcParamUsedAnalyse.from_dict(api_response)

#     def fc_param_used(self, device_id, round_id, tray_id) -> models.FcParamUsed:
#         api_response = self.fc_api.fc_param_used(device_id, round_id, tray_id)
#         return models.FcParamUsed.from_dict(api_response)

#     def fc_param_image_analyse(self, id, param_id) -> models.FcParamImageAnalyse:
#         api_response = self.fc_api.fc_param_image_analyse(id, param_id)
#         return models.FcParamImageAnalyse.from_dict(api_response)

#     def fc_param_image(self, device_id, round_id, tray_id, param_id) -> models.FcParamImage:
#         api_response = self.fc_api.fc_param_image(device_id, round_id, tray_id, param_id)
#         return models.FcParamImage.from_dict(api_response)

#     def fc_plant_param_analyse(self, id, param_id) -> models.FcPlantParamAnalyse:
#         api_response = self.fc_api.fc_plant_param_analyse(id, param_id)
#         return models.FcPlantParamAnalyse.from_dict(api_response)

#     def fc_plant_param(self, device_id, round_id, tray_id, param_id) -> models.FcPlantParam:
#         api_response = self.fc_api.fc_plant_param(device_id, round_id, tray_id, param_id)
#         return models.FcPlantParam.from_dict(api_response)

#     def fc_leaf_param_analyse(self, id, param_id) -> models.FcLeafParamAnalyse:
#         api_response = self.fc_api.fc_leaf_param_analyse(id, param_id)
#         return models.FcLeafParamAnalyse.from_dict(api_response)

#     def fc_leaf_param(self, device_id, round_id, tray_id, param_id) -> models.FcLeafParam:
#         api_response = self.fc_api.fc_leaf_param(device_id, round_id, tray_id, param_id)
#         return models.FcLeafParam.from_dict(api_response)

# # Hc API
#     def hc_imaging_measure(self, id) -> models.HcImagingMeasure:
#         api_response = self.hc_api.hc_imaging_measure(id)
#         return models.HcImagingMeasure.from_dict(api_response)

#     def hc_imaging(self, device_id, round_id, tray_id) -> models.HcImagingWrapper:
#         api_response = self.hc_api.hc_imaging(device_id, round_id, tray_id)
#         return models.HcImagingWrapper.from_dict(api_response)

#     def hc_imaging_extended_data_measure(self, id) -> models.HcImagingExtendedDataMeasure:
#         api_response = self.hc_api.hc_imaging_extended_data_measure(id)
#         return models.HcImagingExtendedDataMeasure.from_dict(api_response)

#     def hc_imaging_extended_data(self, device_id, round_id, tray_id) -> models.HcImagingExtendedData:
#         api_response = self.hc_api.hc_imaging_extended_data(device_id, round_id, tray_id)
#         return models.HcImagingExtendedData.from_dict(api_response)

#     def hc_rgb_image_measure(self, id) -> models.HcRgbImageMeasure:
#         api_response = self.hc_api.hc_rgb_image_measure(id)
#         return models.HcRgbImageMeasure.from_dict(api_response)

#     def hc_rgb_image(self, device_id, round_id, tray_id) -> models.HcRgbImage:
#         api_response = self.hc_api.hc_rgb_image(device_id, round_id, tray_id)
#         return models.HcRgbImage.from_dict(api_response)

#     def hc_plant_mask_measure(self, id) -> models.HcPlantMaskMeasure:
#         api_response = self.hc_api.hc_plant_mask_measure(id)
#         return models.HcPlantMaskMeasure.from_dict(api_response)

#     def hc_plant_mask(self, device_id, round_id, tray_id) -> models.HcPlantMask:
#         api_response = self.hc_api.hc_plant_mask(device_id, round_id, tray_id)
#         return models.HcPlantMask.from_dict(api_response)

#     def hc_param(self, id) -> models.HcParamWrapper:
#         api_response = self.hc_api.hc_param(id)
#         return models.HcParamWrapper.from_dict(api_response)

#     def hc_param_used_analyse(self, id) -> models.HcParamUsedAnalyse:
#         api_response = self.hc_api.hc_param_used_analyse(id)
#         return models.HcParamUsedAnalyse.from_dict(api_response)

#     def hc_param_used(self, device_id, round_id, tray_id) -> models.HcParamUsed:
#         api_response = self.hc_api.hc_param_used(device_id, round_id, tray_id)
#         return models.HcParamUsed.from_dict(api_response)

#     def hc_param_image_analyse(self, id, param_id) -> models.HcParamImageAnalyse:
#         api_response = self.hc_api.hc_param_image_analyse(id, param_id)
#         return models.HcParamImageAnalyse.from_dict(api_response)

#     def hc_param_image(self, device_id, round_id, tray_id, param_id) -> models.HcParamImage:
#         api_response = self.hc_api.hc_param_image(device_id, round_id, tray_id, param_id)
#         return models.HcParamImage.from_dict(api_response)

#     def hc_plant_param_analyse(self, id, param_id) -> models.HcPlantParamAnalyse:
#         api_response = self.hc_api.hc_plant_param_analyse(id, param_id)
#         return models.HcPlantParamAnalyse.from_dict(api_response)

#     def hc_plant_param(self, device_id, round_id, tray_id, param_id) -> models.HcPlantParam:
#         api_response = self.hc_api.hc_plant_param(device_id, round_id, tray_id, param_id)
#         return models.HcPlantParam.from_dict(api_response)

#     def hc_leaf_param_analyse(self, id, param_id) -> models.HcLeafParamAnalyse:
#         api_response = self.hc_api.hc_leaf_param_analyse(id, param_id)
#         return models.HcLeafParamAnalyse.from_dict(api_response)

#     def hc_leaf_param(self, device_id, round_id, tray_id, param_id) -> models.HcLeafParam:
#         api_response = self.hc_api.hc_leaf_param(device_id, round_id, tray_id, param_id)
#         return models.HcLeafParam.from_dict(api_response)

# # Ir API
#     def ir_imaging_measure(self, id) -> models.IrImagingMeasure:
#         api_response = self.ir_api.ir_imaging_measure(id)
#         return models.IrImagingMeasure.from_dict(api_response)

#     def ir_imaging(self, device_id, round_id, tray_id) -> models.IrImaging:
#         api_response = self.ir_api.ir_imaging(device_id, round_id, tray_id)
#         return models.IrImaging.from_dict(api_response)

#     def ir_imaging_extended_data_measure(self, id) -> models.IrImagingExtendedDataMeasure:
#         api_response = self.ir_api.ir_imaging_extended_data_measure(id)
#         return models.IrImagingExtendedDataMeasure.from_dict(api_response)

#     def ir_imaging_extended_data(self, device_id, round_id, tray_id) -> models.IrImagingExtendedData:
#         api_response = self.ir_api.ir_imaging_extended_data(device_id, round_id, tray_id)
#         return models.IrImagingExtendedData.from_dict(api_response)

#     def ir_plant_mask_measure(self, id) -> models.IrPlantMaskMeasure:
#         api_response = self.ir_api.ir_plant_mask_measure(id)
#         return models.IrPlantMaskMeasure.from_dict(api_response)

#     def ir_plant_mask(self, device_id, round_id, tray_id) -> models.IrPlantMask:
#         api_response = self.ir_api.ir_plant_mask(device_id, round_id, tray_id)
#         return models.IrPlantMask.from_dict(api_response)

#     def ir_plant_mask_image_measure(self, id) -> models.IrPlantMaskImageMeasure:
#         api_response = self.ir_api.ir_plant_mask_image_measure(id)
#         return models.IrPlantMaskImageMeasure.from_dict(api_response)

#     def ir_plant_mask_image(self, device_id, round_id, tray_id) -> models.IrPlantMaskImage:
#         api_response = self.ir_api.ir_plant_mask_image(device_id, round_id, tray_id)
#         return models.IrPlantMaskImage.from_dict(api_response)

#     def ir_param(self, id) -> models.IrParamWrappper:
#         api_response = self.ir_api.ir_param(id)
#         return models.IrParamWrappper.from_dict(api_response)

#     def ir_param_used_analyse(self, id) -> models.IrParamUsedAnalyse:
#         api_response = self.ir_api.ir_param_used_analyse(id)
#         return models.IrParamUsedAnalyse.from_dict(api_response)

#     def ir_param_used(self, device_id, round_id, tray_id) -> models.IrParamUsed:
#         api_response = self.ir_api.ir_param_used(device_id, round_id, tray_id)
#         return models.IrParamUsed.from_dict(api_response)

#     def ir_plant_param_analyse(self, id, param_id) -> models.IrPlantParamAnalyse:
#         api_response = self.ir_api.ir_plant_param_analyse(id, param_id)
#         return models.IrPlantParamAnalyse.from_dict(api_response)

#     def ir_plant_param(self, device_id, round_id, tray_id, param_id) -> models.IrPlantParam:
#         api_response = self.ir_api.ir_plant_param(device_id, round_id, tray_id, param_id)
#         return models.IrPlantParam.from_dict(api_response)

#     def ir_leaf_param_analyse(self, id, param_id) -> models.IrLeafParamAnalyse:
#         api_response = self.ir_api.ir_leaf_param_analyse(id, param_id)
#         return models.IrLeafParamAnalyse.from_dict(api_response)

#     def ir_leaf_param(self, device_id, round_id, tray_id, param_id) -> models.IrLeafParam:
#         api_response = self.ir_api.ir_leaf_param(device_id, round_id, tray_id, param_id)
#         return models.IrLeafParam.from_dict(api_response)

# # Probe API
#     def probe(self) -> models.ProbeWrapper:
#         api_response = self.probe_api.probe()
#         return models.ProbeWrapper.from_dict(api_response)

#     def probe_value_date(self, start, stop) -> models.ProbeValuesDate:
#         api_response = self.probe_api.probe_value_date(start, stop)
#         return models.ProbeValuesDate.from_dict(api_response)

#     def probe_value_date_probe(self, id, start, stop) -> models.ProbeValueDateProbe:
#         api_response = self.probe_api.probe_value_date_probe(id, start, stop)
#         return models.ProbeValueDateProbe.from_dict(api_response)

# ############################################# TODO Test #################################################################
# # Msc API
#     def msc_imaging_measure(self, id) -> models.MscImagingMeasure:
#         api_response = self.msc_api.msc_imaging_measure(id)
#         return models.MscImagingMeasure.from_dict(api_response)

#     def msc_imaging(self, device_id, round_id, tray_id) -> models.MscImaging:
#         api_response = self.msc_api.msc_imaging(device_id, round_id, tray_id)
#         return models.MscImaging.from_dict(api_response)

#     def msc_imaging_extended_data_measure(self, id) -> models.MscImagingExtendedDataMeasure:
#         api_response = self.msc_api.msc_imaging_extended_data_measure(id)
#         return models.MscImagingExtendedDataMeasure.from_dict(api_response)

#     def msc_imaging_extended_data(self, device_id, round_id, tray_id) -> models.MscImagingExtendedData:
#         api_response = self.msc_api.msc_imaging_extended_data(device_id, round_id, tray_id)
#         return models.MscImagingExtendedData.from_dict(api_response)

#     def msc_plant_mask_measure(self, id) -> models.MscPlantMaskMeasure:
#         api_response = self.msc_api.msc_plant_mask_measure(id)
#         return models.MscPlantMaskMeasure.from_dict(api_response)

#     def msc_plant_mask_meamsc_plant_masksure(self, device_id, round_id, tray_id) -> models.MscPlantMask:
#         api_response = self.msc_api.msc_plant_mask(device_id, round_id, tray_id)
#         return models.MscPlantMask.from_dict(api_response)

#     def msc_param(self, id) -> models.MscParamWrapper:
#         api_response = self.msc_api.msc_param(id)
#         return models.MscParamWrapper.from_dict(api_response)

#     def msc_param_used_analyse(self, id) -> models.MscParamUsedAnalyse:
#         api_response = self.msc_api.msc_param_used_analyse(id)
#         return models.MscParamUsedAnalyse.from_dict(api_response)

#     def msc_param_used(self, device_id, round_id, tray_id) -> models.MscParamUsed:
#         api_response = self.msc_api.msc_param_used(device_id, round_id, tray_id)
#         return models.MscParamUsed.from_dict(api_response)

#     def msc_param_image_analyse(self, id, param_id) -> models.MscParamImageAnalyse:
#         api_response = self.msc_api.msc_param_image_analyse(id, param_id)
#         return models.MscParamImageAnalyse.from_dict(api_response)

#     def msc_param_image(self, device_id, round_id, tray_id, param_id) -> models.MscParamImageWrapper:
#         api_response = self.msc_api.msc_param_image(device_id, round_id, tray_id, param_id)
#         return models.MscParamImageWrapper.from_dict(api_response)

#     def msc_plant_param_analyse(self, id, param_id) -> models.MscPlantParamAnalyse:
#         api_response = self.msc_api.msc_plant_param_analyse(id, param_id)
#         return models.MscPlantParamAnalyse.from_dict(api_response)

#     def msc_plant_param(self, device_id, round_id, tray_id, param_id) -> models.MscPlantParam:
#         api_response = self.msc_api.msc_plant_param(device_id, round_id, tray_id, param_id)
#         return models.MscPlantParam.from_dict(api_response)

#     def msc_leaf_param_analyse(self, id, param_id) -> models.MscLeafParamAnalyse:
#         api_response = self.msc_api.msc_leaf_param_analyse(id, param_id)
#         return models.MscLeafParamAnalyse.from_dict(api_response)

    def msc_leaf_param(self, device_id, round_id, tray_id, param_id) -> models.msc.MscLeafParam:
        api_response = self.msc_api.msc_leaf_param(device_id, round_id, tray_id, param_id)
        return models.msc.MscLeafParam.from_dict(api_response)

#     def msc_light_set(self, id) -> models.MscLightSet:
#         api_response = self.msc_api.msc_light_set(id)
#         return models.MscLightSet.from_dict(api_response)

#     def msc_light_set_used(self, device_id, round_id, tray_id) -> models.MscLightSetUsed:
#         api_response = self.msc_api.msc_light_set_used(device_id, round_id, tray_id)
#         return models.MscLightSetUsed.from_dict(api_response)

#     def msc_calibration(self, id) -> models.MscCalibration:
#         api_response = self.msc_api.msc_calibration(id)
#         return models.MscCalibration.from_dict(api_response)

#     def msc_calibration_light_set(self, id) -> models.MscCalibrationLightSet:
#         api_response = self.msc_api.msc_calibration_light_set(id)
#         return models.MscCalibrationLightSet.from_dict(api_response)

#     def msc_calibration_light(self) -> models.MscCalibrationLight:
#         api_response = self.msc_api.msc_calibration_light()
#         return models.MscCalibrationLight.from_dict(api_response)

# # RGB API
#     def rgb_imaging_measure(self, id) -> models.RgbImagingMeasure:
#         api_response = self.rgb_api.rgb_imaging_measure(id)
#         return models.RgbImagingMeasure.from_dict(api_response)

#     def rgb_imaging(self, device_id, round_id, tray_id) -> models.RgbImaging:
#         api_response = self.rgb_api.rgb_imaging(device_id, round_id, tray_id)
#         return models.RgbImaging.from_dict(api_response)

#     def rgb_imaging_extended_data_measure(self, id) -> models.RgbImagingExtendedDataMeasure:
#         api_response = self.rgb_api.rgb_imaging_extended_data_measure(id)
#         return models.RgbImagingExtendedDataMeasure.from_dict(api_response)

#     def rgb_imaging_extended_data(self, device_id, round_id, tray_id) -> models.RgbImagingExtendedData:
#         api_response = self.rgb_api.rgb_imaging_extended_data(device_id, round_id, tray_id)
#         return models.RgbImagingExtendedData.from_dict(api_response)

#     def rgb_plant_mask_measure(self, id) -> models.RgbPlantMaskMeasure:
#         api_response = self.rgb_api.rgb_plant_mask_measure(id)
#         return models.RgbPlantMaskMeasure.from_dict(api_response)

#     def rgb_plant_mask(self, device_id, round_id, tray_id) -> models.RgbPlantMask:
#         api_response = self.rgb_api.rgb_plant_mask(device_id, round_id, tray_id)
#         return models.RgbPlantMask.from_dict(api_response)

#     def rgb_greening_mask_image_measure(self, id) -> models.RgbGreeningMaskImageMeasure:
#         api_response = self.rgb_api.rgb_greening_mask_image_measure(id)
#         return models.RgbGreeningMaskImageMeasure.from_dict(api_response)

#     def rgb_greening_mask_image(self, device_id, round_id, tray_id) -> models.RgbGreeningMaskImage:
#         api_response = self.rgb_api.rgb_greening_mask_image(device_id, round_id, tray_id)
#         return models.RgbGreeningMaskImage.from_dict(api_response)

#     def rgb_param(self, id) -> models.RgbParamWrapper:
#         api_response = self.rgb_api.rgb_param(id)
#         return models.RgbParamWrapper.from_dict(api_response)

#     def rgb_param_used_analyse(self, id) -> models.RgbParamUsedAnalyse:
#         api_response = self.rgb_api.rgb_param_used_analyse(id)
#         return models.RgbParamUsedAnalyse.from_dict(api_response)

#     def rgb_param_used(self, device_id, round_id, tray_id) -> models.RgbParamUsed:
#         api_response = self.rgb_api.rgb_param_used(device_id, round_id, tray_id)
#         return models.RgbParamUsed.from_dict(api_response)

#     def rgb_param_color_used_analyse(self, id) -> models.RgbParamColorUsedAnalyse:
#         api_response = self.rgb_api.rgb_param_color_used_analyse(id)
#         return models.RgbParamColorUsedAnalyse.from_dict(api_response)

#     def rgb_param_color_used(self, device_id, round_id, tray_id) -> models.RgbParamColorUsed:
#         api_response = self.rgb_api.rgb_param_color_used(device_id, round_id, tray_id)
#         return models.RgbParamColorUsed.from_dict(api_response)

#     def rgb_plant_param_analyse(self, id, param_id) -> models.RgbPlantParamAnalyse:
#         api_response = self.rgb_api.rgb_plant_param_analyse(id, param_id)
#         return models.RgbPlantParamAnalyse.from_dict(api_response)

#     def rgb_plant_param(self, device_id, round_id, tray_id, param_id) -> models.RgbPlantParam:
#         api_response = self.rgb_api.rgb_plant_param(device_id, round_id, tray_id, param_id)
#         return models.RgbPlantParam.from_dict(api_response)

#     def rgb_plant_param_color_analyse(self, id, param_id) -> models.RgbPlantParamColorAnalyse:
#         api_response = self.rgb_api.rgb_plant_param_color_analyse(id, param_id)
#         return models.RgbPlantParamColorAnalyse.from_dict(api_response)

#     def rgb_plant_param_color(self, device_id, round_id, tray_id, param_id) -> models.RgbPlantParamColor:
#         api_response = self.rgb_api.rgb_plant_param_color(device_id, round_id, tray_id, param_id)
#         return models.RgbPlantParamColor.from_dict(api_response)

#     def rgb_leaf_param_analyse(self, id, param_id) -> models.RgbLeafParamAnalyse:
#         api_response = self.rgb_api.rgb_leaf_param_analyse(id, param_id)
#         return models.RgbLeafParamAnalyse.from_dict(api_response)

#     def rgb_leaf_param(self, device_id, round_id, tray_id, param_id) -> models.RgbLeafParam:
#         api_response = self.rgb_api.rgb_leaf_param(device_id, round_id, tray_id, param_id)
#         return models.RgbLeafParam.from_dict(api_response)

#     def rgb_leaf_param_color_analyse(self, id, param_id) -> models.RgbLeafParamColorAnalyse:
#         api_response = self.rgb_api.rgb_leaf_param_color_analyse(id, param_id)
#         return models.RgbLeafParamColorAnalyse.from_dict(api_response)

#     def rgb_leaf_param_color(self, device_id, round_id, tray_id, param_id) -> models.RgbLeafParamColor:
#         api_response = self.rgb_api.rgb_leaf_param_color(device_id, round_id, tray_id, param_id)
#         return models.RgbLeafParamColor.from_dict(api_response)

# # Scan3d API
#     def scan3d_imaging_measure(self, id) -> models.Scan3dImagingMeasure:
#         api_response = self.scan3d_api.scan3d_imaging_measure(id)
#         return models.Scan3dImagingMeasure.from_dict(api_response)

#     def scan3d(self, device_id, round_id, tray_id) -> models.Scan3d:
#         api_response = self.scan3d_api.scan3d(device_id, round_id, tray_id)
#         return models.Scan3d.from_dict(api_response)

#     def scan3d_imaging_extended_data_measure(self, id) -> models.Scan3dImagingExtendedDataMeasure:
#         api_response = self.scan3d_api.scan3d_imaging_extended_data_measure(id)
#         return models.Scan3dImagingExtendedDataMeasure.from_dict(api_response)

#     def i_scan3d_imaging_extended_data(self, device_id, round_id, tray_id) -> models.Scan3dImagingExtendedData:
#         api_response = self.scan3d_api.i_scan3d_imaging_extended_data(device_id, round_id, tray_id)
#         return models.Scan3dImagingExtendedData.from_dict(api_response)

#     def scan3d_analyzed_model_measure(self, id) -> models.Scan3dAnalyzedModelMeasure:
#         api_response = self.scan3d_api.scan3d_analyzed_model_measure(id)
#         return models.Scan3dAnalyzedModelMeasure.from_dict(api_response)

#     def scan3d_analysed_model_analyse(self, id) -> models.Scan3dAnalysedModelAnalyse:
#         api_response = self.scan3d_api.scan3d_analysed_model_analyse(id)
#         return models.Scan3dAnalysedModelAnalyse.from_dict(api_response)

#     def scan3d_analyzed_model(self, device_id, round_id, tray_id) -> models.Scan3dAnalyzedModel:
#         api_response = self.scan3d_api.scan3d_analyzed_model(device_id, round_id, tray_id)
#         return models.Scan3dAnalyzedModel.from_dict(api_response)

#     def scan3d_param(self, id) -> models.Scan3dParamWrapper:
#         api_response = self.scan3d_api.scan3d_param(id)
#         return models.Scan3dParamWrapper.from_dict(api_response)

#     def scan3d_param_used_analyse(self, id) -> models.Scan3dParamUsedAnalyse:
#         api_response = self.scan3d_api.scan3d_param_used_analyse(id)
#         return models.Scan3dParamUsedAnalyse.from_dict(api_response)

#     def scan3d_param_used(self, device_id, round_id, tray_id) -> models.Scan3dParamUsed:
#         api_response = self.scan3d_api.scan3d_param_used(device_id, round_id, tray_id)
#         return models.Scan3dParamUsed.from_dict(api_response)

#     def scan3d_plant_param_analyse(self, id, param_id) -> models.Scan3dPlantParamAnalyse:
#         api_response = self.scan3d_api.scan3d_plant_param_analyse(id, param_id)
#         return models.Scan3dPlantParamAnalyse.from_dict(api_response)

#     def scan3d_plant_param(self, device_id, round_id, tray_id, param_id) -> models.Scan3dPlantParam:
#         api_response = self.scan3d_api.scan3d_plant_param(device_id, round_id, tray_id, param_id)
#         return models.Scan3dPlantParam.from_dict(api_response)

#     def scan3d_leaf_param_analyse(self, id, param_id) -> models.Scan3dLeafParamAnalyse:
#         api_response = self.scan3d_api.scan3d_leaf_param_analyse(id, param_id)
#         return models.Scan3dLeafParamAnalyse.from_dict(api_response)

#     def scan3d_leaf_param(self, device_id, round_id, tray_id, param_id) -> models.Scan3dLeafParam:
#         api_response = self.scan3d_api.scan3d_leaf_param(device_id, round_id, tray_id, param_id)
#         return models.Scan3dLeafParam.from_dict(api_response)

# # Scales API
#     def scales_plant_weight_measure(self, id) -> models.ScalesPlantWeightMeasure:
#         api_response = self.scales_api.scales_plant_weight_measure(id)
#         return models.ScalesPlantWeightMeasure.from_dict(api_response)

#     def get_scales_plant_weight(self, device_id, round_id, tray_id) -> models.ScalesPlantWeight:
#         api_response = self.scales_api.scales_plant_weight(device_id, round_id, tray_id)
#         return models.ScalesPlantWeight.from_dict(api_response)

#     def get_scales_weight_reference_plant(self, id) -> models.ScalesWeightReferencePlant:
#         api_response = self.scales_api.scales_weight_reference_plant(id)
#         return models.ScalesWeightReferencePlant.from_dict(api_response)

#     def get_scales_weight_reference_tray(self, id) -> models.ScalesWeightReferenceTray:
#         api_response = self.scales_api.scales_weight_reference_tray(id)
#         return models.ScalesWeightReferenceTray.from_dict(api_response)

#     def get_scales_weight_reference_to_date_tray(self, id, _date) -> models.ScalesWeightReferenceToDateTray:
#         api_response = self.scales_api.scales_weight_reference_to_date_tray(id, _date)
#         return models.ScalesWeightReferenceToDateTray.from_dict(api_response)

# # Spray API
#     def get_spray_action(self, device_id, round_id, tray_id) -> models.SprayAction:
#         api_response = self.spray_api.spray_action(device_id, round_id, tray_id)
#         return models.SprayAction.from_dict(api_response)

# # Spectrum Device API
#     def get_spectrum_device_id(self) -> models.SpectrumDeviceID:
#         api_response = self.spectrum_device_api.spectrum_device_id()
#         return models.SpectrumDeviceID.from_dict(api_response)

#     def get_spectrum_device(self, id) -> models.SpectrumDeviceWrapper:
#         api_response = self.spectrum_device_api.spectrum_device(id)
#         return models.SpectrumDevice.from_dict(api_response)

#     def get_spectrum_values_date_device(self, id, start, stop) -> models.SpectrumValuesDateDevice:
#         api_response = self.spectrum_device_api.spectrum_values_date_device(id, start, stop)
#         return models.SpectrumValuesDateDevice.from_dict(api_response)

# # Buffer API
#     def get_buffer_history(self, id) -> models.BufferHistoryWrapper:
#         api_response = self.buffer_api.buffer_history(id)
#         return models.BufferHistoryWrapper.from_dict(api_response)

#     def get_buffer_history_date(self, start, stop) -> models.BufferHistoryDate:
#         api_response = self.buffer_api.buffer_history_date(start, stop)
#         return models.BufferHistoryDate.from_dict(api_response)

# # System Log API
#     def get_system_log_round(self, id) -> models.SystemLogRound:
#         api_response = self.system_log_api.system_log_round(id)
#         return models.SystemLogRound.from_dict(api_response)

#     def get_system_log_date_round(self, id, start, stop) -> models.SystemLogDateRound:
#         api_response = self.system_log_api.system_log_date_round(id, start, stop)
#         return models.SystemLogDateRound.from_dict(api_response)

#     def get_system_log_tray(self, id) -> models.SystemLogTray:
#         api_response = self.system_log_api.system_log_tray(id)
#         return models.SystemLogTray.from_dict(api_response)

#     def get_system_log_date_tray(self, id, start, stop) -> models.SystemLogDateTray:
#         api_response = self.system_log_api.system_log_date_tray(id, start, stop)
#         return models.SystemLogDateTray.from_dict(api_response)

#     def get_system_log_log_type(self) -> models.SystemLogLogType:
#         api_response = self.system_log_api.system_log_log_type()
#         return models.SystemLogLogType.from_dict(api_response)

#     def get_system_log_date_log_type(self, type, start, stop) -> models.SystemLogDateLogType:
#         api_response = self.system_log_api.system_log_date_log_type(type, start, stop)
#         return models.SystemLogDateLogType.from_dict(api_response)

#     def get_system_log_log_tag(self) -> models.SystemLogLogTag:
#         api_response = self.system_log_api.system_log_log_tag()
#         return models.SystemLogLogTag.from_dict(api_response)

#     def get_system_log_date_log_tag(self, tag, start, stop) -> models.SystemLogDateLogTag:
#         api_response = self.system_log_api.system_log_date_log_tag(tag, start, stop)
#         return models.SystemLogDateLogTag.from_dict(api_response)

# # Version Info API
#     def version_info(self) -> models.VersionInfo:
#         api_response = self.version_info_api.version_info()
#         return models.VersionInfo.from_dict(api_response)





