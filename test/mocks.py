"""Example replies from the calls """
from unittest.mock import MagicMock
import replies


class SwaggerMock():
    def __init__(self):
        self.Configuration = MagicMock()
        self.ApiClient = MagicMock()

    def ExperimentApi(self, _):
        return ExpMock()

    def RoundApi(self, _):
        return MagicMock()

    def ActionApi(self, _):
        return MagicMock()

    def DeviceApi(self, _):
        return MagicMock()

    def ProfileApi(self, _):
        return MagicMock()

    def TrayApi(self, _):
        return MagicMock()

    def PlantApi(self, _):
        return MagicMock()

    def FcApi(self, _):
        return MagicMock()

    def HcApi(self, _):
        return MagicMock()

    def IrApi(self, _):
        return MagicMock()

    def ProbeApi(self, _):
        return MagicMock()

    def MscApi(self, _):
        return MagicMock()

    def RgbApi(self, _):
        return MagicMock()

    def Scan3dApi(self, _):
        return MagicMock()

    def ScalesApi(self, _):
        return MagicMock()

    def SprayApi(self, _):
        return MagicMock()

    def SpectrumDeviceApi(self, _):
        return MagicMock()

    def BufferApi(self, _):
        return MagicMock()

    def SystemLogApi(self, _):
        return MagicMock()

    def FileApi(self, _):
        return MagicMock()

    def VersionInfoApi(self, _):
        return MagicMock()


class ExpMock():
    def __init__(self):
        self.experiment_id = MagicMock(return_value=replies.experiment.MOCK_EXPERIMENT_ID_REPLY)
        self.experiment = MagicMock(return_value=replies.experiment.MOCK_EXPERIMENT_REPLY)
        self.experiment_date = MagicMock(return_value=replies.experiment.MOCK_EXPERIMENT_DATE_REPLY)
        self.experiment_owner = MagicMock(return_value=replies.experiment.MOCK_EXPERIMENT_OWNER_REPLY)
        self.owner_id = MagicMock(return_value=replies.experiment.MOCK_OWNER_ID_REPLY)
        self.owner = MagicMock(return_value=replies.experiment.MOCK_OWNER_REPLY)
        self.note_experiment = MagicMock(return_value=replies.experiment.MOCK_NOTE_EXPERIMENT_REPLY)