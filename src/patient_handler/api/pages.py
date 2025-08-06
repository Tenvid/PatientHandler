from flask import Blueprint, render_template, redirect

from patient_handler.database.domain.database import SessionLocal
from patient_handler.patients.infrastructure.sqlite_patient_repository import (
    SqlitePatientRepository,
)

blueprint = Blueprint("Pages", __name__)

repo = SqlitePatientRepository(SessionLocal())


@blueprint.get("/")
def index():
    return redirect("/patients/all")


@blueprint.get("/patients/all")
def show_all_patients():
    patients = repo.get_all_active()
    return render_template("base.html", patients=patients, first_link_active=True)


@blueprint.get("/patients/active")
def show_active_patients():
    patients = repo.get_by_active_status(True)
    return render_template("base.html", patients=patients, second_link_active=True)


@blueprint.get("/patients/inactive")
def show_inactive_patients():
    patients = repo.get_by_active_status(False)
    return render_template("base.html", patients=patients, third_link_active=True)


@blueprint.get("/patients/area/<area_name>")
def show_patients_by_area(area_name: str):
    patients = repo.get_by_area(area_name)
    return render_template("base.html", patients=patients, selected_area=area_name)


@blueprint.get("/patients/area/<area_name>/active")
def show_active_patients_by_area(area_name: str):
    patients = repo.get_by_area_and_status(area_name, True)
    return render_template(
        "base.html",
        patients=patients,
        selected_area=area_name,
        second_link_active=True,
    )


@blueprint.get("/patients/area/<area_name>/inactive")
def show_inactive_patients_by_area(area_name: str):
    patients = repo.get_by_area_and_status(area_name, False)
    return render_template(
        "base.html",
        patients=patients,
        selected_area=area_name,
        third_link_active=True,
    )
