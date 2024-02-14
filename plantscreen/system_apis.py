import plantscreen.swagger_client as swagger_client
import plantscreen.models as models
from typing import List


class Imaging_API():
    """ Wrapper around the automatically  generated swagger client.
       \n return class instances instead of dictionaries """
    def __init__(self, server, poort):
        configuration = swagger_client.Configuration()
        configuration.host = f'{server}:{poort}/RestService/json'
        self.probe_api = swagger_client.ProbeApi(swagger_client.ApiClient(configuration))
        self.scales_api = swagger_client.ScalesApi(swagger_client.ApiClient(configuration))
        self.spray_api = swagger_client.SprayApi(swagger_client.ApiClient(configuration))
        self.spectrum_device_api = swagger_client.SpectrumDeviceApi(swagger_client.ApiClient(configuration))

# Probe API
    def probe(self) -> swagger_client.Probe:
        """ If called without ID it returns all probeIDs,
        when called with it returns one environment probe of that probe ID

        Args:
            -

        Return:
            swagger_client.Probe """
        api_response = self.probe_api.probe()
        return api_response.JsonProbeResult

    def probeID(self, probe_id: int) -> swagger_client.Probe:
        """ If called without ID it returns all probeIDs,
        when called with it returns one environment probe of that probe ID

        Args:
            probe_id (int): Probe ID

        Return:
            swagger_client.Probe """
        api_response = self.probe_api.probe(probe_id)
        return api_response.JsonProbeByIDResult

    def probe_value_date(self, start: str, stop: str) -> List[swagger_client.ProbeValue]:
        """ Returns all probe values measured between times.
        Times is entered as the start and end time of the required interval

        Args:
            start (str): Startdate
            stop (str): Stopdate

        Return:
            swagger_client.Probe """
        api_response = self.probe_api.probe_value_date(start, stop)
        if api_response.JsonProbeValueByDateResult is None:
            return []
        else:
            return api_response.JsonProbeValueByDateResult

    def probe_value_date_probe(self, probe_id: int, start: str, stop: str) -> List[swagger_client.ProbeValue]:
        """ Returns all probe values for probe defined by probe ID measured between times.
        Times is entered as the start and end time of the required interval

        Args:
            probe_id (int): Probe ID
            start (str): Startdate
            stop (str): Stopdate

        Return:
            swagger_client.Probe """
        api_response = self.probe_api.probe_value_date_probe(probe_id, start, stop)
        if api_response.JsonProbeValueByIDAndDateResult is None:
            return []
        else:
            return api_response.JsonProbeValueByIDAndDateResult

# Scales API
    def scales_plant_weight_measure(self, meas_id) -> swagger_client.ScalesData:
        """ Returns scales data by measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.ScalesData """
        api_response = self.scales_api.scales_plant_weight_measure(id)
        return api_response.JsonScalesMeasureByIDResult

    def get_scales_plant_weight(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.ScalesData]:
        """ Returns scales data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.ScalesData] """
        api_response = self.scales_api.scales_plant_weight(device_id, round_id, tray_id)
        if api_response.JsonScalesMeasureResult is None:
            return []
        else:
            return api_response.JsonScalesMeasureResult

    def get_scales_weight_reference_plant(self, meas_id: int) -> swagger_client.PlantWeightReference:
        """ Returns plant weight reference data by plant ID. The weight is in units of grams

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.PlantWeightReference """
        api_response = self.scales_api.scales_weight_reference_plant(meas_id)
        return api_response.JsonPlantWeightReferenceByPlantIDResult

    def get_scales_weight_reference_tray(self, tray_id: int) -> List[swagger_client.PlantWeightReference]:
        """ Returns plant weight reference data by tray ID. The weight is in units of grams

        Args:
            tray_id (int): Tray ID

        Return:
            List[swagger_client.PlantWeightReference] """
        api_response = self.scales_api.scales_weight_reference_tray(tray_id)
        if api_response.JsonPlantWeightReferenceByTrayIDResult is None:
            return []
        else:
            return api_response.JsonPlantWeightReferenceByTrayIDResult

    def get_scales_weight_reference_to_date_tray(self, tray_id: int, date: str) -> List[swagger_client.PlantWeightReference]:
        """ Returns plant weight reference data by plant ID. The weight is in units of grams

        Args:
            tray_id (int): Tray ID
            date (str): Date

        Return:
            List[swagger_client.PlantWeightReference] """
        api_response = self.scales_api.scales_weight_reference_to_date_tray(tray_id, date)
        if api_response.JsonPlantWeightReferenceByTrayIDToDateResult is None:
            return []
        else:
            return api_response.JsonPlantWeightReferenceByTrayIDToDateResult

# Spray API
    def get_spray_action(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.SprayAction:
        """ Return spray action data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.SprayAction """
        api_response = self.spray_api.spray_action(device_id, round_id, tray_id)
        if api_response.JsonSprayActionResult is None:
            return []
        else:
            return api_response.JsonSprayActionResult

# Spectrum Device API
    def get_spectrum_device_id(self) -> List[int]:
        """ Returns a list of all spectrum device IDs in the database

        Args:
            -

        Return:
            List[int] """
        api_response = self.spectrum_device_api.spectrum_device_id()
        return models.spectrum_device.SpectrumDeviceIDs.from_dict(api_response.to_dict())

    def get_spectrum_device(self, spec_dev_id: int) -> swagger_client.SpectrumDevice:
        """ Returns one spectrum device by spectrum device ID

        Args:
            spec_dev_id (int): Spectrum Device ID

        Return:
            swagger_client.SpectrumDevice """
        api_response = self.spectrum_device_api.spectrum_device(spec_dev_id)
        return api_response.JsonSpectrumDeviceResult

    def get_spectrum_values_date_device(self, spec_dev_id: int, start: str, stop: str) -> List[swagger_client.SpectrumDevice]:
        """ Returns one spectrum device by spectrum device ID

        Args:
            spec_dev_id (int): Spectrum Device ID
            start (str): Startdate
            stop (str): Stopdate

        Return:
            List[swagger_client.SpectrumDevice] """
        api_response = self.spectrum_device_api.spectrum_values_date_device(spec_dev_id, start, stop)
        if api_response.JsonSpectrumValuesResult is None:
            return []
        else:
            return api_response.JsonSpectrumValuesResult
