from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Experiment:
    """Experiment baseclass"""
    created_date: str
    experiment_id: int
    experiment_info: str
    experiment_mame: str
    experiment_status: str
    owner_id: int
    status_changed_date: str

    @staticmethod
    def from_dict(obj: Any) -> Experiment:
        return Experiment(
            created_date=obj.get("CreatedDate"),
            experiment_id=obj.get("ExperimentID"),
            experiment_info=obj.get("ExperimentInfo"),
            experiment_mame=obj.get("ExperimentName"),
            experiment_status=obj.get("ExperimentStatus"),
            owner_id=obj.get("OwnerID"),
            status_changed_date=obj.get("StatusChangedDate")
        )


@dataclass
class Owner:
    """Owner baseclass"""
    created_date: str
    email: str
    first_name: str
    last_failed_date: str
    last_name: str
    last_success_login: str
    login: str
    owner_id: int
    sms_phone_number: str

    @staticmethod
    def from_dict(obj: Any) -> Owner:
        return Owner(
            created_date=obj.get("CreatedDate"),
            email=obj.get("Email"),
            first_name=obj.get("FirstName"),
            last_failed_date=obj.get("LastFailedDate"),
            last_name=obj.get("LastName"),
            last_success_login=obj.get("LastSuccessLogin"),
            login=obj.get("Login"),
            owner_id=obj.get("OwnerID"),
            sms_phone_number=obj.get("SmsPhoneNumber")
        )


@dataclass
class Note:
    """Note baseclass"""
    note_id: int
    owner_id: int
    experiment_id: int
    note_created_date: str
    note_text: str

    @staticmethod
    def from_dict(obj: Any) -> Note:
        return Note(
            note_id=obj.get("NoteID"),
            owner_id=obj.get("OwnerID"),
            experiment_id=obj.get("ExperimentID"),
            note_created_date=obj.get("NoteCreatedDate"),
            note_text=obj.get("NoteText"),
        )


@dataclass
class ExperimentIDs:
    """"List experiments"""

    @staticmethod
    def from_dict(obj: Any) -> List[int]:
        if obj.get("JsonExperimentIDResult") is None:
            return []        
        _ids = [int(y.get("ExperimentID")) for y in obj.get("JsonExperimentIDResult")]
        return _ids


@dataclass
class ExperimentWrapper:
    """Experiment by ID (experiment wrapper, JSON result is not list)"""

    @staticmethod
    def from_dict(obj: Any) -> Experiment:
        if obj.get("JsonExperimentResult") is None:
            return None
        return Experiment.from_dict(obj.get("JsonExperimentResult"))


@dataclass
class ExperimentDate:
    """List experiments in period"""

    @staticmethod
    def from_dict(obj: Any) -> List[Experiment]:
        if obj.get("JsonExperimentByDateResult") is None:
            return []
        return [Experiment.from_dict(y) for y in obj.get("JsonExperimentByDateResult")]


# List experiments by owner
class ExperimentOwner:
    Experiments: List[Experiment]

    @staticmethod
    def from_dict(obj: Any) -> 'ExperimentOwner':
        if obj.get("JsonExperimentByOwnerResult") is None:
            return []     
        return [Experiment.from_dict(y) for y in obj.get("JsonExperimentByOwnerResult")]


@dataclass
class OwnerID:
    """List experiment owner ids"""

    @staticmethod
    def from_dict(obj: Any) -> List[Experiment]:
        if obj.get("JsonOwnerIDResult") is None:
            return []
        return [y.get('OwnerID') for y in obj.get("JsonOwnerIDResult")]


@dataclass
class OwnerWrapper:
    """Owner by ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[Owner]:
        if obj.get("JsonOwnerResult") is None:
            return []
        return [Owner.from_dict(y) for y in obj.get("JsonOwnerResult")]


@dataclass
class NoteExperiment:
    """List experimental notes"""

    @staticmethod
    def from_dict(obj: Any) -> List[Note]:
        if obj.get("JsonNoteResult") is None:
            return []
        return [NoteExperiment.from_dict(y) for y in obj.get("JsonNoteResult")]
