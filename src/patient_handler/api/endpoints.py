from flask import Blueprint, request, redirect

from patient_handler.database.domain.database import SessionLocal
from patient_handler.patients.domain.input_patient import InputPatient
from patient_handler.patients.infrastructure.sqlite_patient_repository import (
    SqlitePatientRepository,
)

blueprint = Blueprint("Endpoints", __name__)


@blueprint.post("/api/v1/patients")
def add_patient():
    name = request.form.get("name")
    age_str = request.form.get("age")
    area = request.form.get("area")

    if not all([name, age_str, area]):
        return "Todos los campos obligatorios son requeridos", 400

    try:
        age = int(age_str)
        if age < 0 or age > 150:
            return "La edad debe estar entre 0 y 150 años", 400
    except ValueError:
        return "La edad debe ser un número válido", 400

    patient = InputPatient(name=name, age=age, area=area)

    repo = SqlitePatientRepository(SessionLocal())
    try:
        _ = repo.add(patient)
    except Exception as e:
        return f"Error al crear paciente: {str(e)}", 400

    return redirect(request.referrer or "/patients/all")


@blueprint.post("/api/v1/patients/<int:patient_id>/activate")
def activate_patient(patient_id: int):
    repo = SqlitePatientRepository(SessionLocal())
    patient = repo.get_by_id(patient_id)

    if not patient:
        return "Paciente no encontrado", 404

    patient.activate()
    repo.update(patient)

    return redirect(request.referrer or "/patients/all")


@blueprint.post("/api/v1/patients/<int:patient_id>/deactivate")
def deactivate_patient(patient_id: int):
    repo = SqlitePatientRepository(SessionLocal())
    patient = repo.get_by_id(patient_id)

    if not patient:
        return "Paciente no encontrado", 404

    patient.deactivate()
    repo.update(patient)

    return redirect(request.referrer or "/patients/all")


@blueprint.post("/api/v1/patients/<int:patient_id>/delete")
def delete_patient(patient_id: int):
    repo = SqlitePatientRepository(SessionLocal())
    patient = repo.get_by_id(patient_id)

    if not patient:
        return "Paciente no encontrado", 404

    repo.delete(patient_id)

    return redirect(request.referrer or "/patients/all")
