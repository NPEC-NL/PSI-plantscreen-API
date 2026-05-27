# CompleteAPIClient API Reference

This page documents all public methods of the `CompleteAPIClient` class.


For example implemenations please see: [example_implementation.py](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_implementation.py)

## action

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Action](docs/Action.md)

---

## action_experiment

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Action](docs/Action.md)]

---

## action_group

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[ActionGroup](docs/ActionGroup.md)

---

## action_group_round

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[ActionGroup](docs/ActionGroup.md)

---

## action_not_done_experiment

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Action](docs/Action.md)]

---

## action_protocol

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[ActionProtocol](docs/ActionProtocol.md)

---

## action_protocol_round

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[ActionProtocol](docs/ActionProtocol.md)

---

## buffer_history

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[BufferHistory](docs/BufferHistory.md)

---

## buffer_history_date

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[BufferHistory](docs/BufferHistory.md)]

---

## device

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Device](docs/Device.md)

---

## device_active

### Return type

List[[Device](docs/Device.md)]

---

## device_profile

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Device](docs/Device.md)]

---

## experiment

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Experiment](docs/Experiment.md)

---

## experiment_date

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[Experiment](docs/Experiment.md)]

---

## experiment_id

### Return type

list[int]

---

## experiment_owner

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Experiment](docs/Experiment.md)]

---

## note_experiment

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[ExperimentNote](docs/ExperimentNote.md)]

---

## owner

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**ids** | **List[int]** | list of IDs of the resources. | 

### Return type

List[[Owner](docs/Owner.md)]

---

## owner_id

### Return type

list[int]

---

## fc_imaging

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[FcImaging](docs/FcImaging.md)]

---

## fc_imaging_extended_data

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

[MeasureExtendedData](docs/MeasureExtendedData.md)

---

## fc_imaging_extended_data_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[MeasureExtendedData](docs/MeasureExtendedData.md)

---

## fc_imaging_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[FcImaging](docs/FcImaging.md)

---

## fc_leaf_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[LeafParameter](docs/LeafParameter.md)]

---

## fc_leaf_param_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[LeafParameter](docs/LeafParameter.md)]

---

## fc_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Parameter](docs/Parameter.md)

---

## fc_param_image

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[ParameterImage](docs/ParameterImage.md)]

---

## fc_param_image_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

[ParameterImage](docs/ParameterImage.md)

---

## fc_param_used

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## fc_param_used_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## fc_plant_mask

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[PlantMask](docs/PlantMask.md)]

---

## fc_plant_mask_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[PlantMask](docs/PlantMask.md)

---

## fc_plant_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[PlantParameter](docs/PlantParameter.md)]

---

## fc_plant_param_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[PlantParameter](docs/PlantParameter.md)]

---

## file

### Return type

None

---

## file_changelog

### Return type

str

---

## hc_imaging

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[HcImaging](docs/HcImaging.md)]

---

## hc_imaging_extended_data

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

[MeasureExtendedData](docs/MeasureExtendedData.md)

---

## hc_imaging_extended_data_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[MeasureExtendedData](docs/MeasureExtendedData.md)

---

## hc_imaging_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[HcImaging](docs/HcImaging.md)

---

## hc_leaf_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[StatisticLeafParameter](docs/StatisticLeafParameter.md)]

---

## hc_leaf_param_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[StatisticLeafParameter](docs/StatisticLeafParameter.md)]

---

## hc_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Parameter](docs/Parameter.md)

---

## hc_param_image

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[ParameterImage](docs/ParameterImage.md)]

---

## hc_param_image_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

[ParameterImage](docs/ParameterImage.md)

---

## hc_param_used

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## hc_param_used_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## hc_plant_mask

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[PlantMask](docs/PlantMask.md)]

---

## hc_plant_mask_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[PlantMask](docs/PlantMask.md)

---

## hc_plant_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[StatisticPlantParameter](docs/StatisticPlantParameter.md)]

---

## hc_plant_param_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[StatisticPlantParameter](docs/StatisticPlantParameter.md)]

---

## hc_rgb_image

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[HcRgbImage](docs/HcRgbImage.md)]

---

## hc_rgb_image_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[HcRgbImage](docs/HcRgbImage.md)

---

## ir_imaging

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Imaging](docs/Imaging.md)]

---

## ir_imaging_extended_data

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

[MeasureExtendedData](docs/MeasureExtendedData.md)

---

## ir_imaging_extended_data_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[MeasureExtendedData](docs/MeasureExtendedData.md)

---

## ir_imaging_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Imaging](docs/Imaging.md)

---

## ir_leaf_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[StatisticLeafParameter](docs/StatisticLeafParameter.md)]

---

## ir_leaf_param_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[StatisticLeafParameter](docs/StatisticLeafParameter.md)]

---

## ir_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Parameter](docs/Parameter.md)

---

## ir_param_used

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## ir_param_used_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## ir_plant_mask

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[PlantMask](docs/PlantMask.md)]

---

## ir_plant_mask_image

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Imaging](docs/Imaging.md)]

---

## ir_plant_mask_image_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Imaging](docs/Imaging.md)

---

## ir_plant_mask_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[PlantMask](docs/PlantMask.md)

---

## ir_plant_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[StatisticPlantParameter](docs/StatisticPlantParameter.md)]

---

## ir_plant_param_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[StatisticPlantParameter](docs/StatisticPlantParameter.md)]

---

## msc_calibration

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[MscCalibration](docs/MscCalibration.md)

---

## msc_calibration_light

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **Optional[int]** | ID of the resource. | 

### Return type

[MscCalibrationLight](docs/MscCalibrationLight.md)

---

## msc_calibration_light_set

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[MscCalibration](docs/MscCalibration.md)

---

## msc_imaging

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Imaging](docs/Imaging.md)]

---

## msc_imaging_extended_data

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

[MeasureExtendedData](docs/MeasureExtendedData.md)

---

## msc_imaging_extended_data_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[MeasureExtendedData](docs/MeasureExtendedData.md)

---

## msc_imaging_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Imaging](docs/Imaging.md)]

---

## msc_leaf_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[StatisticLeafParameter](docs/StatisticLeafParameter.md)]

---

## msc_leaf_param_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[StatisticLeafParameter](docs/StatisticLeafParameter.md)]

---

## msc_light_set

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[MscLightSet](docs/MscLightSet.md)

---

## msc_light_set_used

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[MscLightSet](docs/MscLightSet.md)]

---

## msc_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Parameter](docs/Parameter.md)

---

## msc_param_image

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[ParameterImage](docs/ParameterImage.md)]

---

## msc_param_image_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

[ParameterImage](docs/ParameterImage.md)

---

## msc_param_used

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## msc_param_used_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## msc_plant_mask

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[PlantMask](docs/PlantMask.md)]

---

## msc_plant_mask_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[PlantMask](docs/PlantMask.md)

---

## msc_plant_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[StatisticPlantParameter](docs/StatisticPlantParameter.md)]

---

## msc_plant_param_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[StatisticPlantParameter](docs/StatisticPlantParameter.md)]

---

## plant

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**ids** | **List[int]** | list of IDs of the resources. | 

### Return type

List[[Plant](docs/Plant.md)]

---

## plant_height_round

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[PlantHeight](docs/PlantHeight.md)]

---

## plant_leaf

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[PlantLeaf](docs/PlantLeaf.md)]

---

## plant_tray

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Plant](docs/Plant.md)]

---

## plant_tray_profile

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Plant](docs/Plant.md)]

---

## plant_tray_profile_tray

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[Plant](docs/Plant.md)]

---

## probe

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Probe](docs/Probe.md)

---

## probe_value_date

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[ProbeValue](docs/ProbeValue.md)]

---

## probe_value_date_probe

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[ProbeValue](docs/ProbeValue.md)]

---

## profile

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[SystemProfile](docs/SystemProfile.md)

---

## profile_active

### Return type

[SystemProfile](docs/SystemProfile.md)

---

## profile_id

### Return type

list[int]

---

## rgb_greening_mask_image

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[RgbGreeningMaskImage](docs/RgbGreeningMaskImage.md)]

---

## rgb_greening_mask_image_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[RgbGreeningMaskImage](docs/RgbGreeningMaskImage.md)

---

## rgb_imaging

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Imaging](docs/Imaging.md)]

---

## rgb_imaging_extended_data

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

[MeasureExtendedData](docs/MeasureExtendedData.md)

---

## rgb_imaging_extended_data_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[MeasureExtendedData](docs/MeasureExtendedData.md)

---

## rgb_imaging_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Imaging](docs/Imaging.md)

---

## rgb_leaf_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[LeafParameter](docs/LeafParameter.md)]

---

## rgb_leaf_param_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[LeafParameter](docs/LeafParameter.md)]

---

## rgb_leaf_param_color

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[LeafParameter](docs/LeafParameter.md)]

---

## rgb_leaf_param_color_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[LeafParameter](docs/LeafParameter.md)]

---

## rgb_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Parameter](docs/Parameter.md)

---

## rgb_param_color_used

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## rgb_param_color_used_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## rgb_param_used

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## rgb_param_used_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## rgb_plant_mask

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[PlantMask](docs/PlantMask.md)]

---

## rgb_plant_mask_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[PlantMask](docs/PlantMask.md)

---

## rgb_plant_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[PlantParameter](docs/PlantParameter.md)]

---

## rgb_plant_param_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[PlantParameter](docs/PlantParameter.md)]

---

## rgb_plant_param_color

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[PlantParameter](docs/PlantParameter.md)]

---

## rgb_plant_param_color_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[PlantParameter](docs/PlantParameter.md)]

---

## round

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Round](docs/Round.md)

---

## round_date_experiment

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[Round](docs/Round.md)]

---

## round_experiment

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Round](docs/Round.md)]

---

## round_order_date_experiment

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[RoundOrder](docs/RoundOrder.md)]

---

## round_order_experiment

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[RoundOrder](docs/RoundOrder.md)]

---

## round_order_round

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[RoundOrder](docs/RoundOrder.md)

---

## scales_plant_weight

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[ScalesData](docs/ScalesData.md)]

---

## scales_plant_weight_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[ScalesData](docs/ScalesData.md)

---

## scales_weight_reference_plant

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[PlantWeightReference](docs/PlantWeightReference.md)

---

## scales_weight_reference_to_date_tray

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**var_date** | **datetime** |  | 

### Return type

List[[PlantWeightReference](docs/PlantWeightReference.md)]

---

## scales_weight_reference_tray

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[PlantWeightReference](docs/PlantWeightReference.md)]

---

## scan3d

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Scan3DImaging](docs/Scan3DImaging.md)]

---

## scan3d_analyzed_model

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Scan3DAnalyzedModel](docs/Scan3DAnalyzedModel.md)]

---

## scan3d_analyzed_model_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Scan3DAnalyzedModel](docs/Scan3DAnalyzedModel.md)]

---

## scan3d_analyzed_model_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Scan3DAnalyzedModel](docs/Scan3DAnalyzedModel.md)]

---

## scan3d_imaging_extended_data

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

[MeasureExtendedData](docs/MeasureExtendedData.md)

---

## scan3d_imaging_extended_data_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[MeasureExtendedData](docs/MeasureExtendedData.md)

---

## scan3d_imaging_measure

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Scan3DImaging](docs/Scan3DImaging.md)

---

## scan3d_leaf_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[LeafParameter](docs/LeafParameter.md)]

---

## scan3d_leaf_param_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[LeafParameter](docs/LeafParameter.md)]

---

## scan3d_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Parameter](docs/Parameter.md)

---

## scan3d_param_used

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## scan3d_param_used_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Parameter](docs/Parameter.md)]

---

## scan3d_plant_param

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[PlantParameter](docs/PlantParameter.md)]

---

## scan3d_plant_param_analyse

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**param_id** | **int** | ID of the parameter. | 

### Return type

List[[PlantParameter](docs/PlantParameter.md)]

---

## spectrum_device

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[SpectrumDevice](docs/SpectrumDevice.md)

---

## spectrum_device_id

### Return type

List[[SpectrumDeviceID](docs/SpectrumDeviceID.md)]

---

## spectrum_values_date_device

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[SpectrumValues](docs/SpectrumValues.md)]

---

## spray_action

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**device_id** | **int** | ID of the device. | 
**round_id** | **int** | ID of the round. | 
**tray_id** | **int** | ID of the tray. | 

### Return type

List[[SprayAction](docs/SprayAction.md)]

---

## system_log_date_log_tag

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**tag** | **str** |  | 
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[SystemLog](docs/SystemLog.md)]

---

## system_log_date_log_type

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**type** | **str** |  | 
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[SystemLog](docs/SystemLog.md)]

---

## system_log_date_round

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[SystemLog](docs/SystemLog.md)]

---

## system_log_date_tray

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[SystemLog](docs/SystemLog.md)]

---

## system_log_log_tag

### Return type

List[[LogTag](docs/LogTag.md)]

---

## system_log_log_type

### Return type

List[[LogType](docs/LogType.md)]

---

## system_log_round

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[SystemLog](docs/SystemLog.md)]

---

## system_log_tray

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[SystemLog](docs/SystemLog.md)]

---

## scales_mapping_tray

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[ScalesMapping](docs/ScalesMapping.md)]

---

## tray

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[Tray](docs/Tray.md)

---

## tray_profile

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[TrayProfile](docs/TrayProfile.md)

---

## tray_profile_to_date_tray

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**var_date** | **datetime** |  | 

### Return type

[TrayProfile](docs/TrayProfile.md)

---

## tray_profile_tray

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[TrayProfile](docs/TrayProfile.md)]

---

## tray_profile_used_tray

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 
**start** | **datetime** | Start datetime for filtering results. | 
**stop** | **datetime** | Stop datetime for filtering results. | 

### Return type

List[[TrayProfile](docs/TrayProfile.md)]

---

## tray_round

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

List[[Tray](docs/Tray.md)]

---

## tray_type

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[TrayType](docs/TrayType.md)

---

## tray_type_tray

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[TrayType](docs/TrayType.md)

---

## tray_type_tray_profile

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**id** | **int** | ID of the resource. | 

### Return type

[TrayType](docs/TrayType.md)

---

## version_info

### Return type

[VersionInfo](docs/VersionInfo.md)

---

[Back to top](#) | [Back to API Endpoints](API_endpoints.md) | [Back to Models](Models.md) | [Back to README](README.md)
