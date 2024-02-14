import plantscreen.swagger_client as swagger_client
import plantscreen.models as models
from typing import List


class Imaging_API():
    """ Wrapper around the automatically  generated swagger client.
       \n return class instances instead of dictionaries """
    def __init__(self, server, poort):
        configuration = swagger_client.Configuration()
        configuration.host = f'{server}:{poort}/RestService/json'
        self.fc_api = swagger_client.FcApi(swagger_client.ApiClient(configuration))
        self.hc_api = swagger_client.HcApi(swagger_client.ApiClient(configuration))
        self.ir_api = swagger_client.IrApi(swagger_client.ApiClient(configuration))        
        self.msc_api = swagger_client.MscApi(swagger_client.ApiClient(configuration))
        self.rgb_api = swagger_client.RgbApi(swagger_client.ApiClient(configuration))
        self.scan3d_api = swagger_client.Scan3dApi(swagger_client.ApiClient(configuration))

# Fc API
    def fc_imaging_measure(self, meas_id: int) -> swagger_client.FcImaging:
        """ Returns FluorCam imaging data by FC measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.FcImaging """
        api_response = self.fc_api.fc_imaging_measure(meas_id)
        return api_response.JsonFcImagingByIDResult

    def fc_imaging(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.FcImaging:
        """ Returns FluorCam imaging data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.FcImaging """
        api_response = self.fc_api.fc_imaging(device_id, round_id, tray_id)
        if api_response.JsonFcImagingResult is None:
            return []
        else:
            return api_response.JsonFcImagingResult

    def fc_imaging_extended_data_measure(self, meas_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns FluorCam imaging extended data by FC measure ID. (Only available for field systems

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.fc_api.fc_imaging_extended_data_measure(meas_id)
        return api_response.JsonFcMeasureExtendedDataByIDResult

    def fc_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns FluorCam extended data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID.

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.fc_api.fc_imaging_extended_data(device_id, round_id, tray_id)
        return api_response.JsonFcMeasureExtendedDataResult

    def fc_plant_mask_measure(self, meas_id: int) -> swagger_client.PlantMask:
        """ Returns the FluorCam plant mask created for the measured tray defined by FC measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.PlantMask """
        api_response = self.fc_api.fc_plant_mask_measure(meas_id)
        return api_response.JsonFcPlantMaskByMeasureIDResult

    def fc_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.PlantMask:
        """ Returns FluorCam plant masks created for the tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.PlantMask """
        api_response = self.fc_api.fc_plant_mask(device_id, round_id, tray_id)
        if api_response.JsonFcPlantMaskResult is None:
            return []
        else:
            return api_response.JsonFcPlantMaskResult

    def fc_param(self, param_id: int) -> swagger_client.Parameter:
        """ Returns one FluorCam parameter by parameter ID

        Args:
            param_id (int): Parameter ID

        Return:
            swagger_client.Parameter """
        api_response = self.fc_api.fc_param(param_id)
        return api_response.JsonFcParamResult

    def fc_param_used_analyse(self, analisys_id: int) -> swagger_client.Parameter:
        """ Returns the FluorCam plant and leaf parameters used in the analysis defined by analyse ID

        Args:
            analisys_id (int): Analysis ID

        Return:
            swagger_client.Parameter """
        api_response = self.fc_api.fc_param_used_analyse(analisys_id)
        if api_response.JsonFcUsedParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonFcUsedParamByAnalyseIDResult

    def fc_param_used(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.Parameter:
        """ Returns the FluorCam plant and leaf parameters used in the analysis by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.Parameter """
        api_response = self.fc_api.fc_param_used(device_id, round_id, tray_id)
        if api_response.JsonFcUsedParamResult is None:
            return []
        else:
            return api_response.JsonFcUsedParamResult

    def fc_param_image_analyse(self, analisys_id: int, param_id: int) -> swagger_client.ParameterImage:
        """ Returns the FluorCam parameter image for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            analisys_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            swagger_client.ParameterImage """
        api_response = self.fc_api.fc_param_image_analyse(analisys_id, param_id)
        return api_response.JsonFcParameterImageByAnalyseIDResult

    def fc_param_image(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> swagger_client.ParameterImage:
        """ Returns the FluorCam parameter images for the parameter defined by parameter ID, by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            swagger_client.ParameterImage """
        api_response = self.fc_api.fc_param_image(device_id, round_id, tray_id, param_id)
        if api_response.JsonFcParameterImageResult is None:
            return []
        else:
            return api_response.JsonFcParameterImageResult

    def fc_plant_param_analyse(self, analisys_id: int, param_id: int) -> swagger_client.PlantParameter:
        """ Returns the FluorCam plant parameter values for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            analisys_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            swagger_client.PlantParameter """
        api_response = self.fc_api.fc_plant_param_analyse(analisys_id, param_id)
        if api_response.JsonFcPlantParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonFcPlantParamByAnalyseIDResult

    def fc_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> swagger_client.PlantParameter:
        """ Returns the FluorCam plant parameter values for the parameter defined by parameter ID, by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            swagger_client.PlantParameter """
        api_response = self.fc_api.fc_plant_param(device_id, round_id, tray_id, param_id)
        if api_response.JsonFcPlantParamResult is None:
            return []
        else:
            return api_response.JsonFcPlantParamResult

    def fc_leaf_param_analyse(self, analisys_id: int, param_id: int) -> swagger_client.LeafParameter:
        """ Returns the FluorCam leaf parameter values for the parameter defined by parameter ID and
        calculated in the analysis defined by analyse ID

        Args:
            analisys_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            swagger_client.PlantParameter """
        api_response = self.fc_api.fc_leaf_param_analyse(analisys_id, param_id)
        if api_response.JsonFcLeafParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonFcLeafParamByAnalyseIDResult

    def fc_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> swagger_client.LeafParameter:
        """ Returns the FluorCam leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID
        of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            swagger_client.PlantParameter """
        api_response = self.fc_api.fc_leaf_param(device_id, round_id, tray_id, param_id)
        if api_response.JsonFcLeafParamResult is None:
            return []
        else:
            return api_response.JsonFcLeafParamResult

# Hc API
    def hc_imaging_measure(self, meas_id: int) -> swagger_client.HcImaging:
        """ Returns Hyperspectral imaging data by HC measure ID

        Args:
            meas_id (int): Measure ID

        Return:
            swagger_client.HcImaging """
        api_response = self.hc_api.hc_imaging_measure(meas_id)
        return api_response.JsonHcImagingByIDResult

    def hc_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.HcImaging]:
        """ Returns Hyperspectral imaging data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.HcImaging] """
        api_response = self.hc_api.hc_imaging(device_id, round_id, tray_id)
        if api_response.JsonHcImagingResult is None:
            return []
        else:
            return api_response.JsonHcImagingResult

    def hc_imaging_extended_data_measure(self, meas_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns Hyperspectral imaging extended data by HC measure ID

        Args:
            meas_id (int): Measure ID

        Return:
            swagger_client.HcImaging """
        api_response = self.hc_api.hc_imaging_extended_data_measure(meas_id)
        return api_response.JsonHcMeasureExtendedDataByIDResult

    def hc_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.MeasureExtendedData]:
        """ Returns Hyperspectral imaging extended data by HC measure ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.MeasureExtendedData] """
        api_response = self.hc_api.hc_imaging_extended_data(device_id, round_id, tray_id)
        if api_response.JsonHcMeasureExtendedDataResult is None:
            return []
        else:
            return api_response.JsonHcMeasureExtendedDataResult

    def hc_rgb_image_measure(self, meas_id: int) -> swagger_client.HcRgbImage:
        """ Returns Hyperspectral imaging extended data by HC measure ID

        Args:
            meas_id (int): Measure ID

        Return:
            swagger_client.HcRgbImage """
        api_response = self.hc_api.hc_rgb_image_measure(meas_id)
        return api_response.JsonHcRgbImageByMeasureIDResult

    def hc_rgb_image(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.HcRgbImage]:
        """ Returns Hyperspectral imaging extended data by HC measure ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.HcRgbImage] """
        api_response = self.hc_api.hc_rgb_image(device_id, round_id, tray_id)
        if api_response.JsonHcRgbImageResult is None:
            return []
        else:
            return api_response.JsonHcRgbImageResult

    def hc_plant_mask_measure(self, meas_id: int) -> swagger_client.PlantMask:
        """ Returns the Hyperspectral plant mask created for the measured tray defined by HC measure ID

        Args:
            meas_id (int): Measure ID

        Return:
            swagger_client.PlantMask """
        api_response = self.hc_api.hc_plant_mask_measure(meas_id)
        return api_response.JsonHcPlantMaskByMeasureIDResult

    def hc_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.PlantMask]:
        """ Returns Hyperspectral plant masks created for the tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.PlantMask] """
        api_response = self.hc_api.hc_plant_mask(device_id, round_id, tray_id)
        if api_response.JsonHcPlantMaskResult is None:
            return []
        else:
            return api_response.JsonHcPlantMaskResult

    def hc_param(self, param_id: int) -> swagger_client.Parameter:
        """ Returns one Hyperspectral parameter by parameter ID

        Args:
            param_id (int): Parameter ID

        Return:
            swagger_client.Parameter """
        api_response = self.hc_api.hc_param(param_id)
        return api_response.JsonHcParamResult

    def hc_param_used_analyse(self, analysis_id: int) -> List[swagger_client.Parameter]:
        """ Returns the Hyperspectral plant and leaf parameters used in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID

        Return:
            list[swagger_client.Parameter] """
        api_response = self.hc_api.hc_param_used_analyse(analysis_id)
        if api_response.JsonHcUsedParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonHcUsedParamByAnalyseIDResult

    def hc_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Parameter]:
        """ Returns the Hyperspectral plant and leaf parameters used in the analysis by tray ID, by round ID
        of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            list[swagger_client.Parameter] """
        api_response = self.hc_api.hc_param_used(device_id, round_id, tray_id)
        if api_response.JsonHcUsedParamResult is None:
            return []
        else:
            return api_response.JsonHcUsedParamResult

    def hc_param_image_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.ParameterImage]:
        """ Returns the Hyperspectral parameter image for the parameter defined by parameter ID and calculated 
        in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            list[swagger_client.ParameterImage] """
        api_response = self.hc_api.hc_param_image_analyse(analysis_id, param_id)
        if api_response.JsonHcParameterImageByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonHcParameterImageByAnalyseIDResult

    def hc_param_image(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.ParameterImage]:
        """ Returns the Hyperspectral parameter images for the parameter defined by parameter ID, by tray ID, by round ID of round
        in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            list[swagger_client.ParameterImage] """
        api_response = self.hc_api.hc_param_image(device_id, round_id, tray_id, param_id)
        if api_response.JsonHcParameterImageResult is None:
            return []
        else:
            return api_response.JsonHcParameterImageResult

    def hc_plant_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.StatisticPlantParameter]:
        """ Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            list[swagger_client.StatisticPlantParameter] """
        api_response = self.hc_api.hc_plant_param_analyse(analysis_id, param_id)
        if api_response.JsonHcPlantParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonHcPlantParamByAnalyseIDResult

    def hc_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.StatisticPlantParameter]:
        """ Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID, by tray ID, by round ID 
        of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            list[swagger_client.StatisticPlantParameter] """
        api_response = self.hc_api.hc_plant_param(device_id, round_id, tray_id, param_id)
        if api_response.JsonHcPlantParamResult is None:
            return []
        else:
            return api_response.JsonHcPlantParamResult

    def hc_leaf_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.StatisticLeafParameter]:
        """ Returns the Hyperspectral statistic leaf parameter values for the parameter defined by parameter ID and
        calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            list[swagger_client.StatisticLeafParameter] """
        api_response = self.hc_api.hc_leaf_param_analyse(analysis_id, param_id)
        if api_response.JsonHcLeafParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonHcLeafParamByAnalyseIDResult

    def hc_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.StatisticLeafParameter]:
        """ Returns the Hyperspectral Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID
        of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            list[swagger_client.StatisticLeafParameter] """
        api_response = self.hc_api.hc_leaf_param(device_id, round_id, tray_id, param_id)
        if api_response.JsonHcLeafParamResult is None:
            return []
        else:
            return api_response.JsonHcLeafParamResult

# Ir API
    def ir_imaging_measure(self, meas_id: int) -> swagger_client.Imaging:
        """ Returns Thermal imaging data by IR measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.Imaging """
        api_response = self.ir_api.ir_imaging_measure(meas_id)
        api_response.JsonIrImagingByIDResult

    def ir_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Imaging]:
        """ Returns Thermal imaging data for tray defined by tray ID, by round ID of round in which the
        tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Imaging] """
        api_response = self.ir_api.ir_imaging(device_id, round_id, tray_id)
        if api_response.JsonIrImagingResult is None:
            return []
        else:
            return api_response.JsonIrImagingResult

    def ir_imaging_extended_data_measure(self, meas_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns Thermal imaging data by IR measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.ir_api.ir_imaging_extended_data_measure(meas_id)
        return api_response.JsonIrMeasureExtendedDataByIDResult

    def ir_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns Thermal extended data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.ir_api.ir_imaging_extended_data(device_id, round_id, tray_id)
        return api_response.JsonIrMeasureExtendedDataResult

    def ir_plant_mask_measure(self, meas_id: int) -> swagger_client.PlantMask:
        """ Returns the Thermal plant mask created for the measured tray defined by IR measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.PlantMask """
        api_response = self.ir_api.ir_plant_mask_measure(meas_id)
        return api_response.JsonIrPlantMaskByMeasureIDResult

    def ir_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.PlantMask]:
        """ Returns Thermal plant masks created for the tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.PlantMask] """
        api_response = self.ir_api.ir_plant_mask(device_id, round_id, tray_id)
        if api_response.JsonIrPlantMaskResult is None:
            return []
        else:
            return api_response.JsonIrPlantMaskResult

    def ir_plant_mask_image_measure(self, meas_id: int) -> swagger_client.Imaging:
        """ Returns Thermal imaging data masked by the plant mask defined by IR measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.Imaging """
        api_response = self.ir_api.ir_plant_mask_image_measure(meas_id)
        return api_response.JsonIrPlantMaskImageByMeasureIDResult

    def ir_plant_mask_image(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Imaging]:
        """ Returns Thermal imaging data masked by the plant mask for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Imaging] """
        api_response = self.ir_api.ir_plant_mask_image(device_id, round_id, tray_id)
        if api_response.JsonIrPlantMaskImageResult is None:
            return []
        else:
            return api_response.JsonIrPlantMaskImageResult

    def ir_param(self, param_id: int) -> swagger_client.Parameter:
        """ Returns one Thermal parameter by parameter ID

        Args:
            param_id (int): Parameter ID

        Return:
            swagger_client.Parameter """
        api_response = self.ir_api.ir_param(param_id)
        return api_response.JsonIrParamResult

    def ir_param_used_analyse(self, analysis_id: int) -> List[swagger_client.Parameter]:
        """ Returns the Thermalplant and leaf parameters used in the analysis defined by analyse ID

        Args:
            analysis_id (int): analysis ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.ir_api.ir_param_used_analyse(analysis_id)
        if api_response.JsonIrUsedParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonIrUsedParamByAnalyseIDResult

    def ir_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Parameter]:
        """ Returns the Thermal plant and leaf parameters used in the analysis by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.ir_api.ir_param_used(device_id, round_id, tray_id)
        if api_response.JsonIrUsedParamResult is None:
            return []
        else:
            return api_response.JsonIrUsedParamResult

    def ir_plant_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.StatisticPlantParameter]:
        """ Returns the Thermal plant parameter values for the parameter defined by parameter ID and
        calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.StatisticPlantParameter] """
        api_response = self.ir_api.ir_plant_param_analyse(analysis_id, param_id)
        if api_response.JsonIrPlantParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonIrPlantParamByAnalyseIDResult

    def ir_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.StatisticPlantParameter]:
        """ Returns the Thermal statistic plant parameter values for the parameter defined by parameter ID, by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.StatisticPlantParameter] """
        api_response = self.ir_api.ir_plant_param(device_id, round_id, tray_id, param_id)
        if api_response.JsonIrPlantParamResult is None:
            return []
        else:
            return api_response.JsonIrPlantParamResult

    def ir_leaf_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.StatisticLeafParameter]:
        """ Returns the Thermal statistic leaf parameter values for the parameter defined by 
        parameter ID and calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.StatisticLeafParameter] """
        api_response = self.ir_api.ir_leaf_param_analyse(analysis_id, param_id)
        if api_response.JsonIrLeafParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonIrLeafParamByAnalyseIDResult

    def ir_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.StatisticPlantParameter]:
        """ Returns the Thermal Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.StatisticPlantParameter] """
        api_response = self.ir_api.ir_leaf_param(device_id, round_id, tray_id, param_id)
        if api_response.JsonIrLeafParamResult is None:
            return []
        else:
            return api_response.JsonIrLeafParamResult

# Msc API
    def msc_imaging_measure(self, meas_id: int) -> swagger_client.Imaging:
        """ Returns Multispectral imaging data by MSC measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.Imaging """
        api_response = self.msc_api.msc_imaging_measure(meas_id)
        if api_response.JsonMscImagingByIDResult is None:
            return []
        else:
            return api_response.JsonMscImagingByIDResult

    def msc_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Imaging]:
        """ Returns Multispectral imaging data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Imaging] """
        api_response = self.msc_api.msc_imaging(device_id, round_id, tray_id)
        if api_response.JsonMscImagingResult is None:
            return []
        else:
            return api_response.JsonMscImagingResult

    def msc_imaging_extended_data_measure(self, meas_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns Multispectral imaging extended data by MSC measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.msc_api.msc_imaging_extended_data_measure(meas_id)
        return api_response.JsonMscMeasureExtendedDataByIDResult

    def msc_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns Multispectral extended data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.msc_api.msc_imaging_extended_data(device_id, round_id, tray_id)
        return api_response.JsonMscMeasureExtendedDataResult

    def msc_plant_mask_measure(self, meas_id: int) -> swagger_client.PlantMask:
        """ Returns Multispectral extended data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.PlantMask """
        api_response = self.msc_api.msc_plant_mask_measure(meas_id)
        return api_response.JsonMscPlantMaskByMeasureIDResult

    def msc_plant_mask_meamsc_plant_masksure(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.PlantMask]:
        """ Returns Multispectral plant mask by device, round and tray ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.PlantMask """
        api_response = self.msc_api.msc_plant_mask(device_id, round_id, tray_id)
        if api_response.JsonMscPlantMaskResult is None:
            return []
        else:
            return api_response.JsonMscPlantMaskResult

    def msc_param(self, param_id: int) -> swagger_client.Parameter:
        """ Returns one Multispectral parameter by parameter ID

        Args:
            param_id (int): Parameter ID

        Return:
            swagger_client.Parameter """
        api_response = self.msc_api.msc_param(param_id)
        return api_response.JsonMscParamResult

    def msc_param_used_analyse(self, analysis_id: int) -> List[swagger_client.Parameter]:
        """ Returns Multispectral used plant parameters by analyse ID

        Args:
            analysis_id (int): Analysis ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.msc_api.msc_param_used_analyse(analysis_id)
        if api_response.JsonMscUsedParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonMscUsedParamByAnalyseIDResult

    def msc_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Parameter]:
        """ Returns the Multispectral plant and leaf parameters used in the analysis by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.msc_api.msc_param_used(device_id, round_id, tray_id)
        if api_response.JsonMscUsedParamResult is None:
            return []
        else:
            return api_response.JsonMscUsedParamResult

    def msc_param_image_analyse(self, analysis_id: int, param_id: int) -> swagger_client.ParameterImage:
        """ Returns the Multispectral parameter image for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            swagger_client.ParameterImage """
        api_response = self.msc_api.msc_param_image_analyse(analysis_id, param_id)
        return api_response.JsonMscParameterImageByAnalyseIDResult

    def msc_param_image(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.ParameterImage]:
        """ Returns the Multispectral parameter images for the parameter defined by parameter ID, by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.ParameterImage] """
        api_response = self.msc_api.msc_param_image(device_id, round_id, tray_id, param_id)
        if api_response.JsonMscParameterImageResult is None:
            return []
        else:
            return api_response.JsonMscParameterImageResult

    def msc_plant_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.StatisticPlantParameter]:
        """ Returns the Multispectral parameter image for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.StatisticPlantParameter] """
        api_response = self.msc_api.msc_plant_param_analyse(analysis_id, param_id)
        if api_response.JsonMscPlantParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonMscPlantParamByAnalyseIDResult

    def msc_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.StatisticPlantParameter]:
        """ Returns the Multispectral parameter image for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.StatisticPlantParameter] """
        api_response = self.msc_api.msc_plant_param(device_id, round_id, tray_id, param_id)
        if api_response.JsonMscPlantParamResult is None:
            return []
        else:
            return api_response.JsonMscPlantParamResult

    def msc_leaf_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.StatisticLeafParameter]:
        """ Returns the Multispectral statistic leaf parameter values for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.StatisticLeafParameter] """
        api_response = self.msc_api.msc_leaf_param_analyse(analysis_id, param_id)
        if api_response.JsonMscLeafParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonMscLeafParamByAnalyseIDResult

    def msc_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.StatisticLeafParameter]:
        """ Returns the Multispectral Statistic leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID
        of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.StatisticLeafParameter] """
        api_response = self.msc_api.msc_leaf_param(device_id, round_id, tray_id, param_id)
        if api_response.JsonMscLeafParamResult is None:
            return []
        else:
            return api_response.JsonMscLeafParamResult

    def msc_light_set(self, lightset_id: int) -> swagger_client.MscLightSet:
        """ Returns one set of the lights for multispectral camera service defined by light set ID

        Args:
            lightset_id (int): Lightset ID

        Return:
            swagger_client.MscLightSet """
        api_response = self.msc_api.msc_light_set(lightset_id)
        api_response.JsonMscLightSetResult

    def msc_light_set_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.MscLightSet]:
        """ Returns the sets of the lights for multispectral camera service used in the measure for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.MscLightSet] """
        api_response = self.msc_api.msc_light_set_used(device_id, round_id, tray_id)
        if api_response.JsonMscLightSetUsedResult is None:
            return []
        else:
            return api_response.JsonMscLightSetUsedResult

    def msc_calibration(self, calib_id: int) -> swagger_client.MscCalibration:
        """ Returns one Multispectral calibration for individual groups of lights
        with information about the exposure and gain of the camera defined by calibration ID

        Args:
            calib_id (int): Calibration ID

        Return:
            swagger_client.MscCalibration """
        api_response = self.msc_api.msc_calibration(id)
        return api_response.JsonMscCalibrationResult

    def msc_calibration_light_set(self, lightset_id: int) -> swagger_client.MscCalibration:
        """ Returns the Multispectral calibration for individual groups of lights with
        information about the exposure and gain of the camera defined by light set ID

        Args:
            lightset_id (int): Lightset ID

        Return:
            swagger_client.MscCalibration """
        api_response = self.msc_api.msc_calibration_light_set(id)
        return api_response.JsonMscCalibrationByLightSetIDResult

    def msc_calibration_light(self) -> swagger_client.MscCalibrationLight:
        """ Returns a list of all lightsettings if no ID is passed.
        Or the light output setting for light group calibration defined by calibration light ID

        Args:
            -

        Return:
            swagger_client.MscCalibrationLight """
        api_response = self.msc_api.msc_calibration_light()
        return api_response.JsonMscCalibrationLightByIDResult

# RGB API
    def rgb_imaging_measure(self, meas_id: int) -> swagger_client.Imaging:
        """ Returns RGB imaging data by RGB measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.Imaging """
        api_response = self.rgb_api.rgb_imaging_measure(meas_id)
        return api_response.JsonRgbImagingByIDResult

    def rgb_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Imaging]:
        """ Returns FluorCam imaging data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.Imaging """
        api_response = self.rgb_api.rgb_imaging(device_id, round_id, tray_id)
        if api_response.JsonRgbImagingResult is None:
            return []
        else:
            return api_response.JsonRgbImagingResult

    def rgb_imaging_extended_data_measure(self, meas_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns RGB imaging extended data by RGB measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.rgb_api.rgb_imaging_extended_data_measure(meas_id)
        return api_response.JsonRgbMeasureExtendedDataByIDResult

    def rgb_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns RGB extended data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.rgb_api.rgb_imaging_extended_data(device_id, round_id, tray_id)
        return api_response.JsonRgbMeasureExtendedDataResult

    def rgb_plant_mask_measure(self, meas_id) -> swagger_client.PlantMask:
        """ Returns the RGB plant mask created for the measured tray defined by RGB measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.rgb_api.rgb_plant_mask_measure(meas_id)
        return api_response.JsonRgbPlantMaskByMeasureIDResult

    def rgb_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.PlantMask]:
        """ Returns RGB plant masks created for the tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.PlantMask] """
        api_response = self.rgb_api.rgb_plant_mask(device_id, round_id, tray_id)
        if api_response.JsonRgbPlantMaskResult is None:
            return []
        else:
            return api_response.JsonRgbPlantMaskResult

    def rgb_greening_mask_image_measure(self, meas_id: int) -> swagger_client.RgbGreeningMaskImage:
        """ Returns RGB greening data masked by the plant mask defined by RGB measure ID.
        The greening mask image is created by greening analysis,
        therefore it is only available if greening analysis has been performed on the required data

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.RgbGreeningMaskImage """
        api_response = self.rgb_api.rgb_greening_mask_image_measure(meas_id)
        return api_response.JsonRgbGreeningMaskImageByMeasureIDResult

    def rgb_greening_mask_image(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.RgbGreeningMaskImage]:
        """ Returns RGB greening data data masked by the plant mask for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID.
        The greening mask image is created by greening analysis,
        therefore it is only available if greening analysis has been performed on the required data.

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.RgbGreeningMaskImage] """
        api_response = self.rgb_api.rgb_greening_mask_image(device_id, round_id, tray_id)
        if api_response.JsonRgbGreeningMaskImageResult is None:
            return []
        else:
            return api_response.JsonRgbGreeningMaskImageResult

    def rgb_param(self, param_id: int) -> swagger_client.Parameter:
        """ Returns one RGB morfo parameter by parameter ID

        Args:
            param_id (int): Measurement ID

        Return:
            swagger_client.RgbGreeningMaskImage """
        api_response = self.rgb_api.rgb_param(param_id)
        return api_response.JsonRgbParamResult

    def rgb_param_used_analyse(self, analysis_id: int) -> List[swagger_client.Parameter]:
        """ Returns the RGB plant and leaf parameters used in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.rgb_api.rgb_param_used_analyse(analysis_id)
        if api_response.JsonRgbUsedParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonRgbUsedParamByAnalyseIDResult

    def rgb_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Parameter]:
        """ Returns the RGB plant and leaf parameters used in the analysis defined by analyse ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.rgb_api.rgb_param_used(device_id, round_id, tray_id)
        if api_response.JsonRgbUsedParamsResult is None:
            return []
        else:
            return api_response.JsonRgbUsedParamsResult

    def rgb_param_color_used_analyse(self, analysis_id: int) -> List[swagger_client.Parameter]:
        """ Returns the greening RGB plant and leaf parameters used in the greening analysis
        defined by analyse ID (for greening analysis)

        Args:
            analysis_id (int): Analysis ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.rgb_api.rgb_param_color_used_analyse(analysis_id)
        if api_response.JsonRgbUsedParamColorByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonRgbUsedParamColorByAnalyseIDResult

    def rgb_param_color_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Parameter]:
        """ Returns the greening RGB plant and leaf parameters used in the analysis by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.rgb_api.rgb_param_color_used(device_id, round_id, tray_id)
        if api_response.JsonRgbUsedParamColorResult is None:
            return []
        else:
            return api_response.JsonRgbUsedParamColorResult

    def rgb_plant_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.PlantParameter]:
        """ Returns the RGB plant parameter values for the parameter defined by parameter ID and
        calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.PlantParameter] """
        api_response = self.rgb_api.rgb_plant_param_analyse(analysis_id, param_id)
        if api_response.JsonRgbPlantParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonRgbPlantParamByAnalyseIDResult

    def rgb_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.PlantParameter]:
        """ Returns the RGB plant parameter values for the parameter defined by parameter ID, by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.PlantParameter] """
        api_response = self.rgb_api.rgb_plant_param(device_id, round_id, tray_id, param_id)
        if api_response.JsonRgbPlantParamResult is None:
            return []
        else:
            return api_response.JsonRgbPlantParamResult

    def rgb_plant_param_color_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.PlantParameter]:
        """ Returns the RGB greening plant parameter values for the parameter defined by parameter ID and calculated
        in the analysis defined by analyse ID (for greening analysis)

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.PlantParameter] """
        api_response = self.rgb_api.rgb_plant_param_color_analyse(analysis_id, param_id)
        if api_response.JsonRgbPlantParamColorByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonRgbPlantParamColorByAnalyseIDResult

    def rgb_plant_param_color(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.PlantParameter]:
        """ Returns the RGB greening plant parameter values for the parameter defined by parameter ID and calculated
        in the analysis defined by analyse ID (for greening analysis)

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.PlantParameter] """
        api_response = self.rgb_api.rgb_plant_param_color(device_id, round_id, tray_id, param_id)
        if api_response.JsonRgbPlantParamColorResult is None:
            return []
        else:
            return api_response.JsonRgbPlantParamColorResult

    def rgb_leaf_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.LeafParameter]:
        """ Returns the RGB leaf parameter values for the parameter defined by parameter ID and calculated
        in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.LeafParameter] """
        api_response = self.rgb_api.rgb_leaf_param_analyse(analysis_id, param_id)
        if api_response.JsonRgbLeafParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonRgbLeafParamByAnalyseIDResult

    def rgb_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.LeafParameter]:
        """ Returns the RGB leaf parameter values for the parameter defined by parameter ID,
        by tray ID, by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.LeafParameter] """
        api_response = self.rgb_api.rgb_leaf_param(device_id, round_id, tray_id, param_id)
        if api_response.JsonRgbLeafParamResult is None:
            return []
        else:
            return api_response.JsonRgbLeafParamResult

    def rgb_leaf_param_color_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.LeafParameter]:
        """ Returns the RGB greening leaf parameter values for the parameter defined by parameter ID and calculated
        in the analysis defined by analyse ID (for greening analysis)

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.LeafParameter] """
        api_response = self.rgb_api.rgb_leaf_param_color_analyse(analysis_id, param_id)
        if api_response.JsonRgbLeafParamColorByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonRgbLeafParamColorByAnalyseIDResult

    def rgb_leaf_param_color(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.LeafParameter]:
        """ Returns the RGB greening leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of round
        in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.LeafParameter] """
        api_response = self.rgb_api.rgb_leaf_param_color(device_id, round_id, tray_id, param_id)
        if api_response.JsonRgbLeafParamColorResult is None:
            return []
        else:
            return api_response.JsonRgbLeafParamColorResult

# Scan3d API
    def scan3d_imaging_measure(self, meas_id: int) -> swagger_client.Scan3DImaging:
        """ Returns 3D imaging data by scan 3D measure ID

        Args:
            meas_id (int): Meusurement ID

        Return:
            swagger_client.Scan3DImaging """
        api_response = self.scan3d_api.scan3d_imaging_measure(id)
        return api_response.JsonScan3dImagingByIDResult

    def scan3d(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Scan3DImaging]:
        """ Returns 3D imaging data for tray defined by tray ID, by round ID of round in which the tray
        was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.Scan3DImaging """
        api_response = self.scan3d_api.scan3d(device_id, round_id, tray_id)
        if api_response.JsonScan3dImagingResult is None:
            return []
        else:
            return api_response.JsonScan3dImagingResult

    def scan3d_imaging_extended_data_measure(self, meas_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns 3D imaging extended data by scan 3D measure ID

        Args:
            meas_id (int): Meusurement ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.scan3d_api.scan3d_imaging_extended_data_measure(meas_id)
        return api_response.JsonScan3DMeasureExtendedDataByIDResult

    def scan3d_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns 3D extended data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.scan3d_api.i_scan3d_imaging_extended_data(device_id, round_id, tray_id)
        return api_response.JsonScan3dMeasureExtendedDataResult

    def scan3d_analyzed_model_measure(self, meas_id: int) -> swagger_client.Scan3DAnalyzedModel:
        """ Returns the analyzed 3D data as a triangulated 3D model defined by scan 3D measure ID

        Args:
            meas_id (int): Meusurement ID

        Return:
            swagger_client.Scan3DAnalyzedModel """
        api_response = self.scan3d_api.scan3d_analyzed_model_measure(id)
        if api_response.JsonScan3dAnalyzedModelByMeasureIDResult is None:
            return []
        else:
            return api_response.JsonScan3dAnalyzedModelByMeasureIDResult

    def scan3d_analysed_model_analyse(self, analysis_id: int) -> swagger_client.Scan3DAnalyzedModel:
        """ Returns the analyzed 3D data as a triangulated 3D model defined by analyse ID

        Args:
            analysis_id (int): Analysis ID

        Return:
            swagger_client.Scan3DAnalyzedModel """
        api_response = self.scan3d_api.scan3d_analysed_model_analyse(id)
        if api_response.JsonScan3dAnalyzedModelByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonScan3dAnalyzedModelByAnalyseIDResult

    def scan3d_analyzed_model(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.Scan3DAnalyzedModel:
        """ Returns the analyzed 3D data as a triangulated 3D model defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.Scan3DAnalyzedModel """
        api_response = self.scan3d_api.scan3d_analyzed_model(device_id, round_id, tray_id)
        if api_response.JsonScan3dAnalyzedModelResult is None:
            return []
        else:
            return api_response.JsonScan3dAnalyzedModelResult

    def scan3d_param(self, param_id: int) -> swagger_client.Parameter:
        """ Returns one 3D parameter by parameter ID

        Args:
            param_id (int): Parameter ID

        Return:
            swagger_client.Parameter """
        api_response = self.scan3d_api.scan3d_param(param_id)
        return api_response.JsonScan3dParamResult

    def scan3d_param_used_analyse(self, analysis_id: int) -> List[swagger_client.Parameter]:
        """ Returns the 3D plant and leaf parameters used in the analysis defined by analyse ID

        Args:
            analysis_id (int): Ánalysis ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.scan3d_api.scan3d_param_used_analyse(analysis_id)
        if api_response.JsonScan3dUsedParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonScan3dUsedParamByAnalyseIDResult

    def scan3d_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Parameter]:
        """ Returns the 3D plant and leaf parameters used in the analysis by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.scan3d_api.scan3d_param_used(device_id, round_id, tray_id)
        if api_response.JsonScan3dUsedParamResult is None:
            return []
        else:
            return api_response.JsonScan3dUsedParamResult

    def scan3d_plant_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.PlantParameter]:
        """ Returns the 3D plant parameter values for the parameter defined by parameter ID and
        calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Ánalysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.PlantParameter] """
        api_response = self.scan3d_api.scan3d_plant_param_analyse(analysis_id, param_id)
        if api_response.JsonScan3dPlantParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonScan3dPlantParamByAnalyseIDResult

    def scan3d_plant_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.PlantParameter]:
        """ Returns the 3D plant parameter values for the parameter defined by parameter ID and
        calculated in the analysis defined by analyse ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.PlantParameter] """
        api_response = self.scan3d_api.scan3d_plant_param(device_id, round_id, tray_id, param_id)
        if api_response.JsonScan3dPlantParamResult is None:
            return []
        else:
            return api_response.JsonScan3dPlantParamResult

    def scan3d_leaf_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.LeafParameter]:
        """ Returns the 3D local leaf parameter values for the parameter defined by parameter ID and calculated
        in the analysis defined by analyse ID

        Args:
            analysis_id (int): Ánalysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.LeafParameter] """
        api_response = self.scan3d_api.scan3d_leaf_param_analyse(id, param_id)
        if api_response.JsonScan3dLeafParamByAnalyseIDResult is None:
            return []
        else:
            return api_response.JsonScan3dLeafParamByAnalyseIDResult

    def scan3d_leaf_param(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.LeafParameter]:
        """ Returns the 3D local leaf parameter values for the parameter defined by parameter ID, by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.LeafParameter] """
        api_response = self.scan3d_api.scan3d_leaf_param(device_id, round_id, tray_id, param_id)
        if api_response.JsonScan3dLeafParamResult is None:
            return []
        else:
            return api_response.JsonScan3dLeafParamResult
