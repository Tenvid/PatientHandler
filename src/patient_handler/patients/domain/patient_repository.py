from abc import ABC, abstractmethod
from typing import List, Optional
from patient_handler.patients.domain.input_patient import InputPatient


class PatientRepository(ABC):
    """Abstract base class for patient repository implementations."""

    @abstractmethod
    def add(self, patient: InputPatient) -> InputPatient:
        """Add a new patient to the repository."""
        pass

    @abstractmethod
    def get_by_id(self, patient_id: int) -> Optional[InputPatient]:
        """Get a patient by their ID."""
        pass

    @abstractmethod
    def get_all_active(self) -> List[InputPatient]:
        """Get all non-deleted patients."""
        pass

    @abstractmethod
    def get_by_active_status(self, active: bool) -> List[InputPatient]:
        """Get patients filtered by active status."""
        pass

    @abstractmethod
    def get_by_area(self, area: str) -> List[InputPatient]:
        """Get patients filtered by area."""
        pass

    @abstractmethod
    def get_by_area_and_status(self, area: str, active: bool) -> List[InputPatient]:
        """Get patients filtered by area and active status."""
        pass

    @abstractmethod
    def get_all_areas(self) -> List[str]:
        """Get all distinct areas."""
        pass

    @abstractmethod
    def update(self, patient: InputPatient) -> InputPatient:
        """Update an existing patient."""
        pass

    @abstractmethod
    def delete(self, patient_id: int) -> None:
        """Soft delete a patient."""
        pass
