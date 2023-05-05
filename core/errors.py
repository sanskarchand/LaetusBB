from collections import namedtuple

Error = namedtuple("Error", "status_code int_code msg")


ERR_EMAIL_EXISTS = Error(409, "ERR_EMAIL_EXISTS", "This email is already in use")
ERR_CREDENTIALS_WRONG = Error(400, "ERR_CREDENTIALS_WRONG", "Wrong email or password")
ERR_UNAUTHORIZED_ACCESS = Error(401, "ERR_UNAUTHORIZED_ACCESS", "You are not authorized to acccess this resource")
ERR_SERVER_ERROR = Error(500, "ERR_SERVER_ERROR", "Server error")
ERR_VALIDATION_ERROR = Error(422, "ERR_VALIDATION_ERROR", "Some inputs are invalid")
