"""Test Hyperspectral models"""
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies

class HCModels(unittest.TestCase):
    def hc_imaging_assertor(self, exp_class, exp_dict):
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
        self.assertEqual(exp_class.calibration_dark_content_path, exp_dict['CalibrationDarkContentPath'])
        self.assertEqual(exp_class.calibration_dark_header_path, exp_dict['CalibrationDarkHeaderPath'])
        self.assertEqual(exp_class.calibration_white_content_path, exp_dict['CalibrationWhiteContentPath'])
        self.assertEqual(exp_class.calibration_white_header_path, exp_dict['CalibrationWhiteHeaderPath'])
        self.assertEqual(exp_class.data_content_path, exp_dict['DataContentPath'])
        self.assertEqual(exp_class.data_header_path, exp_dict['DataHeaderPath'])

    def hc_measure_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.device_id, exp_dict['DeviceID'])
        self.assertEqual(exp_class.extended_data, exp_dict['ExtendedData'])
        self.assertEqual(exp_class.measure_date, exp_dict['MeasureDate'])
        self.assertEqual(exp_class.measure_id, exp_dict['MeasureID'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])

    def hc_rgb_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.device_id, exp_dict['DeviceID'])
        self.assertEqual(exp_class.device_pid, exp_dict['DevicePID'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.measure_angle, exp_dict['MeasureAngle'])
        self.assertEqual(exp_class.measure_id, exp_dict['MeasureID'])
        self.assertEqual(exp_class.rgb_image_path, exp_dict['RgbImagePath'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])
        self.assertEqual(exp_class.tray_barcode, exp_dict['TrayBarcode'])
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])

    def hc_mask_assertor(self, exp_class, exp_dict):
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

    def hc_param_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.parameter_id, exp_dict['ParameterID'])
        self.assertEqual(exp_class.parameter_name, exp_dict['ParameterName'])
        self.assertEqual(exp_class.parameter_unit, exp_dict['ParameterUnit'])

    def hc_image_assertor(self, exp_class, exp_dict):
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

    def hc_plant_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.analyse_id, exp_dict['AnalyseID'])
        self.assertEqual(exp_class.device_id, exp_dict['DeviceID'])
        self.assertEqual(exp_class.device_pid, exp_dict['DevicePID'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.measure_angle, exp_dict['MeasureAngle'])
        self.assertEqual(exp_class.measure_id, exp_dict['MeasureID'])
        self.assertEqual(exp_class.parameter_avg, exp_dict['ParameterAvg'])
        self.assertEqual(exp_class.parameter_id, exp_dict['ParameterID'])
        self.assertEqual(exp_class.parameter_max, exp_dict['ParameterMax'])
        self.assertEqual(exp_class.parameter_median, exp_dict['ParameterMedian'])
        self.assertEqual(exp_class.parameter_min, exp_dict['ParameterMin'])
        self.assertEqual(exp_class.parameter_name, exp_dict['ParameterName'])
        self.assertEqual(exp_class.parameter_stddev, exp_dict['ParameterStddev'])
        self.assertEqual(exp_class.plant_barcode, exp_dict['PlantBarcode'])
        self.assertEqual(exp_class.plant_id, exp_dict['PlantID'])
        self.assertEqual(exp_class.plant_name, exp_dict['PlantName'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])
        self.assertEqual(exp_class.tray_area, exp_dict['TrayArea'])
        self.assertEqual(exp_class.tray_barcode, exp_dict['TrayBarcode'])
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])

    def hc_leaf_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.analyse_id, exp_dict['AnalyseID'])
        self.assertEqual(exp_class.device_id, exp_dict['DeviceID'])
        self.assertEqual(exp_class.device_pid, exp_dict['DevicePID'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.leaf_index, exp_dict['LeafIndex'])
        self.assertEqual(exp_class.measure_angle, exp_dict['MeasureAngle'])
        self.assertEqual(exp_class.measure_id, exp_dict['MeasureID'])
        self.assertEqual(exp_class.parameter_avg, exp_dict['ParameterAvg'])
        self.assertEqual(exp_class.parameter_id, exp_dict['ParameterID'])
        self.assertEqual(exp_class.parameter_max, exp_dict['ParameterMax'])
        self.assertEqual(exp_class.parameter_median, exp_dict['ParameterMedian'])
        self.assertEqual(exp_class.parameter_min, exp_dict['ParameterMin'])
        self.assertEqual(exp_class.parameter_name, exp_dict['ParameterName'])
        self.assertEqual(exp_class.parameter_stddev, exp_dict['ParameterStddev'])
        self.assertEqual(exp_class.plant_barcode, exp_dict['PlantBarcode'])
        self.assertEqual(exp_class.plant_id, exp_dict['PlantID'])
        self.assertEqual(exp_class.plant_name, exp_dict['PlantName'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])
        self.assertEqual(exp_class.tray_area, exp_dict['TrayArea'])
        self.assertEqual(exp_class.tray_barcode, exp_dict['TrayBarcode'])
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])

    def test_hc_imaging_meassure_none(self):
        reply = models.hc.HcImagingMeasure.from_dict({'JsonHcImagingByIDResult': None})
        self.assertEqual(reply, None)

    def test_hc_imaging_meassure(self):
        reply = models.hc.HcImagingMeasure.from_dict(replies.hc.MOCK_HC_IMAGING_MEASURE_REPLY)
        self.hc_imaging_assertor(reply, replies.hc.MOCK_HC_IMAGING_MEASURE_REPLY['JsonHcImagingByIDResult'])

    def test_hc_imaging_none(self):
        reply = models.hc.HcImagingWrapper.from_dict({'JsonHcImagingResult': None})
        self.assertEqual(reply, [])

    def test_hc_imaging_empty(self):
        reply = models.hc.HcImagingWrapper.from_dict({'JsonHcImagingResult': []})
        self.assertEqual(reply, [])

    def test_hc_imaging(self):
        reply = models.hc.HcImagingWrapper.from_dict(replies.hc.MOCK_HC_IMAGING_REPLY)
        self.assertEqual(len(reply), len(replies.hc.MOCK_HC_IMAGING_REPLY['JsonHcImagingResult']))
        for i in range(0, len(replies.hc.MOCK_HC_IMAGING_REPLY['JsonHcImagingResult'])):
            self.hc_imaging_assertor(reply[i], replies.hc.MOCK_HC_IMAGING_REPLY['JsonHcImagingResult'][i])

    def test_hc_imaging_extended_data_meassure_none(self):
        reply = models.hc.HcImagingExtendedDataMeasure.from_dict({'JsonHcMeasureExtendedDataByIDResult': None})
        self.assertEqual(reply, None)

    def test_hc_imaging_extended_data_meassure(self):
        reply = models.hc.HcImagingExtendedDataMeasure.from_dict(replies.hc.MOCK_HC_IMAGING_EXTENDED_DATA_MEASURE_REPLY)
        self.hc_measure_assertor(reply, replies.hc.MOCK_HC_IMAGING_EXTENDED_DATA_MEASURE_REPLY['JsonHcMeasureExtendedDataByIDResult'])

    def test_hc_imaging_extended_data_none(self):
        reply = models.hc.HcImagingExtendedData.from_dict({'JsonHcMeasureExtendedDataResult': None})
        self.assertEqual(reply, None)

    def test_hc_imaging_extended_data(self):
        reply = models.hc.HcImagingExtendedData.from_dict(replies.hc.MOCK_HC_IMAGING_EXTENDED_DATA_REPLY)
        self.hc_measure_assertor(reply, replies.hc.MOCK_HC_IMAGING_EXTENDED_DATA_REPLY['JsonHcMeasureExtendedDataResult'])

    def test_hc_rgb_image_meassure_none(self):
        reply = models.hc.HcRgbImageMeasure.from_dict({'JsonHcRgbImageByMeasureIDResult': None})
        self.assertEqual(reply, None)

    def test_hc_rgb_image_meassure(self):
        reply = models.hc.HcRgbImageMeasure.from_dict(replies.hc.MOCK_HC_RGB_IMAGE_MEASURE_REPLY)
        self.hc_rgb_assertor(reply, replies.hc.MOCK_HC_RGB_IMAGE_MEASURE_REPLY['JsonHcRgbImageByMeasureIDResult'])

    def test_hc_image_none(self):
        reply = models.hc.HcRgbImage.from_dict({'JsonHcRgbImageResult': None})
        self.assertEqual(reply, [])

    def test_hc_image_empty(self):
        reply = models.hc.HcRgbImage.from_dict({'JsonHcRgbImageResult': []})
        self.assertEqual(reply, [])

    def test_hc_image(self):
        reply = models.hc.HcRgbImage.from_dict(replies.hc.MOCK_HC_RGB_IMAGE_REPLY)
        self.assertEqual(len(reply), len(replies.hc.MOCK_HC_RGB_IMAGE_REPLY['JsonHcRgbImageResult']))
        for i in range(0, len(replies.hc.MOCK_HC_RGB_IMAGE_REPLY['JsonHcRgbImageResult'])):
            self.hc_rgb_assertor(reply[i], replies.hc.MOCK_HC_RGB_IMAGE_REPLY['JsonHcRgbImageResult'][i])

    def test_hc_plant_mask_meassure_none(self):
        reply = models.hc.HcPlantMaskMeasure.from_dict({'JsonHcPlantMaskByMeasureIDResult': None})
        self.assertEqual(reply, None)

    def test_hc_plant_mask_meassure(self):
        reply = models.hc.HcPlantMaskMeasure.from_dict(replies.hc.MOCK_HC_PLANT_MASK_MEASURE_REPLY)
        self.hc_mask_assertor(reply, replies.hc.MOCK_HC_PLANT_MASK_MEASURE_REPLY['JsonHcPlantMaskByMeasureIDResult'])

    def test_hc_plant_mask_none(self):
        reply = models.hc.HcPlantMask.from_dict({'JsonHcPlantMaskResult': None})
        self.assertEqual(reply, [])

    def test_hc_plant_mask_empty(self):
        reply = models.hc.HcPlantMask.from_dict({'JsonHcPlantMaskResult': []})
        self.assertEqual(reply, [])

    def test_hc_plant_mask(self):
        reply = models.hc.HcPlantMask.from_dict(replies.hc.MOCK_HC_PLANT_MASK_REPLY)
        self.assertEqual(len(reply), len(replies.hc.MOCK_HC_PLANT_MASK_REPLY['JsonHcPlantMaskResult']))
        for i in range(0, len(replies.hc.MOCK_HC_PLANT_MASK_REPLY['JsonHcPlantMaskResult'])):
            self.hc_mask_assertor(reply[i], replies.hc.MOCK_HC_PLANT_MASK_REPLY['JsonHcPlantMaskResult'][i])

    def test_hc_param_none(self):
        reply = models.hc.HcParamWrapper.from_dict({'JsonHcParamResult': None})
        self.assertEqual(reply, None)

    def test_hc_param(self):
        reply = models.hc.HcParamWrapper.from_dict(replies.hc.MOCK_HC_PARAM_REPLY)
        self.hc_param_assertor(reply, replies.hc.MOCK_HC_PARAM_REPLY['JsonHcParamResult'])

    def test_hc_param_used_analyzed_none(self):
        reply = models.hc.HcParamUsedAnalyse.from_dict({'JsonHcUsedParamByAnalyseIDResult': None})
        self.assertEqual(reply, [])

    def test_hc_param_used_analyzed_empty(self):
        reply = models.hc.HcParamUsedAnalyse.from_dict({'JsonHcUsedParamByAnalyseIDResult': []})
        self.assertEqual(reply, [])

    def test_hc_param_used_analyzed(self):
        reply = models.hc.HcParamUsedAnalyse.from_dict(replies.hc.MOCK_HC_PARAM_USED_ANALYSE_REPLY)
        self.assertEqual(len(reply), len(replies.hc.MOCK_HC_PARAM_USED_ANALYSE_REPLY['JsonHcUsedParamByAnalyseIDResult']))
        for i in range(0, len(replies.hc.MOCK_HC_PARAM_USED_ANALYSE_REPLY['JsonHcUsedParamByAnalyseIDResult'])):
            self.hc_param_assertor(reply[i], replies.hc.MOCK_HC_PARAM_USED_ANALYSE_REPLY['JsonHcUsedParamByAnalyseIDResult'][i])

    def test_hc_param_used_none(self):
        reply = models.hc.HcParamUsed.from_dict({'JsonHcUsedParamResult': None})
        self.assertEqual(reply, [])

    def test_hc_param_used_empty(self):
        reply = models.hc.HcParamUsed.from_dict({'JsonHcUsedParamResult': []})
        self.assertEqual(reply, [])

    def test_hc_param_used(self):
        reply = models.hc.HcParamUsed.from_dict(replies.hc.MOCK_HC_PARAM_USED_REPLY)
        self.assertEqual(len(reply), len(replies.hc.MOCK_HC_PARAM_USED_REPLY['JsonHcUsedParamResult']))
        for i in range(0, len(replies.hc.MOCK_HC_PARAM_USED_REPLY['JsonHcUsedParamResult'])):
            self.hc_param_assertor(reply[i], replies.hc.MOCK_HC_PARAM_USED_REPLY['JsonHcUsedParamResult'][i])

    def test_hc_param_image_analysis_none(self):
        reply = models.hc.HcParamImageAnalyse.from_dict({'JsonHcParameterImageByAnalyseIDResult': None})
        self.assertEqual(reply, None)

    def test_hc_param_image_analysis(self):
        reply = models.hc.HcParamImageAnalyse.from_dict(replies.hc.MOCK_HC_PARAM_IMAGE_ANALYSE_REPLY)
        self.hc_image_assertor(reply, replies.hc.MOCK_HC_PARAM_IMAGE_ANALYSE_REPLY['JsonHcParameterImageByAnalyseIDResult'])

    def test_hc_param_image_none(self):
        reply = models.hc.HcParamImage.from_dict({'JsonHcParameterImageResult': None})
        self.assertEqual(reply, [])

    def test_hc_param_image_empty(self):
        reply = models.hc.HcParamImage.from_dict({'JsonHcParameterImageResult': []})
        self.assertEqual(reply, [])

    def test_hc_param_image(self):
        reply = models.hc.HcParamImage.from_dict(replies.hc.MOCK_HC_PARAM_IMAGE_REPLY)
        self.assertEqual(len(reply), len(replies.hc.MOCK_HC_PARAM_IMAGE_REPLY['JsonHcParameterImageResult']))
        for i in range(0, len(replies.hc.MOCK_HC_PARAM_IMAGE_REPLY['JsonHcParameterImageResult'])):
            self.hc_image_assertor(reply[i], replies.hc.MOCK_HC_PARAM_IMAGE_REPLY['JsonHcParameterImageResult'][i])

    def test_hc_plant_param_analysis_none(self):
        reply = models.hc.HcPlantParamAnalyse.from_dict({'JsonHcPlantParamByAnalyseIDResult': None})
        self.assertEqual(reply, [])

    def test_hc_plant_param_analysis_empty(self):
        reply = models.hc.HcPlantParamAnalyse.from_dict({'JsonHcPlantParamByAnalyseIDResult': []})
        self.assertEqual(reply, [])

    def test_hc_plant_param_analysis(self):
        reply = models.hc.HcPlantParamAnalyse.from_dict(replies.hc.MOCK_HC_PLANT_PARAM_ANALYSE_REPLY)
        self.assertEqual(len(reply), len(replies.hc.MOCK_HC_PLANT_PARAM_ANALYSE_REPLY['JsonHcPlantParamByAnalyseIDResult']))
        for i in range(0, len(replies.hc.MOCK_HC_PLANT_PARAM_ANALYSE_REPLY['JsonHcPlantParamByAnalyseIDResult'])):
            self.hc_plant_assertor(reply[i], replies.hc.MOCK_HC_PLANT_PARAM_ANALYSE_REPLY['JsonHcPlantParamByAnalyseIDResult'][i])

    def test_hc_plant_param_none(self):
        reply = models.hc.HcPlantParam.from_dict({'JsonHcPlantParamResult': None})
        self.assertEqual(reply, [])

    def test_hc_plant_param_empty(self):
        reply = models.hc.HcPlantParam.from_dict({'JsonHcPlantParamResult': []})
        self.assertEqual(reply, [])

    def test_hc_plant_param(self):
        reply = models.hc.HcPlantParam.from_dict(replies.hc.MOCK_HC_PLANT_PARAM_REPLY)
        self.assertEqual(len(reply), len(replies.hc.MOCK_HC_PLANT_PARAM_REPLY['JsonHcPlantParamResult']))
        for i in range(0, len(replies.hc.MOCK_HC_PLANT_PARAM_REPLY['JsonHcPlantParamResult'])):
            self.hc_plant_assertor(reply[i], replies.hc.MOCK_HC_PLANT_PARAM_REPLY['JsonHcPlantParamResult'][i])

    def test_hc_leaf_param_analysis_none(self):
        reply = models.hc.HcLeafParamAnalyse.from_dict({'JsonHcLeafParamByAnalyseIDResult': None})
        self.assertEqual(reply, [])

    def test_hc_leaf_param_analysis_empty(self):
        reply = models.hc.HcLeafParamAnalyse.from_dict({'JsonHcLeafParamByAnalyseIDResult': []})
        self.assertEqual(reply, [])

    def test_hc_leaf_param_analysis(self):
        reply = models.hc.HcLeafParamAnalyse.from_dict(replies.hc.MOCK_HC_LEAF_PARAM_ANALYSE_REPLY)
        self.assertEqual(len(reply), len(replies.hc.MOCK_HC_LEAF_PARAM_ANALYSE_REPLY['JsonHcLeafParamByAnalyseIDResult']))
        for i in range(0, len(replies.hc.MOCK_HC_LEAF_PARAM_ANALYSE_REPLY['JsonHcLeafParamByAnalyseIDResult'])):
            self.hc_leaf_assertor(reply[i], replies.hc.MOCK_HC_LEAF_PARAM_ANALYSE_REPLY['JsonHcLeafParamByAnalyseIDResult'][i])

    def test_hc_leaf_param_none(self):
        reply = models.hc.HcLeafParam.from_dict({'JsonHcLeafParamsResult': None})
        self.assertEqual(reply, [])

    def test_hc_leaf_param_empty(self):
        reply = models.hc.HcLeafParam.from_dict({'JsonHcLeafParamsResult': []})
        self.assertEqual(reply, [])

    def test_hc_leaf_param(self):
        reply = models.hc.HcLeafParam.from_dict(replies.hc.MOCK_HC_LEAF_PARAM_REPLY)
        self.assertEqual(len(reply), len(replies.hc.MOCK_HC_LEAF_PARAM_REPLY['JsonHcLeafParamsResult']))
        for i in range(0, len(replies.hc.MOCK_HC_LEAF_PARAM_REPLY['JsonHcLeafParamsResult'])):
            self.hc_leaf_assertor(reply[i], replies.hc.MOCK_HC_LEAF_PARAM_REPLY['JsonHcLeafParamsResult'][i])


if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = HCModels()
    test_case.test_hc_imaging_meassure_none()
    test_case.test_hc_imaging_meassure()
    test_case.test_hc_imaging_none()
    test_case.test_hc_imaging_empty()
    test_case.test_hc_imaging()
    test_case.test_hc_imaging_extended_data_meassure_none()
    test_case.test_hc_imaging_extended_data_meassure()
    test_case.test_hc_imaging_extended_data_none()
    test_case.test_hc_imaging_extended_data()
    test_case.test_hc_rgb_image_meassure_none()
    test_case.test_hc_rgb_image_meassure()
    test_case.test_hc_image_none()
    test_case.test_hc_image_empty()
    test_case.test_hc_image()
    test_case.test_hc_plant_mask_meassure_none()
    test_case.test_hc_plant_mask_meassure()
    test_case.test_hc_plant_mask_none()
    test_case.test_hc_plant_mask_empty()
    test_case.test_hc_plant_mask()
    test_case.test_hc_param_none()
    test_case.test_hc_param()
    test_case.test_hc_param_used_analyzed_none()
    test_case.test_hc_param_used_analyzed_empty()
    test_case.test_hc_param_used_analyzed()
    test_case.test_hc_param_used_none()
    test_case.test_hc_param_used_empty()
    test_case.test_hc_param_used()
    test_case.test_hc_param_image_analysis_none()
    test_case.test_hc_param_image_analysis()
    test_case.test_hc_param_image_none()
    test_case.test_hc_param_image_empty()
    test_case.test_hc_param_image()
    test_case.test_hc_plant_param_analysis_none()
    test_case.test_hc_plant_param_analysis_empty()
    test_case.test_hc_plant_param_analysis()
    test_case.test_hc_plant_param_none()
    test_case.test_hc_plant_param_empty()
    test_case.test_hc_plant_param()
    test_case.test_hc_leaf_param_analysis_none()
    test_case.test_hc_leaf_param_analysis_empty()
    test_case.test_hc_leaf_param_analysis()
    test_case.test_hc_leaf_param_none()
    test_case.test_hc_leaf_param_empty()
    test_case.test_hc_leaf_param()