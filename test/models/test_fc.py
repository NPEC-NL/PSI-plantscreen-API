"""Test Fluorcam models"""
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies

class FCModels(unittest.TestCase):
    def fc_imaging_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.action_id, exp_dict['ActionID'])
        self.assertEqual(exp_class.device_id, exp_dict['DeviceID'])
        self.assertEqual(exp_class.device_pid, exp_dict['DevicePID'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.measure_angle, exp_dict['MeasureAngle'])
        self.assertEqual(exp_class.measure_date, exp_dict['MeasureDate'])
        self.assertEqual(exp_class.measure_height, exp_dict['MeasureHeight'])
        self.assertEqual(exp_class.measure_id, exp_dict['MeasureID'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])
        self.assertEqual(exp_class.tray_barcode, exp_dict['TrayBarcode'])
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])
        self.assertEqual(exp_class.tray_profile_id, exp_dict['TrayProfileID'])
        self.assertEqual(exp_class.protocol_path, exp_dict['ProtocolPath'])
        self.assertEqual(exp_class.tar_path, exp_dict['TarPath'])

    def fc_measure_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.device_id, exp_dict['DeviceID'])
        self.assertEqual(exp_class.extended_data, exp_dict['ExtendedData'])
        self.assertEqual(exp_class.measure_date, exp_dict['MeasureDate'])
        self.assertEqual(exp_class.measure_id, exp_dict['MeasureID'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])

    def fc_mask_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.device_id, exp_dict['DeviceID'])
        self.assertEqual(exp_class.device_pid, exp_dict['DevicePID'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.mask_is_leaf, exp_dict['MaskIsLeaf'])
        self.assertEqual(exp_class.measure_angle, exp_dict['MeasureAngle'])
        self.assertEqual(exp_class.measure_date, exp_dict['MeasureDate'])
        self.assertEqual(exp_class.measure_id, exp_dict['MeasureID'])
        self.assertEqual(exp_class.plant_mask_path, exp_dict['PlantMaskPath'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])
        self.assertEqual(exp_class.tray_barcode, exp_dict['TrayBarcode'])
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])

    def fc_param_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.parameter_id, exp_dict['ParameterID'])
        self.assertEqual(exp_class.parameter_name, exp_dict['ParameterName'])
        self.assertEqual(exp_class.parameter_unit, exp_dict['ParameterUnit'])

    def fc_analyse_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.analyse_id, exp_dict['AnalyseID'])
        self.assertEqual(exp_class.device_id, exp_dict['DeviceID'])
        self.assertEqual(exp_class.device_pid, exp_dict['DevicePID'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.measure_angle, exp_dict['MeasureAngle'])
        self.assertEqual(exp_class.measure_id, exp_dict['MeasureID'])
        self.assertEqual(exp_class.parameter_id, exp_dict['ParameterID'])
        self.assertEqual(exp_class.parameter_image_path, exp_dict['ParameterImagePath'])
        self.assertEqual(exp_class.parameter_name, exp_dict['ParameterName'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])
        self.assertEqual(exp_class.tray_barcode, exp_dict['TrayBarcode'])
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])

    def fc_plant_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.analyse_id, exp_dict['AnalyseID'])
        self.assertEqual(exp_class.device_id, exp_dict['DeviceID'])
        self.assertEqual(exp_class.device_pid, exp_dict['DevicePID'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])    
        self.assertEqual(exp_class.measure_angle, exp_dict['MeasureAngle'])    
        self.assertEqual(exp_class.measure_id, exp_dict['MeasureID'])
        self.assertEqual(exp_class.parameter_id, exp_dict['ParameterID'])      
        self.assertEqual(exp_class.parameter_name, exp_dict['ParameterName'])  
        self.assertEqual(exp_class.parameter_value, exp_dict['ParameterValue'])
        self.assertEqual(exp_class.plant_barcode, exp_dict['PlantBarcode'])    
        self.assertEqual(exp_class.plant_id, exp_dict['PlantID'])
        self.assertEqual(exp_class.plant_name, exp_dict['PlantName'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])
        self.assertEqual(exp_class.tray_area, exp_dict['TrayArea'])
        self.assertEqual(exp_class.tray_barcode, exp_dict['TrayBarcode'])      
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])

    def fc_leaf_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.analyse_id, exp_dict['AnalyseID'])
        self.assertEqual(exp_class.device_id, exp_dict['DeviceID'])
        self.assertEqual(exp_class.device_pid, exp_dict['DevicePID'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.leaf_index, exp_dict['LeafIndex'])
        self.assertEqual(exp_class.measure_angle, exp_dict['MeasureAngle'])
        self.assertEqual(exp_class.measure_id, exp_dict['MeasureID'])
        self.assertEqual(exp_class.parameter_id, exp_dict['ParameterID'])
        self.assertEqual(exp_class.parameter_name, exp_dict['ParameterName'])
        self.assertEqual(exp_class.parameter_value, exp_dict['ParameterValue'])
        self.assertEqual(exp_class.plant_barcode, exp_dict['PlantBarcode'])
        self.assertEqual(exp_class.plant_id, exp_dict['PlantID'])
        self.assertEqual(exp_class.plant_name, exp_dict['PlantName'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])
        self.assertEqual(exp_class.tray_area, exp_dict['TrayArea'])
        self.assertEqual(exp_class.tray_barcode, exp_dict['TrayBarcode'])
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])

    def test_fc_imaging_meassure_none(self):
        reply = models.fc.FcImagingMeasure.from_dict({'JsonFcImagingByIDResult': None})
        self.assertEqual(reply, None)

    def test_fc_imaging_meassure(self):
        reply = models.fc.FcImagingMeasure.from_dict(replies.fc.MOCK_FC_IMAGING_MEASURE_REPLY)
        self.fc_imaging_assertor(reply, replies.fc.MOCK_FC_IMAGING_MEASURE_REPLY['JsonFcImagingByIDResult'])

    def test_fc_imaging_none(self):
        reply = models.fc.FcImagingWrapper.from_dict({'JsonFcImagingResult': None})
        self.assertEqual(reply, [])

    def test_fc_imaging_empty(self):
        reply = models.fc.FcImagingWrapper.from_dict({'JsonFcImagingResult': []})
        self.assertEqual(reply, [])

    def test_fc_imaging(self):
        reply = models.fc.FcImagingWrapper.from_dict(replies.fc.MOCK_FC_IMAGING_REPLY)
        self.assertEqual(len(reply), len(replies.fc.MOCK_FC_IMAGING_REPLY['JsonFcImagingResult']))
        for i in range(0, len(replies.fc.MOCK_FC_IMAGING_REPLY['JsonFcImagingResult'])):
            self.fc_imaging_assertor(reply[i], replies.fc.MOCK_FC_IMAGING_REPLY['JsonFcImagingResult'][i])

    def test_fc_imaging_extended_data_meassure_none(self):
        reply = models.fc.FcImagingExtendedDataMeasure.from_dict({'JsonFcMeasureExtendedDataByIDResult': None})
        self.assertEqual(reply, None)

    def test_fc_imaging_extended_data_meassure(self):
        reply = models.fc.FcImagingExtendedDataMeasure.from_dict(replies.fc.MOCK_FC_IMAGING_EXTENDED_DATA_MEASURE_REPLY)
        self.fc_measure_assertor(reply, replies.fc.MOCK_FC_IMAGING_EXTENDED_DATA_MEASURE_REPLY['JsonFcMeasureExtendedDataByIDResult'])

    def test_fc_imaging_extended_data_none(self):
        reply = models.fc.FcImagingExtendedData.from_dict({'JsonFcMeasureExtendedDataResult': None})
        self.assertEqual(reply, None)

    def test_fc_imaging_extended_data(self):
        reply = models.fc.FcImagingExtendedData.from_dict(replies.fc.MOCK_FC_IMAGING_EXTENDED_DATA_REPLY)
        self.fc_measure_assertor(reply, replies.fc.MOCK_FC_IMAGING_EXTENDED_DATA_REPLY['JsonFcMeasureExtendedDataResult'])

    def test_fc_plant_mask_meassure_none(self):
        reply = models.fc.FcPlantMaskMeasure.from_dict({'JsonFcPlantMaskByMeasureIDResult': None})
        self.assertEqual(reply, None)

    def test_fc_plant_mask_meassure(self):
        reply = models.fc.FcPlantMaskMeasure.from_dict(replies.fc.MOCK_FC_PLANT_MASK_MEASURE_REPLY)
        self.fc_mask_assertor(reply, replies.fc.MOCK_FC_PLANT_MASK_MEASURE_REPLY['JsonFcPlantMaskByMeasureIDResult'])

    def test_fc_plant_mask_none(self):
        reply = models.fc.FcPlantMask.from_dict({'JsonFcPlantMaskResult': None})
        self.assertEqual(reply, [])

    def test_fc_plant_mask_empty(self):
        reply = models.fc.FcPlantMask.from_dict({'JsonFcPlantMaskResult': []})
        self.assertEqual(reply, [])

    def test_fc_plant_mask(self):
        reply = models.fc.FcPlantMask.from_dict(replies.fc.MOCK_FC_PLANT_MASK_REPLY)
        self.assertEqual(len(reply), len(replies.fc.MOCK_FC_PLANT_MASK_REPLY['JsonFcPlantMaskResult']))
        for i in range(0, len(replies.fc.MOCK_FC_PLANT_MASK_REPLY['JsonFcPlantMaskResult'])):
            self.fc_mask_assertor(reply[i], replies.fc.MOCK_FC_PLANT_MASK_REPLY['JsonFcPlantMaskResult'][i])

    def test_fc_param_none(self):
        reply = models.fc.FcParamWrapper.from_dict({'JsonFcParamResult': None})
        self.assertEqual(reply, None)

    def test_fc_param(self):
        reply = models.fc.FcParamWrapper.from_dict(replies.fc.MOCK_FC_PARAM_REPLY)
        self.fc_param_assertor(reply, replies.fc.MOCK_FC_PARAM_REPLY['JsonFcParamResult'])

    def test_fc_param_used_analysis_none(self):
        reply = models.fc.FcParamUsedAnalyse.from_dict({'JsonFcUsedParamByAnalyseIDResult': None})
        self.assertEqual(reply, [])

    def test_fc_param_used_analysis_empty(self):
        reply = models.fc.FcParamUsedAnalyse.from_dict({'JsonFcUsedParamByAnalyseIDResult': []})
        self.assertEqual(reply, [])

    def test_fc_param_used_analysis(self):
        reply = models.fc.FcParamUsedAnalyse.from_dict(replies.fc.MOCK_FC_PARAM_USED_ANALYSE_REPLY)
        self.assertEqual(len(reply), len(replies.fc.MOCK_FC_PARAM_USED_ANALYSE_REPLY['JsonFcUsedParamByAnalyseIDResult']))
        for i in range(0, len(replies.fc.MOCK_FC_PARAM_USED_ANALYSE_REPLY['JsonFcUsedParamByAnalyseIDResult'])):
            self.fc_param_assertor(reply[i], replies.fc.MOCK_FC_PARAM_USED_ANALYSE_REPLY['JsonFcUsedParamByAnalyseIDResult'][i])

    def test_fc_param_used_none(self):
        reply = models.fc.FcParamUsed.from_dict({'JsonFcUsedParamResult': None})
        self.assertEqual(reply, [])

    def test_fc_param_used_empty(self):
        reply = models.fc.FcParamUsed.from_dict({'JsonFcUsedParamResult': []})
        self.assertEqual(reply, [])

    def test_fc_param_used(self):
        reply = models.fc.FcParamUsed.from_dict(replies.fc.MOCK_FC_PARAM_USED_REPLY)
        self.assertEqual(len(reply), len(replies.fc.MOCK_FC_PARAM_USED_REPLY['JsonFcUsedParamResult']))
        for i in range(0, len(replies.fc.MOCK_FC_PARAM_USED_REPLY['JsonFcUsedParamResult'])):
            self.fc_param_assertor(reply[i], replies.fc.MOCK_FC_PARAM_USED_REPLY['JsonFcUsedParamResult'][i])

    def test_fc_param_image_analysis_none(self):
        reply = models.fc.FcParamImageAnalyse.from_dict({'JsonFcParameterImageByAnalyseIDResult': None})
        self.assertEqual(reply, None)

    def test_fc_param_image_analysis(self):
        reply = models.fc.FcParamImageAnalyse.from_dict(replies.fc.MOCK_FC_PARAM_IMAGE_ANALYSE_REPLY)
        self.fc_analyse_assertor(reply, replies.fc.MOCK_FC_PARAM_IMAGE_ANALYSE_REPLY['JsonFcParameterImageByAnalyseIDResult'])

    def test_fc_param_image_none(self):
        reply = models.fc.FcParamImage.from_dict({'JsonFcParameterImageResult': None})
        self.assertEqual(reply, [])

    def test_fc_param_image_empty(self):
        reply = models.fc.FcParamImage.from_dict({'JsonFcParameterImageResult': []})
        self.assertEqual(reply, [])

    def test_fc_param_image(self):
        reply = models.fc.FcParamImage.from_dict(replies.fc.MOCK_FC_PARAM_IMAGE_REPLY)
        self.assertEqual(len(reply), len(replies.fc.MOCK_FC_PARAM_IMAGE_REPLY['JsonFcParameterImageResult']))
        for i in range(0, len(replies.fc.MOCK_FC_PARAM_IMAGE_REPLY['JsonFcParameterImageResult'])):
            self.fc_analyse_assertor(reply[i], replies.fc.MOCK_FC_PARAM_IMAGE_REPLY['JsonFcParameterImageResult'][i])

    def test_fc_plant_param_analysis_none(self):
        reply = models.fc.FcPlantParamAnalyse.from_dict({'JsonFcPlantParamByAnalyseIDResult': None})
        self.assertEqual(reply, [])

    def test_fc_plant_param_analysis_empty(self):
        reply = models.fc.FcPlantParamAnalyse.from_dict({'JsonFcPlantParamByAnalyseIDResult': []})
        self.assertEqual(reply, [])

    def test_fc_plant_param_analysis(self):
        reply = models.fc.FcPlantParamAnalyse.from_dict(replies.fc.MOCK_FC_PLANT_PARAM_ANALYSE_REPLY)
        self.assertEqual(len(reply), len(replies.fc.MOCK_FC_PLANT_PARAM_ANALYSE_REPLY['JsonFcPlantParamByAnalyseIDResult']))
        for i in range(0, len(replies.fc.MOCK_FC_PLANT_PARAM_ANALYSE_REPLY['JsonFcPlantParamByAnalyseIDResult'])):
            self.fc_plant_assertor(reply[i], replies.fc.MOCK_FC_PLANT_PARAM_ANALYSE_REPLY['JsonFcPlantParamByAnalyseIDResult'][i])

    def test_fc_plant_param_none(self):
        reply = models.fc.FcPlantParam.from_dict({'JsonFcPlantParamResult': None})
        self.assertEqual(reply, [])

    def test_fc_plant_param_empty(self):
        reply = models.fc.FcPlantParam.from_dict({'JsonFcPlantParamResult': []})
        self.assertEqual(reply, [])

    def test_fc_plant_param(self):
        reply = models.fc.FcPlantParam.from_dict(replies.fc.MOCK_FC_PLANT_PARAM_REPLY)
        self.assertEqual(len(reply), len(replies.fc.MOCK_FC_PLANT_PARAM_REPLY['JsonFcPlantParamResult']))
        for i in range(0, len(replies.fc.MOCK_FC_PLANT_PARAM_REPLY['JsonFcPlantParamResult'])):
            self.fc_plant_assertor(reply[i], replies.fc.MOCK_FC_PLANT_PARAM_REPLY['JsonFcPlantParamResult'][i])

    def test_fc_leaf_param_analysis_none(self):
        reply = models.fc.FcLeafParamAnalyse.from_dict({'JsonFcLeafParamByAnalyseIDResult': None})
        self.assertEqual(reply, [])

    def test_fc_leaf_param_analysis_empty(self):
        reply = models.fc.FcLeafParamAnalyse.from_dict({'JsonFcLeafParamByAnalyseIDResult': []})
        self.assertEqual(reply, [])

    def test_fc_leaf_param_analysis(self):
        reply = models.fc.FcLeafParamAnalyse.from_dict(replies.fc.MOCK_FC_LEAF_PARAM_ANALYSE_REPLY)
        self.assertEqual(len(reply), len(replies.fc.MOCK_FC_LEAF_PARAM_ANALYSE_REPLY['JsonFcLeafParamByAnalyseIDResult']))
        for i in range(0, len(replies.fc.MOCK_FC_LEAF_PARAM_ANALYSE_REPLY['JsonFcLeafParamByAnalyseIDResult'])):
            self.fc_leaf_assertor(reply[i], replies.fc.MOCK_FC_LEAF_PARAM_ANALYSE_REPLY['JsonFcLeafParamByAnalyseIDResult'][i])

    def test_fc_leaf_param_none(self):
        reply = models.fc.FcLeafParam.from_dict({'JsonFcLeafParamResult': None})
        self.assertEqual(reply, [])

    def test_fc_leaf_param_empty(self):
        reply = models.fc.FcLeafParam.from_dict({'JsonFcLeafParamResult': []})
        self.assertEqual(reply, [])

    def test_fc_leaf_param(self):
        reply = models.fc.FcLeafParam.from_dict(replies.fc.MOCK_FC_LEAF_PARAM_REPLY)
        self.assertEqual(len(reply), len(replies.fc.MOCK_FC_LEAF_PARAM_REPLY['JsonFcLeafParamResult']))
        for i in range(0, len(replies.fc.MOCK_FC_LEAF_PARAM_REPLY['JsonFcLeafParamResult'])):
            self.fc_leaf_assertor(reply[i], replies.fc.MOCK_FC_LEAF_PARAM_REPLY['JsonFcLeafParamResult'][i])


if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = FCModels()
    test_case.test_fc_imaging_meassure_none()
    test_case.test_fc_imaging_meassure()
    test_case.test_fc_imaging_none()
    test_case.test_fc_imaging_empty()
    test_case.test_fc_imaging()
    test_case.test_fc_imaging_extended_data_meassure_none()
    test_case.test_fc_imaging_extended_data_meassure()
    test_case.test_fc_imaging_extended_data_none()
    test_case.test_fc_imaging_extended_data()
    test_case.test_fc_plant_mask_meassure_none()
    test_case.test_fc_plant_mask_meassure()
    test_case.test_fc_plant_mask_none()
    test_case.test_fc_plant_mask_empty()
    test_case.test_fc_plant_mask()
    test_case.test_fc_param_none()
    test_case.test_fc_param()
    test_case.test_fc_param_used_analysis_none()
    test_case.test_fc_param_used_analysis_empty()
    test_case.test_fc_param_used_analysis()
    test_case.test_fc_param_image_analysis_none()
    test_case.test_fc_param_image_analysis()
    test_case.test_fc_param_image_none()
    test_case.test_fc_param_image_empty()
    test_case.test_fc_param_image()
    test_case.test_fc_plant_param_analysis_none()
    test_case.test_fc_plant_param_analysis_empty()
    test_case.test_fc_plant_param_analysis()
    test_case.test_fc_plant_param_none()
    test_case.test_fc_plant_param_empty()
    test_case.test_fc_plant_param()
    test_case.test_fc_leaf_param_analysis_none()
    test_case.test_fc_leaf_param_analysis_empty()
    test_case.test_fc_leaf_param_analysis()
    test_case.test_fc_leaf_param_none()
    test_case.test_fc_leaf_param_empty()
    test_case.test_fc_leaf_param()
