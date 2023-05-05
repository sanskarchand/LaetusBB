from dataclasses import dataclass
from enum import Enum
from typing import List, Any

class FieldType(Enum):
    TEXT = "text"
    EMAIL = "email"
    PASSWORD = "password"
    TELEPHONE = "telephone"
    SUBMIT = "SUBMIT"
    CHECKBOX = "CHECKBOX"

    # To be implemented later
    DATE = "DATE"

@dataclass
class FieldConfig:
    name: str
    class: str
    id: str
    type: FieldType

    attribs: dict[str, Any]     # extra attribs
