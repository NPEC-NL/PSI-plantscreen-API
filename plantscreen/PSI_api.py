import plantscreen.swagger_client as swagger_client
import plantscreen.models.experiment_models as experiment_models
import plantscreen.models.round_models as round_models
import plantscreen.models.action_models as action_models
import plantscreen.models.device_models as device_models
import plantscreen.models.profile_models as profile_models
import plantscreen.models.tray_models as tray_models
import plantscreen.models.plant_models as plant_models
import plantscreen.models.fc_models as fc_models
import plantscreen.models.hc_models as hc_models
import plantscreen.models.ir_models as ir_models
import plantscreen.models.probe_models as probe_models
import plantscreen.models.msc_models as msc_models 
import plantscreen.models.rgb_models as rgb_models 
import plantscreen.models.scan3d_models as scan3d_models 
import plantscreen.models.scales_models as scales_models 
import plantscreen.models.spray_models as spray_models 
import plantscreen.models.spectrum_device_models as spectrum_device_models 
import plantscreen.models.buffer_models as buffer_models 
import plantscreen.models.system_log_models as system_log_models 
import plantscreen.models.file_models as file_models 
import plantscreen.models.version_info_modes as version_info_modes 


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



    def experimentID(self) -> experiment_models.ExperimentIDs:
        api_response = self.api_instance.experiment_id()
        return experiment_models.ExperimentIDs.from_dict(api_response)
    
    def experiment(self, id) -> experiment_models.Experiment:
        api_response = self.exp_api.experiment(id)
        return experiment_models.ExperimentWrapper.from_dict(api_response)
    
    def experiment_date(self, start, stop) -> experiment_models.ExperimentDate:
        api_response = self.exp_api.experiment_date(start, stop)
        return experiment_models.ExperimentDate.from_dict(api_response)

    def experiment_owner(self, id) -> experiment_models.ExperimentOwner:
        api_response = self.exp_api.experiment_owner(id)
        return experiment_models.ExperimentOwner.from_dict(api_response)    
    
    def owner_id(self) -> experiment_models.OwnerID:
        api_response = self.exp_api.owner_id()
        return experiment_models.OwnerID.from_dict(api_response) 

    def owner(self, id) -> experiment_models.OwnerWrapper:
        api_response = self.exp_api.owner(id)
        return experiment_models.OwnerWrapper.from_dict(api_response) 
    
    def note_experiment(self, id) -> experiment_models.NoteExperiment:
        api_response = self.exp_api.note_experiment(id)
        return experiment_models.NoteExperiment.from_dict(api_response)     
    

# Round API
    def round(self, id) -> round_models.Round:
        api_response = self.round_api.round(id)
        return round_models.RoundWrapper.from_dict(api_response)
    
    def round_experiment(self, id) -> round_models.RoundExperiment:
        api_response = self.round_api.round_experiment(id)
        return round_models.RoundExperiment.from_dict(api_response)   

    def round_date_experiment(self, id, start, stop) -> round_models.RoundDateExperiment:
        api_response = self.round_api.round_date_experiment(id, start, stop)
        return round_models.RoundDateExperiment.from_dict(api_response)    

    def round_order_round(self, id) -> round_models.Order:
        api_response = self.round_api.round_order_round(id)
        return round_models.RoundOrderRound.from_dict(api_response)   

    def round_order_experiment(self, id) -> round_models.RoundOrderExperiment:
        api_response = self.round_api.round_order_experiment(id)
        return round_models.RoundOrderExperiment.from_dict(api_response)   
    
    def round_order_date_experiment(self, id, start, stop) -> round_models.RoundOrderDateExperiment:
        api_response = self.round_api.round_order_date_experiment(id, start, stop)
        return round_models.RoundOrderDateExperiment.from_dict(api_response)   


# Action API
    def action(self, id) -> action_models.Action:
        api_response = self.action_api.action(id)
        return action_models.ActionWrapper.from_dict(api_response)
    
    def action_experiment(self, id) -> action_models.ActionExperiment:
        api_response = self.action_api.action_experiment(id)
        return action_models.ActionExperiment.from_dict(api_response)
    
    def action_not_done_experiment(self, id) -> action_models.ActionNotDoneExperiment:
        api_response = self.action_api.action_not_done_experiment(id)
        return action_models.ActionNotDoneExperiment.from_dict(api_response)
    
    def action_group(self, id) -> action_models.ActionGroup:
        api_response = self.action_api.action_group(id)
        return action_models.ActionGroup.from_dict(api_response)
    
    def action_group_round(self, id) -> action_models.ActionGroupRound:
        api_response = self.action_api.action_group_round(id)
        return action_models.ActionGroupRound.from_dict(api_response)
    
    def action_protocol(self, id) -> action_models.ActionProtocol:
        api_response = self.action_api.action_protocol(id)
        return action_models.ActionProtocol.from_dict(api_response)
    
    def action_protocol_round(self, id) -> action_models.ActionProtocolRound:
        api_response = self.action_api.action_protocol_round(id)
        return action_models.ActionProtocolRound.from_dict(api_response)
    

# Device API
    def device(self, id) -> device_models.DeviceWrapper:
        api_response = self.device_api.device(id)
        return device_models.DeviceWrapper.from_dict(api_response)
    
    def device_active(self) -> device_models.DeviceActive:
        api_response = self.device_api.device_active()
        return device_models.DeviceActive.from_dict(api_response)
    
    def device_profile(self, id) -> device_models.DeviceProfile:
        api_response = self.device_api.device_profile(id)
        return device_models.DeviceProfile.from_dict(api_response)
    
# Profile API
    def profile_id(self) -> profile_models.ProfileID:
        api_response = self.profile_api.profile_id()
        return profile_models.ProfileID.from_dict(api_response)
    
    def profile(self, id) -> profile_models.ProfileWrapper:
        api_response = self.profile_api.profile(id)
        return profile_models.ProfileWrapper.from_dict(api_response)

    def profile_active(self) -> profile_models.ProfileActive:
        api_response = self.profile_api.profile_active()
        return profile_models.ProfileActive.from_dict(api_response) 

# Tray API
    def tray(self, id) -> tray_models.TrayWrapper:
        api_response = self.tray_api.tray(id)
        return tray_models.TrayWrapper.from_dict(api_response)
    
    def tray_round(self, id) -> tray_models.TrayRound:
        api_response = self.tray_api.tray_round(id)
        return tray_models.TrayRound.from_dict(api_response)
    
    def tray_type(self, id) -> tray_models.TrayType:
        api_response = self.tray_api.tray_type(id)
        return tray_models.TrayType.from_dict(api_response)
    
    def tray_type_tray(self, id) -> tray_models.TrayTypeTray:
        api_response = self.tray_api.tray_type_tray(id)
        return tray_models.TrayTypeTray.from_dict(api_response)

    def tray_type_tray_profile(self, id) -> tray_models.TrayTypeTrayProfile:
        api_response = self.tray_api.tray_type_tray_profile(id)
        return tray_models.TrayTypeTrayProfile.from_dict(api_response)
    
    def tray_profile(self, id) -> tray_models.TrayProfileWrapper:
        api_response = self.tray_api.tray_profile(id)
        return tray_models.TrayProfileWrapper.from_dict(api_response)

    def tray_profile_tray(self, id) -> tray_models.TrayProfileTray:
        api_response = self.tray_api.tray_profile_tray(id)
        return tray_models.TrayProfileTray.from_dict(api_response)

    def tray_profile_used_tray(self, id, start, stop) -> tray_models.TrayProfileUsedTray:
        api_response = self.tray_api.tray_profile_used_tray(id, start, stop)
        return tray_models.TrayProfileUsedTray.from_dict(api_response)
    
    def tray_profile_to_date_tray(self, id, date) -> tray_models.TrayProfileToDateTray:
        api_response = self.tray_api.tray_profile_to_date_tray(id, date)
        return tray_models.TrayProfileToDateTray.from_dict(api_response)
    
    def scales_mapping_tray(self, id) -> tray_models.ScalesMappingTray:
        api_response = self.tray_api.scales_mapping_tray(id)
        return tray_models.ScalesMappingTray.from_dict(api_response)
    
# Plant API
    def plant(self, id) -> plant_models.PlantWrapper:
        api_response = self.plant_api.plant(id)
        return plant_models.PlantWrapper.from_dict(api_response)

    def plant_tray(self, id) -> plant_models.PlantTray:
        api_response = self.plant_api.plant_tray(id)
        return plant_models.PlantTray.from_dict(api_response)

    def plant_tray_profile_tray(self, id, start, stop) -> plant_models.PlantTrayProfileTray:
        api_response = self.plant_api.plant_tray_profile_tray(id, start, stop)
        return plant_models.PlantTrayProfileTray.from_dict(api_response)
    
    def plant_tray_profile(self, id) -> plant_models.PlantTrayProfile:
        api_response = self.plant_api.plant_tray_profile(id)
        return plant_models.PlantTrayProfile.from_dict(api_response)

    def plant_height_round(self, id) -> plant_models.PlantHeightRound:
        api_response = self.plant_api.plant_height_round(id)
        return plant_models.PlantHeightRound.from_dict(api_response)

    def plant_leaf(self, plant_id, tray_id) -> plant_models.PlantLeaf:
        api_response = self.plant_api.plant_leaf(plant_id, tray_id)
        return plant_models.PlantLeaf.from_dict(api_response)
    
# Fc API
    def fc_imaging_measure(self, id) -> fc_models.FcImagingMeasure:
        api_response = self.fc_api.fc_imaging_measure(id)
        return fc_models.FcImagingMeasure.from_dict(api_response)
    
    def fc_imaging(self, device_id, round_id, tray_id) -> fc_models.FcImagingWrapper:
        api_response = self.fc_api.fc_imaging(device_id,round_id,tray_id)
        return fc_models.FcImagingWrapper.from_dict(api_response)
    
    def fc_imaging_extended_data_measure(self, id) -> fc_models.FcImagingExtendedDataMeasure:
        api_response = self.fc_api.fc_imaging_extended_data_measure(id)
        return fc_models.FcImagingExtendedDataMeasure.from_dict(api_response)
    
    def fc_imaging_extended_data(self, device_id, round_id, tray_id) -> fc_models.FcImagingExtendedData:
        api_response = self.fc_api.fc_imaging_extended_data(device_id, round_id, tray_id)
        return fc_models.FcImagingExtendedData.from_dict(api_response)

    def fc_plant_mask_measure(self, id) -> fc_models.FcPlantMaskMeasure:
        api_response = self.fc_api.fc_plant_mask_measure(id)
        return fc_models.FcPlantMaskMeasure.from_dict(api_response)

    def fc_plant_mask(self, device_id, round_id, tray_id) -> fc_models.FcPlantMask:
        api_response = self.fc_api.fc_plant_mask(device_id, round_id, tray_id)
        return fc_models.FcPlantMask.from_dict(api_response)
    
    def fc_param(self, id) -> fc_models.FcParamWrapper:
        api_response = self.fc_api.fc_param(id)
        return fc_models.FcParamWrapper.from_dict(api_response)

    def i_fc_param_used_analyse(self, id) -> fc_models.IFcParamUsedAnalyse:
        api_response = self.fc_api.i_fc_param_used_analyse(id)
        return fc_models.IFcParamUsedAnalyse.from_dict(api_response)

    def fc_param_used(self, device_id, round_id, tray_id) -> fc_models.FcParamUsed:
        api_response = self.fc_api.fc_param_used(device_id, round_id, tray_id)
        return fc_models.FcParamUsed.from_dict(api_response)

    def fc_param_image_analyse(self, id, param_id) -> fc_models.FcParamImageAnalyse:
        api_response = self.fc_api.fc_param_image_analyse(id, param_id)
        return fc_models.FcParamImageAnalyse.from_dict(api_response)

    def fc_param_image(self, device_id, round_id, tray_id, param_id) -> fc_models.FcParamImage:
        api_response = self.fc_api.fc_param_image(device_id, round_id, tray_id, param_id)
        return fc_models.FcParamImage.from_dict(api_response)

    def fc_plant_param_analyse(self, id, param_id) -> fc_models.FcPlantParamAnalyse:
        api_response = self.fc_api.fc_plant_param_analyse(id, param_id)
        return fc_models.FcPlantParamAnalyse.from_dict(api_response)

    def fc_plant_param(self, device_id, round_id, tray_id, param_id) -> fc_models.FcPlantParam:
        api_response = self.fc_api.fc_plant_param(device_id, round_id, tray_id, param_id)
        return fc_models.FcPlantParam.from_dict(api_response)

    def fc_leaf_param_analyse(self, id, param_id) -> fc_models.FcLeafParamAnalyse:
        api_response = self.fc_api.fc_leaf_param_analyse(id, param_id)
        return fc_models.FcLeafParamAnalyse.from_dict(api_response)

    def fc_leaf_param(self, device_id, round_id, tray_id, param_id) -> fc_models.FcLeafParam:
        api_response = self.fc_api.fc_leaf_param(device_id, round_id, tray_id, param_id)
        return fc_models.FcLeafParam.from_dict(api_response)

# Hc API
    def hc_imaging_measure(self, id) -> hc_models.HcImagingMeasure:
        api_response = self.hc_api.hc_imaging_measure(id)
        return hc_models.HcImagingMeasure.from_dict(api_response)
    
    def hc_imaging(self, device_id, round_id, tray_id) -> hc_models.HcImagingWrapper:
        api_response = self.hc_api.hc_imaging(device_id, round_id, tray_id)
        return hc_models.HcImagingWrapper.from_dict(api_response)

    def hc_imaging_extended_data_measure(self, id) -> hc_models.HcImagingExtendedDataMeasure:
        api_response = self.hc_api.hc_imaging_extended_data_measure(id)
        return hc_models.HcImagingExtendedDataMeasure.from_dict(api_response)
    
    def hc_imaging_extended_data(self, device_id, round_id, tray_id) -> hc_models.HcImagingExtendedData:
        api_response = self.hc_api.hc_imaging_extended_data(device_id, round_id, tray_id)
        return hc_models.HcImagingExtendedData.from_dict(api_response)

    def hc_rgb_image_measure(self, id) -> hc_models.HcRgbImageMeasure:
        api_response = self.hc_api.hc_rgb_image_measure(id)
        return hc_models.HcRgbImageMeasure.from_dict(api_response)

    def hc_rgb_image(self, device_id, round_id, tray_id) -> hc_models.HcRgbImage:
        api_response = self.hc_api.hc_rgb_image(device_id, round_id, tray_id)
        return hc_models.HcRgbImage.from_dict(api_response)

    def hc_plant_mask_measure(self, id) -> hc_models.HcPlantMaskMeasure:
        api_response = self.hc_api.hc_plant_mask_measure(id)
        return hc_models.HcPlantMaskMeasure.from_dict(api_response)
    
    def hc_plant_mask(self, device_id, round_id, tray_id) -> hc_models.HcPlantMask:
        api_response = self.hc_api.hc_plant_mask(device_id, round_id, tray_id)
        return hc_models.HcPlantMask.from_dict(api_response)

    def hc_param(self,id) -> hc_models.HcParamWrapper:
        api_response = self.hc_api.hc_param(id)
        return hc_models.HcParamWrapper.from_dict(api_response)

    def hc_param_used_analyse(self,id) -> hc_models.HcParamUsedAnalyse:
        api_response = self.hc_api.hc_param_used_analyse(id)
        return hc_models.HcParamUsedAnalyse.from_dict(api_response)

    def hc_param_used(self,device_id, round_id, tray_id) -> hc_models.HcParamUsed:
        api_response = self.hc_api.hc_param_used(device_id, round_id, tray_id)
        return hc_models.HcParamUsed.from_dict(api_response)

    def hc_param_image_analyse(self, id, param_id) -> hc_models.HcParamImageAnalyse:
        api_response = self.hc_api.hc_param_image_analyse(id, param_id)
        return hc_models.HcParamImageAnalyse.from_dict(api_response)
    
    def hc_param_image(self, device_id, round_id, tray_id, param_id) -> hc_models.HcParamImage:
        api_response = self.hc_api.hc_param_image(device_id, round_id, tray_id, param_id)
        return hc_models.HcParamImage.from_dict(api_response)
    
    def hc_plant_param_analyse(self, id, param_id) -> hc_models.HcPlantParamAnalyse:
        api_response = self.hc_api.hc_plant_param_analyse(id, param_id)
        return hc_models.HcPlantParamAnalyse.from_dict(api_response)

    def hc_plant_param(self, device_id, round_id, tray_id, param_id) -> hc_models.HcPlantParam:
        api_response = self.hc_api.hc_plant_param(device_id, round_id, tray_id, param_id)
        return hc_models.HcPlantParam.from_dict(api_response)

    def hc_leaf_param_analyse(self, id, param_id) -> hc_models.HcLeafParamAnalyse:
        api_response = self.hc_api.hc_leaf_param_analyse(id, param_id)
        return hc_models.HcLeafParamAnalyse.from_dict(api_response)

    def hc_leaf_param(self, device_id, round_id, tray_id, param_id) -> hc_models.HcLeafParam:
        api_response = self.hc_api.hc_leaf_param(device_id, round_id, tray_id, param_id)
        return hc_models.HcLeafParam.from_dict(api_response)
    
# Ir API
    def ir_imaging_measure(self, id) -> ir_models.IrImagingMeasure:
        api_response = self.ir_api.ir_imaging_measure(id)
        return ir_models.IrImagingMeasure.from_dict(api_response)

    def ir_imaging(self, device_id, round_id, tray_id) -> ir_models.IrImaging:
        api_response = self.ir_api.ir_imaging(device_id, round_id, tray_id)
        return ir_models.IrImaging.from_dict(api_response)

    def ir_imaging_extended_data_measure(self, id) -> ir_models.IrImagingExtendedDataMeasure:
        api_response = self.ir_api.ir_imaging_extended_data_measure(id)
        return ir_models.IrImagingExtendedDataMeasure.from_dict(api_response)

    def ir_imaging_extended_data(self, device_id, round_id, tray_id) -> ir_models.IrImagingExtendedData:
        api_response = self.ir_api.ir_imaging_extended_data(device_id, round_id, tray_id)
        return ir_models.IrImagingExtendedData.from_dict(api_response)

    def ir_plant_mask_measure(self, id) -> ir_models.IrPlantMaskMeasure:
        api_response = self.ir_api.ir_plant_mask_measure(id)
        return ir_models.IrPlantMaskMeasure.from_dict(api_response)

    def ir_plant_mask(self, device_id, round_id, tray_id) -> ir_models.IrPlantMask:
        api_response = self.ir_api.ir_plant_mask(device_id, round_id, tray_id)
        return ir_models.IrPlantMask.from_dict(api_response)

    def ir_plant_mask_image_measure(self, id) -> ir_models.IrPlantMaskImageMeasure:
        api_response = self.ir_api.ir_plant_mask_image_measure(id)
        return ir_models.IrPlantMaskImageMeasure.from_dict(api_response)

    def ir_plant_mask_image(self, device_id, round_id, tray_id) -> ir_models.IrPlantMaskImage:
        api_response = self.ir_api.ir_plant_mask_image(device_id, round_id, tray_id)
        return ir_models.IrPlantMaskImage.from_dict(api_response)

    def ir_param(self, id) -> ir_models.IrParamWrappper:
        api_response = self.ir_api.ir_param(id)
        return ir_models.IrParamWrappper.from_dict(api_response)

    def ir_param_used_analyse(self, id) -> ir_models.IrParamUsedAnalyse:
        api_response = self.ir_api.ir_param_used_analyse(id)
        return ir_models.IrParamUsedAnalyse.from_dict(api_response)

    def ir_param_used(self, device_id, round_id, tray_id) -> ir_models.IrParamUsed:
        api_response = self.ir_api.ir_param_used(device_id, round_id, tray_id)
        return ir_models.IrParamUsed.from_dict(api_response)

    def ir_plant_param_analyse(self, id, param_id) -> ir_models.IrPlantParamAnalyse:
        api_response = self.ir_api.ir_plant_param_analyse(id, param_id)
        return ir_models.IrPlantParamAnalyse.from_dict(api_response)

    def ir_plant_param(self, device_id, round_id, tray_id, param_id) -> ir_models.IrPlantParam:
        api_response = self.ir_api.ir_plant_param(device_id, round_id, tray_id, param_id)
        return ir_models.IrPlantParam.from_dict(api_response)
    
    def ir_leaf_param_analyse(self, id, param_id) -> ir_models.IrLeafParamAnalyse:
        api_response = self.ir_api.ir_leaf_param_analyse(id, param_id)
        return ir_models.IrLeafParamAnalyse.from_dict(api_response)

    def ir_leaf_param(self, device_id, round_id, tray_id, param_id) -> ir_models.IrLeafParam:
        api_response = self.ir_api.ir_leaf_param(device_id, round_id, tray_id, param_id)
        return ir_models.IrLeafParam.from_dict(api_response)

# Probe API
    
    def probe(self) -> probe_models.ProbeWrapper:
        api_response = self.probe_api.probe()
        return probe_models.ProbeWrapper.from_dict(api_response)      
    
    def probe_value_date(self, start, stop) -> probe_models.ProbeValuesDate:
        api_response = self.probe_api.probe_value_date(start, stop)
        return probe_models.ProbeValuesDate.from_dict(api_response)  
    
    def probe_value_date_probe(self, id, start, stop) -> probe_models.ProbeValueDateProbe:
        api_response = self.probe_api.probe_value_date_probe(id, start, stop)
        return probe_models.ProbeValueDateProbe.from_dict(api_response)
    

############################################# TODO Test #################################################################
# Msc API
    def msc_imaging_measure(self, id) -> msc_models.MscImagingMeasure:
        api_response = self.msc_api.msc_imaging_measure(id)
        return msc_models.MscImagingMeasure.from_dict(api_response)
    
    def msc_imaging(self, device_id, round_id, tray_id) -> msc_models.MscImaging:
        api_response = self.msc_api.msc_imaging(device_id, round_id, tray_id)
        return msc_models.MscImaging.from_dict(api_response)
    
    def msc_imaging_extended_data_measure(self, id) -> msc_models.MscImagingExtendedDataMeasure:
        api_response = self.msc_api.msc_imaging_extended_data_measure(id)
        return msc_models.MscImagingExtendedDataMeasure.from_dict(api_response)
    
    def msc_imaging_extended_data(self, device_id, round_id, tray_id) -> msc_models.MscImagingExtendedData:
        api_response = self.msc_api.msc_imaging_extended_data(device_id, round_id, tray_id)
        return msc_models.MscImagingExtendedData.from_dict(api_response)

    def msc_plant_mask_measure(self, id) -> msc_models.MscPlantMaskMeasure:
        api_response = self.msc_api.msc_plant_mask_measure(id)
        return msc_models.MscPlantMaskMeasure.from_dict(api_response)
    
    def msc_plant_mask_meamsc_plant_masksure(self, device_id, round_id, tray_id) -> msc_models.MscPlantMask:
        api_response = self.msc_api.msc_plant_mask(device_id, round_id, tray_id)
        return msc_models.MscPlantMask.from_dict(api_response)
    
    def msc_param(self, id) -> msc_models.MscParamWrapper:
        api_response = self.msc_api.msc_param(id)
        return msc_models.MscParamWrapper.from_dict(api_response)   
    
    def msc_param_used_analyse(self, id) -> msc_models.MscParamUsedAnalyse:
        api_response = self.msc_api.msc_param_used_analyse(id)
        return msc_models.MscParamUsedAnalyse.from_dict(api_response)   

    def msc_param_used(self, device_id, round_id, tray_id) -> msc_models.MscParamUsed:
        api_response = self.msc_api.msc_param_used(device_id, round_id, tray_id)
        return msc_models.MscParamUsed.from_dict(api_response)   

    def msc_param_image_analyse(self, id, param_id) -> msc_models.MscParamImageAnalyse:
        api_response = self.msc_api.msc_param_image_analyse(id, param_id)
        return msc_models.MscParamImageAnalyse.from_dict(api_response)     

    def msc_param_image(self, device_id, round_id, tray_id, param_id) -> msc_models.MscParamImageWrapper:
        api_response = self.msc_api.msc_param_image(device_id, round_id, tray_id, param_id)
        return msc_models.MscParamImageWrapper.from_dict(api_response)     
 
    def msc_plant_param_analyse(self, id, param_id) -> msc_models.MscPlantParamAnalyse:
        api_response = self.msc_api.msc_plant_param_analyse(id, param_id)
        return msc_models.MscPlantParamAnalyse.from_dict(api_response)        

    def msc_leaf_param_analyse(self, id, param_id) -> msc_models.MscLeafParamAnalyse:
        api_response = self.msc_api.msc_leaf_param_analyse(id, param_id)
        return msc_models.MscLeafParamAnalyse.from_dict(api_response)        

    def msc_leaf_param(self, device_id, round_id, tray_id, param_id) -> msc_models.MscLeafParam:
        api_response = self.msc_api.msc_leaf_param(device_id, round_id, tray_id, param_id)
        return msc_models.MscLeafParam.from_dict(api_response)    
    
    def msc_light_set(self, id) -> msc_models.MscLightSet:
        api_response = self.msc_api.msc_light_set(id)
        return msc_models.MscLightSet.from_dict(api_response)    

    def msc_light_set_used(self, device_id, round_id, tray_id) -> msc_models.MscLightSetUsed:
        api_response = self.msc_api.msc_light_set_used(device_id, round_id, tray_id)
        return msc_models.MscLightSetUsed.from_dict(api_response)       

    def msc_calibration(self, id) -> msc_models.MscCalibration:
        api_response = self.msc_api.msc_calibration(id)
        return msc_models.MscCalibration.from_dict(api_response)       

    def msc_calibration_light_set(self, id) -> msc_models.MscCalibrationLightSet:  
        api_response = self.msc_api.msc_calibration_light_set(id)
        return msc_models.MscCalibrationLightSet.from_dict(api_response)       

    def msc_calibration_light(self) -> msc_models.MscCalibrationLight:
        api_response = self.msc_api.msc_calibration_light()
        return msc_models.MscCalibrationLight.from_dict(api_response)       

# RGB API
    def rgb_imaging_measure(self, id) -> rgb_models.RgbImagingMeasure:
        api_response = self.rgb_api.rgb_imaging_measure(id)
        return rgb_models.RgbImagingMeasure.from_dict(api_response)       

    def rgb_imaging(self, device_id, round_id, tray_id) -> rgb_models.RgbImaging:
        api_response = self.rgb_api.rgb_imaging(device_id, round_id, tray_id)
        return rgb_models.RgbImaging.from_dict(api_response)       
    
    def rgb_imaging_extended_data_measure(self, id) -> rgb_models.RgbImagingExtendedDataMeasure:
        api_response = self.rgb_api.rgb_imaging_extended_data_measure(id)
        return rgb_models.RgbImagingExtendedDataMeasure.from_dict(api_response)  
    
    def rgb_imaging_extended_data(self, device_id, round_id, tray_id) -> rgb_models.RgbImagingExtendedData:
        api_response = self.rgb_api.rgb_imaging_extended_data(device_id, round_id, tray_id)
        return rgb_models.RgbImagingExtendedData.from_dict(api_response)  
    
    def rgb_plant_mask_measure(self, id) -> rgb_models.RgbPlantMaskMeasure:
        api_response = self.rgb_api.rgb_plant_mask_measure(id)
        return rgb_models.RgbPlantMaskMeasure.from_dict(api_response)      
    
    def rgb_plant_mask(self, device_id, round_id, tray_id) -> rgb_models.RgbPlantMask:
        api_response = self.rgb_api.rgb_plant_mask(device_id, round_id, tray_id)
        return rgb_models.RgbPlantMask.from_dict(api_response)        
    
    def rgb_greening_mask_image_measure(self, id) -> rgb_models.RgbGreeningMaskImageMeasure:
        api_response = self.rgb_api.rgb_greening_mask_image_measure(id)
        return rgb_models.RgbGreeningMaskImageMeasure.from_dict(api_response)
    
    def rgb_greening_mask_image(self, device_id, round_id, tray_id) -> rgb_models.RgbGreeningMaskImage:
        api_response = self.rgb_api.rgb_greening_mask_image(device_id, round_id, tray_id)
        return rgb_models.RgbGreeningMaskImage.from_dict(api_response)
    
    def rgb_param(self, id) -> rgb_models.RgbParamWrapper:
        api_response = self.rgb_api.rgb_param(id)
        return rgb_models.RgbParamWrapper.from_dict(api_response)
    
    def rgb_param_used_analyse(self, id) -> rgb_models.RgbParamUsedAnalyse:
        api_response = self.rgb_api.rgb_param_used_analyse(id)
        return rgb_models.RgbParamUsedAnalyse.from_dict(api_response)

    def rgb_param_used(self, device_id, round_id, tray_id) -> rgb_models.RgbParamUsed:
        api_response = self.rgb_api.rgb_param_used(device_id, round_id, tray_id)
        return rgb_models.RgbParamUsed.from_dict(api_response)

    def rgb_param_color_used_analyse(self, id) -> rgb_models.RgbParamColorUsedAnalyse:
        api_response = self.rgb_api.rgb_param_color_used_analyse(id)
        return rgb_models.RgbParamColorUsedAnalyse.from_dict(api_response)

    def rgb_param_color_used(self, device_id, round_id, tray_id) -> rgb_models.RgbParamColorUsed:
        api_response = self.rgb_api.rgb_param_color_used(device_id, round_id, tray_id)
        return rgb_models.RgbParamColorUsed.from_dict(api_response)

    def rgb_plant_param_analyse(self, id, param_id) -> rgb_models.RgbPlantParamAnalyse:
        api_response = self.rgb_api.rgb_plant_param_analyse(id, param_id)
        return rgb_models.RgbPlantParamAnalyse.from_dict(api_response)

    def rgb_plant_param(self, device_id, round_id, tray_id, param_id) -> rgb_models.RgbPlantParam:
        api_response = self.rgb_api.rgb_plant_param(device_id, round_id, tray_id, param_id)
        return rgb_models.RgbPlantParam.from_dict(api_response)
    
    def rgb_plant_param_color_analyse(self,id, param_id) -> rgb_models.RgbPlantParamColorAnalyse:
        api_response = self.rgb_api.rgb_plant_param_color_analyse(id, param_id)
        return rgb_models.RgbPlantParamColorAnalyse.from_dict(api_response)

    def rgb_plant_param_color(self, device_id, round_id, tray_id, param_id) -> rgb_models.RgbPlantParamColor:
        api_response = self.rgb_api.rgb_plant_param_color(device_id, round_id, tray_id, param_id)
        return rgb_models.RgbPlantParamColor.from_dict(api_response)

    def rgb_leaf_param_analyse(self, id, param_id) -> rgb_models.RgbLeafParamAnalyse:
        api_response = self.rgb_api.rgb_leaf_param_analyse(id, param_id)
        return rgb_models.RgbLeafParamAnalyse.from_dict(api_response)

    def rgb_leaf_param(self, device_id, round_id, tray_id, param_id) -> rgb_models.RgbLeafParam:
        api_response = self.rgb_api.rgb_leaf_param(device_id, round_id, tray_id, param_id)
        return rgb_models.RgbLeafParam.from_dict(api_response)

    def rgb_leaf_param_color_analyse(self, id, param_id) -> rgb_models.RgbLeafParamColorAnalyse:
        api_response = self.rgb_api.rgb_leaf_param_color_analyse(id, param_id)
        return rgb_models.RgbLeafParamColorAnalyse.from_dict(api_response)

    def rgb_leaf_param_color(self, device_id, round_id, tray_id, param_id) -> rgb_models.RgbLeafParamColor:
        api_response = self.rgb_api.rgb_leaf_param_color(device_id, round_id, tray_id, param_id)
        return rgb_models.RgbLeafParamColor.from_dict(api_response)

# Scan3d API
    def scan3d_imaging_measure(self, id) -> scan3d_models.Scan3dImagingMeasure:
        api_response = self.scan3d_api.scan3d_imaging_measure(id)
        return scan3d_models.Scan3dImagingMeasure.from_dict(api_response)       

    def scan3d(self, device_id, round_id, tray_id) -> scan3d_models.Scan3d:
        api_response = self.scan3d_api.scan3d(device_id, round_id, tray_id)
        return scan3d_models.Scan3d.from_dict(api_response)       

    def scan3d_imaging_extended_data_measure(self,id) -> scan3d_models.Scan3dImagingExtendedDataMeasure:
        api_response = self.scan3d_api.scan3d_imaging_extended_data_measure(id)
        return scan3d_models.Scan3dImagingExtendedDataMeasure.from_dict(api_response)   

    def i_scan3d_imaging_extended_data(self, device_id, round_id, tray_id) -> scan3d_models.Scan3dImagingExtendedData:
        api_response = self.scan3d_api.i_scan3d_imaging_extended_data(device_id, round_id, tray_id)
        return scan3d_models.Scan3dImagingExtendedData.from_dict(api_response)   

    def scan3d_analyzed_model_measure(self, id) -> scan3d_models.Scan3dAnalyzedModelMeasure:
        api_response = self.scan3d_api.scan3d_analyzed_model_measure(id)
        return scan3d_models.Scan3dAnalyzedModelMeasure.from_dict(api_response)   

    def scan3d_analysed_model_analyse(self, id) -> scan3d_models.Scan3dAnalysedModelAnalyse:
        api_response = self.scan3d_api.scan3d_analysed_model_analyse(id)
        return scan3d_models.Scan3dAnalysedModelAnalyse.from_dict(api_response)   

    def scan3d_analyzed_model(self, device_id, round_id, tray_id) -> scan3d_models.Scan3dAnalyzedModel:
        api_response = self.scan3d_api.scan3d_analyzed_model(device_id, round_id, tray_id)
        return scan3d_models.Scan3dAnalyzedModel.from_dict(api_response)   


    def scan3d_param(self, id) -> scan3d_models.Scan3dParamWrapper:
        api_response = self.scan3d_api.scan3d_param(id)
        return scan3d_models.Scan3dParamWrapper.from_dict(api_response)   

    def scan3d_param_used_analyse(self, id) -> scan3d_models.Scan3dParamUsedAnalyse:
        api_response = self.scan3d_api.scan3d_param_used_analyse(id)
        return scan3d_models.Scan3dParamUsedAnalyse.from_dict(api_response)   

    def scan3d_param_used(self, device_id, round_id, tray_id) -> scan3d_models.Scan3dParamUsed:
        api_response = self.scan3d_api.scan3d_param_used(device_id, round_id, tray_id)
        return scan3d_models.Scan3dParamUsed.from_dict(api_response)   

    def scan3d_plant_param_analyse(self, id, param_id) -> scan3d_models.Scan3dPlantParamAnalyse:
        api_response = self.scan3d_api.scan3d_plant_param_analyse(id, param_id)
        return scan3d_models.Scan3dPlantParamAnalyse.from_dict(api_response)   

    def scan3d_plant_param(self, device_id, round_id, tray_id, param_id) -> scan3d_models.Scan3dPlantParam:
        api_response = self.scan3d_api.scan3d_plant_param(device_id, round_id, tray_id, param_id)
        return scan3d_models.Scan3dPlantParam.from_dict(api_response)   

    def scan3d_leaf_param_analyse(self, id, param_id) -> scan3d_models.Scan3dLeafParamAnalyse:
        api_response = self.scan3d_api.scan3d_leaf_param_analyse(id, param_id)
        return scan3d_models.Scan3dLeafParamAnalyse.from_dict(api_response)   

    def scan3d_leaf_param(self,device_id, round_id, tray_id, param_id) -> scan3d_models.Scan3dLeafParam:
        api_response = self.scan3d_api.scan3d_leaf_param(device_id, round_id, tray_id, param_id)
        return scan3d_models.Scan3dLeafParam.from_dict(api_response)   

# Scales API
    def scales_plant_weight_measure(self, id) -> scales_models.ScalesPlantWeightMeasure:
        api_response = self.scales_api.scales_plant_weight_measure(id)
        return scales_models.ScalesPlantWeightMeasure.from_dict(api_response)       

    def get_scales_plant_weight(self, device_id, round_id, tray_id) -> scales_models.ScalesPlantWeight:
        api_response = self.scales_api.scales_plant_weight(device_id, round_id, tray_id)
        return scales_models.ScalesPlantWeight.from_dict(api_response)  

    def get_scales_weight_reference_plant(self, id) -> scales_models.ScalesWeightReferencePlant:
        api_response = self.scales_api.scales_weight_reference_plant(id)
        return scales_models.ScalesWeightReferencePlant.from_dict(api_response)  

    def get_scales_weight_reference_tray(self, id) -> scales_models.ScalesWeightReferenceTray:
        api_response = self.scales_api.scales_weight_reference_tray(id)
        return scales_models.ScalesWeightReferenceTray.from_dict(api_response)  

    def get_scales_weight_reference_to_date_tray(self, id, _date) -> scales_models.ScalesWeightReferenceToDateTray:
        api_response = self.scales_api.scales_weight_reference_to_date_tray(id, _date)
        return scales_models.ScalesWeightReferenceToDateTray.from_dict(api_response)  

# Spray API
    def get_spray_action(self, device_id, round_id, tray_id) -> spray_models.SprayAction:
        api_response = self.spray_api.spray_action(device_id, round_id, tray_id)
        return spray_models.SprayAction.from_dict(api_response)  

# Spectrum Device API
    def get_spectrum_device_id(self) -> spectrum_device_models.SpectrumDeviceID:
        api_response = self.spectrum_device_api.spectrum_device_id()
        return spectrum_device_models.SpectrumDeviceID.from_dict(api_response)  

    def get_spectrum_device(self, id) -> spectrum_device_models.SpectrumDeviceWrapper:
        api_response = self.spectrum_device_api.spectrum_device(id)
        return spectrum_device_models.SpectrumDevice.from_dict(api_response)  

    def get_spectrum_values_date_device(self, id, start, stop) -> spectrum_device_models.SpectrumValuesDateDevice:
        api_response = self.spectrum_device_api.spectrum_values_date_device(id, start, stop)
        return spectrum_device_models.SpectrumValuesDateDevice.from_dict(api_response)  

# Buffer API
    def get_buffer_history(self, id) -> buffer_models.BufferHistoryWrapper:
        api_response = self.buffer_api.buffer_history(id)
        return buffer_models.BufferHistoryWrapper.from_dict(api_response)  

    def get_buffer_history_date(self, start, stop) -> buffer_models.BufferHistoryDate:
        api_response = self.buffer_api.buffer_history_date(start, stop)
        return buffer_models.BufferHistoryDate.from_dict(api_response)  

# System Log API
    def get_system_log_round(self, id) -> system_log_models.SystemLogRound:
        api_response = self.system_log_api.system_log_round(id)
        return system_log_models.SystemLogRound.from_dict(api_response)  

    def get_system_log_date_round(self, id, start, stop) -> system_log_models.SystemLogDateRound:
        api_response = self.system_log_api.system_log_date_round(id, start, stop)
        return system_log_models.SystemLogDateRound.from_dict(api_response)  

    def get_system_log_tray(self, id) -> system_log_models.SystemLogTray:
        api_response = self.system_log_api.system_log_tray(id)
        return system_log_models.SystemLogTray.from_dict(api_response)  

    def get_system_log_date_tray(self, id, start, stop) -> system_log_models.SystemLogDateTray:
        api_response = self.system_log_api.system_log_date_tray(id, start, stop)
        return system_log_models.SystemLogDateTray.from_dict(api_response)  

    def get_system_log_log_type(self) -> system_log_models.SystemLogLogType:
        api_response = self.system_log_api.system_log_log_type()
        return system_log_models.SystemLogLogType.from_dict(api_response)  

    def get_system_log_date_log_type(self, type, start, stop) -> system_log_models.SystemLogDateLogType:
        api_response = self.system_log_api.system_log_date_log_type(type, start, stop)
        return system_log_models.SystemLogDateLogType.from_dict(api_response)  

    def get_system_log_log_tag(self) -> system_log_models.SystemLogLogTag:
        api_response = self.system_log_api.system_log_log_tag()
        return system_log_models.SystemLogLogTag.from_dict(api_response)  

    def get_system_log_date_log_tag(self, tag, start, stop) -> system_log_models.SystemLogDateLogTag:
        api_response = self.system_log_api.system_log_date_log_tag(tag, start, stop)
        return system_log_models.SystemLogDateLogTag.from_dict(api_response)  

# Version Info API
    def version_info(self) -> version_info_modes.VersionInfo:
        api_response = self.version_info_api.version_info()
        return version_info_modes.VersionInfo.from_dict(api_response)  





