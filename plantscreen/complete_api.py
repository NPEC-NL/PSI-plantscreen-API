import plantscreen.swagger_client as swagger_client
from plantscreen.admin_api import AdminAPI
from plantscreen.imaging_api import ImagingAPI
from plantscreen.system_api import SystemAPI


class Plantscreen_API(AdminAPI, ImagingAPI, SystemAPI):
    """"Child class that inherits all the API calls"""
    def __init__(self, server, poort):
        configuration = swagger_client.Configuration()
        configuration.host = f'{server}:{poort}/RestService/json'
        super(Plantscreen_API, self).__init__(server, poort)
