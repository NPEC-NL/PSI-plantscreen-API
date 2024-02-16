from plantscreen.admin_api import AdminAPI
from plantscreen.imaging_api import ImagingAPI
from plantscreen.system_api import SystemAPI


class Complete_API(AdminAPI, ImagingAPI, SystemAPI):
    """"Child class that inherits all the API calls"""
    def __init__(self, server, poort):
        """ Initialises the API connection

        Args:
            server (str): Server url
            poort (str): Poort number

        Return:
            Complete_API instance, containing the admin, imaging and systems api's """
        AdminAPI.__init__(self, server, poort)
        ImagingAPI.__init__(self, server, poort)
        SystemAPI.__init__(self, server, poort)
