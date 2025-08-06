from flask import Flask

from patient_handler.database.domain.database import get_engine, load_all
from patient_handler.api.endpoints import blueprint as endpoints_blueprint
from patient_handler.api.pages import blueprint as pages_blueprint
from patient_handler.database.domain.models.db_patient import DBPatient  # type: ignore # noqa

app = Flask(__name__, template_folder="templates")

app.register_blueprint(endpoints_blueprint)
app.register_blueprint(pages_blueprint)

engine = get_engine()
load_all(engine)
