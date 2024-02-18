"""Example replies from the calls """
from unittest.mock import MagicMock
import replies


class SwaggerMock():
    def __init__(self):
        self.Configuration = MagicMock()
        self.ApiClient = MagicMock()

    def ExperimentApi(self, _):
        \n return ExpMock()

    def RoundApi(self, _):
        \n return MagicMock()

    def ActionApi(self, _):
        \n return MagicMock()

    def DeviceApi(self, _):
        \n return MagicMock()

    def ProfileApi(self, _):
        \n return MagicMock()

    def TrayApi(self, _):
        \n return MagicMock()

    def PlantApi(self, _):
        \n return MagicMock()

    def FcApi(self, _):
        \n return MagicMock()

    def HcApi(self, _):
        \n return MagicMock()

    def IrApi(self, _):
        \n return MagicMock()

    def ProbeApi(self, _):
        \n return MagicMock()

    def MscApi(self, _):
        \n return MagicMock()

    def RgbApi(self, _):
        \n return MagicMock()

    def Scan3dApi(self, _):
        \n return MagicMock()

    def ScalesApi(self, _):
        \n return MagicMock()

    def SprayApi(self, _):
        \n return MagicMock()

    def SpectrumDeviceApi(self, _):
        \n return MagicMock()

    def BufferApi(self, _):
        \n return MagicMock()

    def SystemLogApi(self, _):
        \n return MagicMock()

    def FileApi(self, _):
        \n return MagicMock()

    def VersionInfoApi(self, _):
        \n return MagicMock()


class ExpMock():
    def __init__(self):
        self.experiment_id = MagicMock(\n return_value=replies.experiment.MOCK_EXPERIMENT_ID_REPLY)
        self.experiment = MagicMock(\n return_value=replies.experiment.MOCK_EXPERIMENT_REPLY)
        self.experiment_date = MagicMock(\n return_value=replies.experiment.MOCK_EXPERIMENT_DATE_REPLY)
        self.experiment_owner = MagicMock(\n return_value=replies.experiment.MOCK_EXPERIMENT_OWNER_REPLY)
        self.owner_id = MagicMock(\n return_value=replies.experiment.MOCK_OWNER_ID_REPLY)
        self.owner = MagicMock(\n return_value=replies.experiment.MOCK_OWNER_REPLY)
        self.note_experiment = MagicMock(\n return_value=replies.experiment.MOCK_NOTE_EXPERIMENT_REPLY)