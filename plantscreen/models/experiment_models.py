from dataclasses import dataclass
from typing import List
from typing import Any
import json

# Experiment baseclass
@dataclass
class Experiment:
    CreatedDate: str
    ExperimentID: int
    ExperimentInfo: str
    ExperimentName: str
    ExperimentStatus: str
    OwnerID: int
    StatusChangedDate: str

    @staticmethod
    def from_dict(obj: Any) -> 'Experiment':
        return Experiment(
            CreatedDate=obj.get("CreatedDate"),
            ExperimentID=obj.get("ExperimentID"),
            ExperimentInfo=obj.get("ExperimentInfo"),
            ExperimentName=obj.get("ExperimentName"),
            ExperimentStatus=obj.get("ExperimentStatus"),
            OwnerID=obj.get("OwnerID"),
            StatusChangedDate=obj.get("StatusChangedDate")
        )


# Owner baseclass
@dataclass
class Owner:
    CreatedDate: str
    Email: str
    FirstName: str
    LastFailedDate: str
    LastName: str
    LastSuccessLogin: str
    Login: str
    OwnerID: int
    SmsPhoneNumber: str

    @staticmethod
    def from_dict(obj: Any) -> 'Owner':
        return Owner(
            CreatedDate=obj.get("CreatedDate"),
            Email=obj.get("Email"),
            FirstName=obj.get("FirstName"),
            LastFailedDate=obj.get("LastFailedDate"),
            LastName=obj.get("LastName"),
            LastSuccessLogin=obj.get("LastSuccessLogin"),
            Login=obj.get("Login"),
            OwnerID=obj.get("OwnerID"),
            SmsPhoneNumber=obj.get("SmsPhoneNumber")
        )
    
# Note baseclass
@dataclass
class Note:
    NoteID: int
    OwnerID: int
    ExperimentID: int
    NoteCreatedDate: str
    NoteText: str

    @staticmethod
    def from_dict(obj: Any) -> 'Note':
        return Note(
            NoteID=obj.get("NoteID"),
            OwnerID=obj.get("OwnerID"),
            ExperimentID=obj.get("ExperimentID"),
            NoteCreatedDate=obj.get("NoteCreatedDate"),
            NoteText=obj.get("NoteText"),
        )



# List experiments
@dataclass
class ExperimentIDs:
    IDs: List[int]

    @staticmethod
    def from_dict(obj: Any) -> 'ExperimentIDs':
        _IDs = [int(y.get("ExperimentID")) for y in obj.get("JsonExperimentIDResult")]
        return ExperimentIDs(_IDs)


# Experiment by ID (experiment wrapper, JSON result is not list)
@dataclass
class ExperimentWrapper:
    Experiment: Experiment

    @staticmethod
    def from_dict(obj: Any) -> 'Experiment':
        return Experiment.from_dict(obj.get("JsonExperimentResult"))
    

# List experiments in period
@dataclass
class ExperimentDate:
    Experiments: List[Experiment]

    @staticmethod
    def from_dict(obj: Any) -> 'ExperimentDate':
        return [Experiment.from_dict(y) for y in obj.get("JsonExperimentByDateResult")]


# List experiments by owner
class ExperimentOwner:
    Experiments: List[Experiment]

    @staticmethod
    def from_dict(obj: Any) -> 'ExperimentOwner':
        return [Experiment.from_dict(y) for y in obj.get("JsonExperimentByOwnerResult")]


# List experiment owner ids
@dataclass
class OwnerID:
    Experiments: List[Experiment]

    @staticmethod
    def from_dict(obj: Any) -> 'OwnerID':
        return [y.get('OwnerID') for y in obj.get("JsonOwnerIDResult")]

# Owner by ID
@dataclass
class OwnerWrapper:
    Experiments: List[Owner]

    @staticmethod
    def from_dict(obj: Any) -> 'Owner':
        return [Owner.from_dict(y) for y in obj.get("JsonOwnerResult")]
    

# List experimental notes
@dataclass
class NoteExperiment:
    Experiments: List[Note]

    @staticmethod
    def from_dict(obj: Any) -> 'NoteExperiment':
        return [NoteExperiment.from_dict(y) for y in obj.get("JsonNoteResult")]
    

