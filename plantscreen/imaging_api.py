import plantscreen.swagger_client as swagger_client
from plantscreen.constants import REQUEST_TIMEOUT
from typing import List


class ImagingAPI():
    """ Wrapper around the automatically  generated swagger client.
       \n return class instances instead of dictionaries """
    def __init__(self, server: str, poort: str):
        """ Initialises the API connection

        Args:
            server (str): Server url
            poort (str): Poort number

        Return:
            ImagingAPI instance """
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
        api_response = self.fc_api.fc_imaging_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_imaging_by_id_result

    def fc_imaging(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.FcImaging:
        """ Returns FluorCam imaging data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.FcImaging """
        api_response = self.fc_api.fc_imaging(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_imaging_result

    def fc_imaging_extended_data_measure(self, meas_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns FluorCam imaging extended data by FC measure ID. (Only available for field systems

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.fc_api.fc_imaging_extended_data_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_measure_extended_data_by_id_result

    def fc_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns FluorCam extended data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID.

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.fc_api.fc_imaging_extended_data(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_measure_extended_data_result

    def fc_plant_mask_measure(self, meas_id: int) -> swagger_client.PlantMask:
        """ Returns the FluorCam plant mask created for the measured tray defined by FC measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.PlantMask """
        api_response = self.fc_api.fc_plant_mask_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_plant_mask_by_measure_id_result

    def fc_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.PlantMask:
        """ Returns FluorCam plant masks created for the tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.PlantMask """
        api_response = self.fc_api.fc_plant_mask(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_plant_mask_result

    def fc_param(self, param_id: int) -> swagger_client.Parameter:
        """ Returns one FluorCam parameter by parameter ID

        Args:
            param_id (int): Parameter ID

        Return:
            swagger_client.Parameter """
        api_response = self.fc_api.fc_param(param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_param_result

    def fc_param_used_analyse(self, analisys_id: int) -> swagger_client.Parameter:
        """ Returns the FluorCam plant and leaf parameters used in the analysis defined by analyse ID

        Args:
            analisys_id (int): Analysis ID

        Return:
            swagger_client.Parameter """
        api_response = self.fc_api.fc_param_used_analyse(analisys_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_used_param_by_analyse_id_result

    def fc_param_used(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.Parameter:
        """ Returns the FluorCam plant and leaf parameters used in the analysis by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.Parameter """
        api_response = self.fc_api.fc_param_used(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_used_param_result

    def fc_param_image_analyse(self, analisys_id: int, param_id: int) -> swagger_client.ParameterImage:
        """ Returns the FluorCam parameter image for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            analisys_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            swagger_client.ParameterImage """
        api_response = self.fc_api.fc_param_image_analyse(analisys_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_parameter_image_by_analyse_id_result

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
        api_response = self.fc_api.fc_param_image(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_parameter_image_result

    def fc_plant_param_analyse(self, analisys_id: int, param_id: int) -> swagger_client.PlantParameter:
        """ Returns the FluorCam plant parameter values for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            analisys_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            swagger_client.PlantParameter """
        api_response = self.fc_api.fc_plant_param_analyse(analisys_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_plant_param_by_analyse_id_result

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
        api_response = self.fc_api.fc_plant_param(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_plant_param_result

    def fc_leaf_param_analyse(self, analisys_id: int, param_id: int) -> swagger_client.LeafParameter:
        """ Returns the FluorCam leaf parameter values for the parameter defined by parameter ID and
        calculated in the analysis defined by analyse ID

        Args:
            analisys_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            swagger_client.PlantParameter """
        api_response = self.fc_api.fc_leaf_param_analyse(analisys_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_leaf_param_by_analyse_id_result

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
        api_response = self.fc_api.fc_leaf_param(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_fc_leaf_param_result

# Hc API
    def hc_imaging_measure(self, meas_id: int) -> swagger_client.HcImaging:
        """ Returns Hyperspectral imaging data by HC measure ID

        Args:
            meas_id (int): Measure ID

        Return:
            swagger_client.HcImaging """
        api_response = self.hc_api.hc_imaging_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_imaging_by_id_result

    def hc_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.HcImaging]:
        """ Returns Hyperspectral imaging data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.HcImaging] """
        api_response = self.hc_api.hc_imaging(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_imaging_result

    def hc_imaging_extended_data_measure(self, meas_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns Hyperspectral imaging extended data by HC measure ID

        Args:
            meas_id (int): Measure ID

        Return:
            swagger_client.HcImaging """
        api_response = self.hc_api.hc_imaging_extended_data_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_measure_extended_data_by_id_result

    def hc_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.MeasureExtendedData]:
        """ Returns Hyperspectral imaging extended data by HC measure ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.MeasureExtendedData] """
        api_response = self.hc_api.hc_imaging_extended_data(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_measure_extended_data_result

    def hc_rgb_image_measure(self, meas_id: int) -> swagger_client.HcRgbImage:
        """ Returns Hyperspectral imaging extended data by HC measure ID

        Args:
            meas_id (int): Measure ID

        Return:
            swagger_client.HcRgbImage """
        api_response = self.hc_api.hc_rgb_image_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_rgb_image_by_measure_id_result

    def hc_rgb_image(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.HcRgbImage]:
        """ Returns Hyperspectral imaging extended data by HC measure ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.HcRgbImage] """
        api_response = self.hc_api.hc_rgb_image(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_rgb_image_result

    def hc_plant_mask_measure(self, meas_id: int) -> swagger_client.PlantMask:
        """ Returns the Hyperspectral plant mask created for the measured tray defined by HC measure ID

        Args:
            meas_id (int): Measure ID

        Return:
            swagger_client.PlantMask """
        api_response = self.hc_api.hc_plant_mask_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_plant_mask_by_measure_id_result

    def hc_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.PlantMask]:
        """ Returns Hyperspectral plant masks created for the tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.PlantMask] """
        api_response = self.hc_api.hc_plant_mask(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_plant_mask_result

    def hc_param(self, param_id: int) -> swagger_client.Parameter:
        """ Returns one Hyperspectral parameter by parameter ID

        Args:
            param_id (int): Parameter ID

        Return:
            swagger_client.Parameter """
        api_response = self.hc_api.hc_param(param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_param_result

    def hc_param_used_analyse(self, analysis_id: int) -> List[swagger_client.Parameter]:
        """ Returns the Hyperspectral plant and leaf parameters used in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID

        Return:
            list[swagger_client.Parameter] """
        api_response = self.hc_api.hc_param_used_analyse(analysis_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_used_param_by_analyse_id_result

    def hc_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Parameter]:
        """ Returns the Hyperspectral plant and leaf parameters used in the analysis by tray ID, by round ID
        of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            list[swagger_client.Parameter] """
        api_response = self.hc_api.hc_param_used(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_used_param_result

    def hc_param_image_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.ParameterImage]:
        """ Returns the Hyperspectral parameter image for the parameter defined by parameter ID and calculated
        in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            list[swagger_client.ParameterImage] """
        api_response = self.hc_api.hc_param_image_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_parameter_image_by_analyse_id_result

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
        api_response = self.hc_api.hc_param_image(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_parameter_image_result

    def hc_plant_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.StatisticPlantParameter]:
        """ Returns the Hyperspectral statistic plant parameter values for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            list[swagger_client.StatisticPlantParameter] """
        api_response = self.hc_api.hc_plant_param_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_plant_param_by_analyse_id_result

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
        api_response = self.hc_api.hc_plant_param(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_plant_param_result

    def hc_leaf_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.StatisticLeafParameter]:
        """ Returns the Hyperspectral statistic leaf parameter values for the parameter defined by parameter ID and
        calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            list[swagger_client.StatisticLeafParameter] """
        api_response = self.hc_api.hc_leaf_param_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_leaf_param_by_analyse_id_result

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
        api_response = self.hc_api.hc_leaf_param(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_hc_leaf_param_result

# Ir API
    def ir_imaging_measure(self, meas_id: int) -> swagger_client.Imaging:
        """ Returns Thermal imaging data by IR measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.Imaging """
        api_response = self.ir_api.ir_imaging_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        api_response.json_ir_imaging_by_id_result

    def ir_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Imaging]:
        """ Returns Thermal imaging data for tray defined by tray ID, by round ID of round in which the
        tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Imaging] """
        api_response = self.ir_api.ir_imaging(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_imaging_result

    def ir_imaging_extended_data_measure(self, meas_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns Thermal imaging data by IR measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.ir_api.ir_imaging_extended_data_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_measure_extended_data_by_id_result

    def ir_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns Thermal extended data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.ir_api.ir_imaging_extended_data(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_measure_extended_data_result

    def ir_plant_mask_measure(self, meas_id: int) -> swagger_client.PlantMask:
        """ Returns the Thermal plant mask created for the measured tray defined by IR measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.PlantMask """
        api_response = self.ir_api.ir_plant_mask_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_plant_mask_by_measure_id_result

    def ir_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.PlantMask]:
        """ Returns Thermal plant masks created for the tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.PlantMask] """
        api_response = self.ir_api.ir_plant_mask(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_plant_mask_result

    def ir_plant_mask_image_measure(self, meas_id: int) -> swagger_client.Imaging:
        """ Returns Thermal imaging data masked by the plant mask defined by IR measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.Imaging """
        api_response = self.ir_api.ir_plant_mask_image_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_plant_mask_image_by_measure_id_result

    def ir_plant_mask_image(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Imaging]:
        """ Returns Thermal imaging data masked by the plant mask for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Imaging] """
        api_response = self.ir_api.ir_plant_mask_image(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_plant_mask_image_result

    def ir_param(self, param_id: int) -> swagger_client.Parameter:
        """ Returns one Thermal parameter by parameter ID

        Args:
            param_id (int): Parameter ID

        Return:
            swagger_client.Parameter """
        api_response = self.ir_api.ir_param(param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_param_result

    def ir_param_used_analyse(self, analysis_id: int) -> List[swagger_client.Parameter]:
        """ Returns the Thermalplant and leaf parameters used in the analysis defined by analyse ID

        Args:
            analysis_id (int): analysis ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.ir_api.ir_param_used_analyse(analysis_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_used_param_by_analyse_id_result

    def ir_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Parameter]:
        """ Returns the Thermal plant and leaf parameters used in the analysis by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.ir_api.ir_param_used(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_used_param_result

    def ir_plant_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.StatisticPlantParameter]:
        """ Returns the Thermal plant parameter values for the parameter defined by parameter ID and
        calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.StatisticPlantParameter] """
        api_response = self.ir_api.ir_plant_param_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_plant_param_by_analyse_id_result

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
        api_response = self.ir_api.ir_plant_param(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_plant_param_result

    def ir_leaf_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.StatisticLeafParameter]:
        """ Returns the Thermal statistic leaf parameter values for the parameter defined by
        parameter ID and calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.StatisticLeafParameter] """
        api_response = self.ir_api.ir_leaf_param_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_leaf_param_by_analyse_id_result

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
        api_response = self.ir_api.ir_leaf_param(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_ir_leaf_param_result

# Msc API
    def msc_imaging_measure(self, meas_id: int) -> swagger_client.Imaging:
        """ Returns Multispectral imaging data by MSC measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.Imaging """
        api_response = self.msc_api.msc_imaging_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_imaging_by_id_result

    def msc_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Imaging]:
        """ Returns Multispectral imaging data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Imaging] """
        api_response = self.msc_api.msc_imaging(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_imaging_result

    def msc_imaging_extended_data_measure(self, meas_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns Multispectral imaging extended data by MSC measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.msc_api.msc_imaging_extended_data_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_measure_extended_data_by_id_result

    def msc_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns Multispectral extended data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.msc_api.msc_imaging_extended_data(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_measure_extended_data_result

    def msc_plant_mask_measure(self, meas_id: int) -> swagger_client.PlantMask:
        """ Returns Multispectral extended data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.PlantMask """
        api_response = self.msc_api.msc_plant_mask_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_plant_mask_by_measure_id_result

    def msc_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.PlantMask]:
        """ Returns Multispectral plant mask by device, round and tray ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.PlantMask """
        api_response = self.msc_api.msc_plant_mask(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_plant_mask_result

    def msc_param(self, param_id: int) -> swagger_client.Parameter:
        """ Returns one Multispectral parameter by parameter ID

        Args:
            param_id (int): Parameter ID

        Return:
            swagger_client.Parameter """
        api_response = self.msc_api.msc_param(param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_param_result

    def msc_param_used_analyse(self, analysis_id: int) -> List[swagger_client.Parameter]:
        """ Returns Multispectral used plant parameters by analyse ID

        Args:
            analysis_id (int): Analysis ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.msc_api.msc_param_used_analyse(analysis_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_used_param_by_analyse_id_result

    def msc_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Parameter]:
        """ Returns the Multispectral plant and leaf parameters used in the analysis by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.msc_api.msc_param_used(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_used_param_result

    def msc_param_image_analyse(self, analysis_id: int, param_id: int) -> swagger_client.ParameterImage:
        """ Returns the Multispectral parameter image for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            swagger_client.ParameterImage """
        api_response = self.msc_api.msc_param_image_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_parameter_image_by_analyse_id_result

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
        api_response = self.msc_api.msc_param_image(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_parameter_image_result

    def msc_plant_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.StatisticPlantParameter]:
        """ Returns the Multispectral parameter image for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.StatisticPlantParameter] """
        api_response = self.msc_api.msc_plant_param_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_plant_param_by_analyse_id_result

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
        api_response = self.msc_api.msc_plant_param(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_plant_param_result

    def msc_leaf_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.StatisticLeafParameter]:
        """ Returns the Multispectral statistic leaf parameter values for the parameter defined by parameter ID
        and calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.StatisticLeafParameter] """
        api_response = self.msc_api.msc_leaf_param_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_leaf_param_by_analyse_id_result

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
        api_response = self.msc_api.msc_leaf_param(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_leaf_param_result

    def msc_light_set(self, lightset_id: int) -> swagger_client.MscLightSet:
        """ Returns one set of the lights for multispectral camera service defined by light set ID

        Args:
            lightset_id (int): Lightset ID

        Return:
            swagger_client.MscLightSet """
        api_response = self.msc_api.msc_light_set(lightset_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_light_set_result

    def msc_light_set_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.MscLightSet]:
        """ Returns the sets of the lights for multispectral camera service used in the measure for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.MscLightSet] """
        api_response = self.msc_api.msc_light_set_used(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_light_set_used_result

    def msc_calibration(self, calib_id: int) -> swagger_client.MscCalibration:
        """ Returns one Multispectral calibration for individual groups of lights
        with information about the exposure and gain of the camera defined by calibration ID

        Args:
            calib_id (int): Calibration ID

        Return:
            swagger_client.MscCalibration """
        api_response = self.msc_api.msc_calibration(calib_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_calibration_result

    def msc_calibration_light_set(self, lightset_id: int) -> swagger_client.MscCalibration:
        """ Returns the Multispectral calibration for individual groups of lights with
        information about the exposure and gain of the camera defined by light set ID

        Args:
            lightset_id (int): Lightset ID

        Return:
            swagger_client.MscCalibration """
        api_response = self.msc_api.msc_calibration_light_set(lightset_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_msc_calibration_by_light_set_id_result

    def msc_calibration_light(self) -> swagger_client.MscCalibrationLight:
        """ Returns a list of all lightsettings if no ID is passed.
        Or the light output setting for light group calibration defined by calibration light ID

        Return:
            swagger_client.MscCalibrationLight """
        api_response = self.msc_api.msc_calibration_light()
        return api_response.json_msc_calibration_light_result

# RGB API
    def rgb_imaging_measure(self, meas_id: int) -> swagger_client.Imaging:
        """ Returns RGB imaging data by RGB measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.Imaging """
        api_response = self.rgb_api.rgb_imaging_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_imaging_by_id_result

    def rgb_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Imaging]:
        """ Returns FluorCam imaging data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.Imaging """
        api_response = self.rgb_api.rgb_imaging(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_imaging_result

    def rgb_imaging_extended_data_measure(self, meas_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns RGB imaging extended data by RGB measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.rgb_api.rgb_imaging_extended_data_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_measure_extended_data_by_id_result

    def rgb_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns RGB extended data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.rgb_api.rgb_imaging_extended_data(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_measure_extended_data_result

    def rgb_plant_mask_measure(self, meas_id) -> swagger_client.PlantMask:
        """ Returns the RGB plant mask created for the measured tray defined by RGB measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.rgb_api.rgb_plant_mask_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_plant_mask_by_measure_id_result

    def rgb_plant_mask(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.PlantMask]:
        """ Returns RGB plant masks created for the tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.PlantMask] """
        api_response = self.rgb_api.rgb_plant_mask(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_plant_mask_result

    def rgb_greening_mask_image_measure(self, meas_id: int) -> swagger_client.RgbGreeningMaskImage:
        """ Returns RGB greening data masked by the plant mask defined by RGB measure ID.
        The greening mask image is created by greening analysis,
        therefore it is only available if greening analysis has been performed on the required data

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.RgbGreeningMaskImage """
        api_response = self.rgb_api.rgb_greening_mask_image_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_greening_mask_image_by_measure_id_result

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
        api_response = self.rgb_api.rgb_greening_mask_image(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_greening_mask_image_result

    def rgb_param(self, param_id: int) -> swagger_client.Parameter:
        """ Returns one RGB morfo parameter by parameter ID

        Args:
            param_id (int): Measurement ID

        Return:
            swagger_client.RgbGreeningMaskImage """
        api_response = self.rgb_api.rgb_param(param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_param_result

    def rgb_param_used_analyse(self, analysis_id: int) -> List[swagger_client.Parameter]:
        """ Returns the RGB plant and leaf parameters used in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.rgb_api.rgb_param_used_analyse(analysis_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_used_param_by_analyse_id_result

    def rgb_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Parameter]:
        """ Returns the RGB plant and leaf parameters used in the analysis defined by analyse ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.rgb_api.rgb_param_used(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_used_params_result

    def rgb_param_color_used_analyse(self, analysis_id: int) -> List[swagger_client.Parameter]:
        """ Returns the greening RGB plant and leaf parameters used in the greening analysis
        defined by analyse ID (for greening analysis)

        Args:
            analysis_id (int): Analysis ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.rgb_api.rgb_param_color_used_analyse(analysis_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_used_param_color_by_analyse_id_result

    def rgb_param_color_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Parameter]:
        """ Returns the greening RGB plant and leaf parameters used in the analysis by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.rgb_api.rgb_param_color_used(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_used_param_color_result

    def rgb_plant_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.PlantParameter]:
        """ Returns the RGB plant parameter values for the parameter defined by parameter ID and
        calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.PlantParameter] """
        api_response = self.rgb_api.rgb_plant_param_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_plant_param_by_analyse_id_result

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
        api_response = self.rgb_api.rgb_plant_param(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_plant_param_result

    def rgb_plant_param_color_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.PlantParameter]:
        """ Returns the RGB greening plant parameter values for the parameter defined by parameter ID and calculated
        in the analysis defined by analyse ID (for greening analysis)

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.PlantParameter] """
        api_response = self.rgb_api.rgb_plant_param_color_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_plant_param_color_by_analyse_id_result

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
        api_response = self.rgb_api.rgb_plant_param_color(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_plant_param_color_result

    def rgb_leaf_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.LeafParameter]:
        """ Returns the RGB leaf parameter values for the parameter defined by parameter ID and calculated
        in the analysis defined by analyse ID

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.LeafParameter] """
        api_response = self.rgb_api.rgb_leaf_param_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_leaf_param_by_analyse_id_result

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
        api_response = self.rgb_api.rgb_leaf_param(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_leaf_param_result

    def rgb_leaf_param_color_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.LeafParameter]:
        """ Returns the RGB greening leaf parameter values for the parameter defined by parameter ID and calculated
        in the analysis defined by analyse ID (for greening analysis)

        Args:
            analysis_id (int): Analysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.LeafParameter] """
        api_response = self.rgb_api.rgb_leaf_param_color_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_leaf_param_color_by_analyse_id_result

    def rgb_leaf_param_color(self, device_id: int, round_id: int, tray_id: int, param_id: int) -> List[swagger_client.LeafParameter]:
        """ Returns the RGB greening leaf parameter values for the parameter defined by parameter ID, by tray ID, by round ID of
         round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.LeafParameter] """
        api_response = self.rgb_api.rgb_leaf_param_color(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_rgb_leaf_param_color_result

# Scan3d API
    def scan3d_imaging_measure(self, meas_id: int) -> swagger_client.Scan3DImaging:
        """ Returns 3D imaging data by scan 3D measure ID

        Args:
            meas_id (int): Meusurement ID

        Return:
            swagger_client.Scan3DImaging """
        api_response = self.scan3d_api.scan3d_imaging_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_imaging_by_id_result

    def scan3d_imaging(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Scan3DImaging]:
        """ Returns 3D imaging data for tray defined by tray ID, by round ID of round in which the tray
        was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.Scan3DImaging """
        api_response = self.scan3d_api.scan3d(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_imaging_result

    def scan3d_imaging_extended_data_measure(self, meas_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns 3D imaging extended data by scan 3D measure ID

        Args:
            meas_id (int): Meusurement ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.scan3d_api.scan3d_imaging_extended_data_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_measure_extended_data_by_id_result

    def scan3d_imaging_extended_data(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.MeasureExtendedData:
        """ Returns 3D extended data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.MeasureExtendedData """
        api_response = self.scan3d_api.scan3d_imaging_extended_data(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_measure_extended_data_result

    def scan3d_analyzed_model_measure(self, meas_id: int) -> swagger_client.Scan3DAnalyzedModel:
        """ Returns the analyzed 3D data as a triangulated 3D model defined by scan 3D measure ID

        Args:
            meas_id (int): Meusurement ID

        Return:
            swagger_client.Scan3DAnalyzedModel """
        api_response = self.scan3d_api.scan3d_analyzed_model_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_analyzed_model_by_measure_id_result

    def scan3d_analyzed_model_analyse(self, analysis_id: int) -> swagger_client.Scan3DAnalyzedModel:
        """ Returns the analyzed 3D data as a triangulated 3D model defined by analyse ID

        Args:
            analysis_id (int): Analysis ID

        Return:
            swagger_client.Scan3DAnalyzedModel """
        api_response = self.scan3d_api.scan3d_analysed_model_analyse(analysis_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_analyzed_model_by_analyse_id_result

    def scan3d_analyzed_model(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.Scan3DAnalyzedModel:
        """ Returns the analyzed 3D data as a triangulated 3D model defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.Scan3DAnalyzedModel """
        api_response = self.scan3d_api.scan3d_analyzed_model(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_analyzed_model_result

    def scan3d_param(self, param_id: int) -> swagger_client.Parameter:
        """ Returns one 3D parameter by parameter ID

        Args:
            param_id (int): Parameter ID

        Return:
            swagger_client.Parameter """
        api_response = self.scan3d_api.scan3d_param(param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_param_result

    def scan3d_param_used_analyse(self, analysis_id: int) -> List[swagger_client.Parameter]:
        """ Returns the 3D plant and leaf parameters used in the analysis defined by analyse ID

        Args:
            analysis_id (int): Ánalysis ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.scan3d_api.scan3d_param_used_analyse(analysis_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_used_param_by_analyse_id_result

    def scan3d_param_used(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.Parameter]:
        """ Returns the 3D plant and leaf parameters used in the analysis by tray ID,
        by round ID of round in which the tray was analyzed and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.Parameter] """
        api_response = self.scan3d_api.scan3d_param_used(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_used_param_result

    def scan3d_plant_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.PlantParameter]:
        """ Returns the 3D plant parameter values for the parameter defined by parameter ID and
        calculated in the analysis defined by analyse ID

        Args:
            analysis_id (int): Ánalysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.PlantParameter] """
        api_response = self.scan3d_api.scan3d_plant_param_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_plant_param_by_analyse_id_result

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
        api_response = self.scan3d_api.scan3d_plant_param(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_plant_param_result

    def scan3d_leaf_param_analyse(self, analysis_id: int, param_id: int) -> List[swagger_client.LeafParameter]:
        """ Returns the 3D local leaf parameter values for the parameter defined by parameter ID and calculated
        in the analysis defined by analyse ID

        Args:
            analysis_id (int): Ánalysis ID
            param_id (int): Parameter ID

        Return:
            List[swagger_client.LeafParameter] """
        api_response = self.scan3d_api.scan3d_leaf_param_analyse(analysis_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_leaf_param_by_analyse_id_result

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
        api_response = self.scan3d_api.scan3d_leaf_param(device_id, round_id, tray_id, param_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scan3d_leaf_param_result
