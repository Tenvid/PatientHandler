from typing import List, Optional
from sqlalchemy.orm import Session

from patient_handler.patients.domain.patient_repository import PatientRepository
from patient_handler.patients.domain.input_patient import InputPatient
from patient_handler.database.domain.models.db_patient import DBPatient


class SqlitePatientRepository(PatientRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, patient: InputPatient) -> InputPatient:
        db_patient = DBPatient(
            name=patient.name,
            age=patient.age,
            area=patient.area,
            active=patient.active,
            deleted=patient.deleted,
        )
        self.session.add(db_patient)
        self.session.commit()
        self.session.refresh(db_patient)

        return self._db_to_domain(db_patient)

    def get_by_id(self, patient_id: int) -> Optional[InputPatient]:
        db_patient = (
            self.session.query(DBPatient)
            .filter(DBPatient.id == patient_id, ~DBPatient.deleted)
            .first()
        )
        if db_patient:
            return self._db_to_domain(db_patient)
        return None

    def get_all_active(self) -> List[InputPatient]:
        db_patients = self.session.query(DBPatient).filter(~DBPatient.deleted).all()
        return [self._db_to_domain(patient) for patient in db_patients]

    def get_by_active_status(self, active: bool) -> List[InputPatient]:
        db_patients = (
            self.session.query(DBPatient)
            .filter(DBPatient.active == active, ~DBPatient.deleted)
            .all()
        )
        return [self._db_to_domain(patient) for patient in db_patients]

    def get_by_area(self, area: str) -> List[InputPatient]:
        db_patients = (
            self.session.query(DBPatient)
            .filter(DBPatient.area == area, ~DBPatient.deleted)
            .all()
        )
        return [self._db_to_domain(patient) for patient in db_patients]

    def get_by_area_and_status(self, area: str, active: bool) -> List[InputPatient]:
        db_patients = (
            self.session.query(DBPatient)
            .filter(
                DBPatient.area == area, DBPatient.active == active, ~DBPatient.deleted
            )
            .all()
        )
        return [self._db_to_domain(patient) for patient in db_patients]

    def get_all_areas(self) -> List[str]:
        areas = (
            self.session.query(DBPatient.area)
            .filter(~DBPatient.deleted)
            .distinct()
            .all()
        )
        return [area[0] for area in areas]

    def update(self, patient: InputPatient) -> InputPatient:
        db_patient = (
            self.session.query(DBPatient).filter(DBPatient.id == patient.id).first()
        )
        if db_patient:
            db_patient.name = patient.name
            db_patient.age = patient.age
            db_patient.area = patient.area
            db_patient.active = patient.active
            db_patient.deleted = patient.deleted
            self.session.commit()
            return self._db_to_domain(db_patient)
        raise ValueError(f"Patient with ID {patient.id} not found")

    def delete(self, patient_id: int) -> None:
        db_patient = (
            self.session.query(DBPatient).filter(DBPatient.id == patient_id).first()
        )
        if db_patient:
            db_patient.deleted = True
            self.session.commit()

    def _db_to_domain(self, db_patient: DBPatient) -> InputPatient:
        return InputPatient(
            id=db_patient.id,
            name=db_patient.name,
            age=db_patient.age,
            area=db_patient.area,
            active=db_patient.active,
            deleted=db_patient.deleted,
        )
