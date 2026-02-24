from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import validate_email


def validate_email_value(email: str) -> str | None:
    if not email:
        return "Email is required."

    try:
        validate_email(email)
    except DjangoValidationError:
        return "Invalid email format."

    return None


def validate_password_value(password: str) -> str | None:
    if not password:
        return "Password is required."

    try:
        validate_password(password)
    except DjangoValidationError as exc:
        return " ".join(exc.messages)

    return None

