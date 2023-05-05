import logging
from email.utils import parseaddr
from enum import Enum
from typing import Any

log = logging.getLogger(__name__)

ValResponse = tuple[bool, str]
class ValidatorType(Enum):
    NAME = "name"
    EMAIL = "email"
    PASSWORD = "password" 


class ValidationValueMissingError(Exception):
    pass


def validate_wholesale(type_map: dict[str, ValidatorType], 
                       value_map: dict[str, Any]) -> dict[str, str]:
    """Validates lots of fields at once.
    :param type_map: Example: {"first_name": "name"}
    :param value_map: Example: {"first_name": "Ignatius"}

    It is not neccessary that all keys in value_map be present
    in type_map - we simply ignore validation for these. However,
    the converse is not true.

    :raises ValidationValueMissingError: raised if a field given in
        type_map is missing from value_map

    :return: A dict mapping field names to error messages. Wil be 
        empty if there are no validation errors.
    """
    errors = {}
    for field_name in type_map:
        if field_name not in value_map:
            raise ValidationValueMissingError()

        fval, ftype = value_map[field_name],  type_map[field_name] 
        valid, msg = validate_field(fval, ftype)

        # issue a warning if the type is invalid (see validate_field)
        if valid and msg:
            log.warn(f"Invalid type for field {field_name}: {ftype}")
        elif not valid:
            errors[field_name] = msg

    return errors
     

def validate_field(value, inp_type) -> ValResponse:
    if inp_type == "email":
        return validate_email(value)
    elif inp_type == "password":
        return validate_password(value)
    elif inp_type == "name":
        return validate_name(value)
    
    return (True, f"warning: invalid validation type {inp_type}")

    

def validate_email(email) -> ValResponse:
    """Validates an email address.

    :return: (valid: bool, err_msg: str) tuple
    """
    name, addr = parseaddr(email)
    valid_addr = addr and "@" in addr
    if not valid_addr:
        return (False, "Invalid Email")
    return (True, "")


def validate_password(password) -> ValResponse:
    if len(password) < 8:
        return (False, "The password is too short")
    return (True, "")

def validate_name(first_name) -> ValResponse:
    if not first_name:
        return (False, "This field cannot be empty")
        
    return (True, "")

