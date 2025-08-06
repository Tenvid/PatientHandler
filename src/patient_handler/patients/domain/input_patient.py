from typing import Dict
from dataclasses import dataclass


@dataclass
class InputPatient:
    name: str
    age: int
    area: str
    active: bool = True
    deleted: bool = False
    id: int = 0

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def delete(self):
        self.deleted = True

    def dump(self) -> Dict[str, str | bool | int]:
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "area": self.area,
            "active": self.active,
            "deleted": self.deleted,
        }
