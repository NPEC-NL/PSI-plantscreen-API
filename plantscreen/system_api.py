import plantscreen.swagger_client as swagger_client
import plantscreen.models as models
from constants import REQUEST_TIMEOUT
from typing import List


class SystemAPI():
    """ Wrapper around the automatically  generated swagger client.
       \n return class instances instead of dictionaries """
    def __init__(self, server: str, poort: str):
        """ Initialises the API connection

        Args:
            server (str): Server url
            poort (str): Poort number

        Return:
            SystemAPI instance """
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

        Return:
            swagger_client.Probe """
        api_response = self.probe_api.probe(_request_timeout=REQUEST_TIMEOUT)
        return api_response.json_probe_result

    def probeID(self, probe_id: int) -> swagger_client.Probe:
        """ If called without ID it returns all probeIDs,
        when called with it returns one environment probe of that probe ID

        Args:
            probe_id (int): Probe ID

        Return:
            swagger_client.Probe """
        api_response = self.probe_api.probe(id=probe_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_probe_by_id_result

    def probe_value_date(self, start: str, stop: str) -> List[swagger_client.ProbeValue]:
        """ Returns all probe values measured between times.
        Times is entered as the start and end time of the required interval

        Args:
            start (str): Startdate
            stop (str): Stopdate

        Return:
            swagger_client.Probe """
        api_response = self.probe_api.probe_value_date(start, stop, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_probe_value_by_date_result

    def probe_value_date_probe(self, probe_id: int, start: str, stop: str) -> List[swagger_client.ProbeValue]:
        """ Returns all probe values for probe defined by probe ID measured between times.
        Times is entered as the start and end time of the required interval

        Args:
            probe_id (int): Probe ID
            start (str): Startdate
            stop (str): Stopdate

        Return:
            swagger_client.Probe """
        api_response = self.probe_api.probe_value_date_probe(probe_id, start, stop, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_probe_value_by_id_and_date_result

# Scales API
    def scales_plant_weight_measure(self, meas_id) -> swagger_client.ScalesData:
        """ Returns scales data by measure ID

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.ScalesData """
        api_response = self.scales_api.scales_plant_weight_measure(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scales_measure_by_id_result

    def scales_plant_weight(self, device_id: int, round_id: int, tray_id: int) -> List[swagger_client.ScalesData]:
        """ Returns scales data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            List[swagger_client.ScalesData] """
        api_response = self.scales_api.scales_plant_weight(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_scales_measure_result

    def scales_weight_reference_plant(self, meas_id: int) -> swagger_client.PlantWeightReference:
        """ Returns plant weight reference data by plant ID. The weight is in units of grams

        Args:
            meas_id (int): Measurement ID

        Return:
            swagger_client.PlantWeightReference """
        api_response = self.scales_api.scales_weight_reference_plant(meas_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_plant_weight_reference_by_plant_id_result

    def scales_weight_reference_tray(self, tray_id: int) -> List[swagger_client.PlantWeightReference]:
        """ Returns plant weight reference data by tray ID. The weight is in units of grams

        Args:
            tray_id (int): Tray ID

        Return:
            List[swagger_client.PlantWeightReference] """
        api_response = self.scales_api.scales_weight_reference_tray(tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_plant_weight_reference_by_tray_id_result

    def scales_weight_reference_to_date_tray(self, tray_id: int, date: str) -> List[swagger_client.PlantWeightReference]:
        """ Returns plant weight reference data by plant ID. The weight is in units of grams

        Args:
            tray_id (int): Tray ID
            date (str): Date

        Return:
            List[swagger_client.PlantWeightReference] """
        api_response = self.scales_api.scales_weight_reference_to_date_tray(tray_id, date, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_plant_weight_reference_by_tray_id_to_date_result

# Spray API
    def spray_action(self, device_id: int, round_id: int, tray_id: int) -> swagger_client.SprayAction:
        """ Return spray action data for tray defined by tray ID,
        by round ID of round in which the tray was measured and by device defined by device ID

        Args:
            device_id (int): Device ID
            round_id (int): Round ID
            tray_id (int): Tray ID

        Return:
            swagger_client.SprayAction """
        api_response = self.spray_api.spray_action(device_id, round_id, tray_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_spray_action_result

# Spectrum Device API
    def spectrum_device_id(self) -> List[int]:
        """ Returns a list of all spectrum device IDs in the database

        Return:
            List[int] """
        api_response = self.spectrum_device_api.spectrum_device_id(_request_timeout=REQUEST_TIMEOUT)
        return models.spectrum_device.SpectrumDeviceIDs.from_dict(api_response.to_dict())

    def spectrum_device(self, spec_dev_id: int) -> swagger_client.SpectrumDevice:
        """ Returns one spectrum device by spectrum device ID

        Args:
            spec_dev_id (int): Spectrum Device ID

        Return:
            swagger_client.SpectrumDevice """
        api_response = self.spectrum_device_api.spectrum_device(spec_dev_id, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_spectrum_device_result

    def spectrum_values_date_device(self, spec_dev_id: int, start: str, stop: str) -> List[swagger_client.SpectrumDevice]:
        """ Returns one spectrum device by spectrum device ID

        Args:
            spec_dev_id (int): Spectrum Device ID
            start (str): Startdate
            stop (str): Stopdate

        Return:
            List[swagger_client.SpectrumDevice] """
        api_response = self.spectrum_device_api.spectrum_values_date_device(spec_dev_id, start, stop, _request_timeout=REQUEST_TIMEOUT)
        return api_response.json_spectrum_values_result
