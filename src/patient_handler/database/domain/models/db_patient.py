from sqlalchemy import Boolean, Integer, String, DateTime
from sqlalchemy.orm import Mapped, MappedColumn
from datetime import datetime
from patient_handler.database.domain.database import BASE


class DBPatient(BASE):
    __tablename__ = "patients"
    id: Mapped[int] = MappedColumn(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = MappedColumn(String(100), nullable=False)
    age: Mapped[int] = MappedColumn(Integer, nullable=False)
    area: Mapped[str] = MappedColumn(String(50), nullable=False)
    active: Mapped[bool] = MappedColumn(Boolean, nullable=False, default=True)
    deleted: Mapped[bool] = MappedColumn(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = MappedColumn(
        DateTime, nullable=False, default=datetime.utcnow
    )
