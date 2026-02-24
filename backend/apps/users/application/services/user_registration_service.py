from apps.users.application.dto.user_registration_dto import UserRegistrationDTO
from apps.users.application.exceptions import DomainValidationError
from apps.users.domain.repositories.user_repository import UserRepository
from apps.users.domain.validators.user_registration_validator import (
    validate_email_value,
    validate_password_value,
)


class UserRegistrationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, dto: UserRegistrationDTO) -> dict:
        errors: dict[str, str] = {}

        email_error = validate_email_value(dto.email)
        if email_error:
            errors["email"] = email_error

        password_error = validate_password_value(dto.password)
        if password_error:
            errors["password"] = password_error

        if dto.password != dto.repeat_password:
            errors["repeat_password"] = "Passwords do not match."

        if not errors and self.user_repository.exists_by_email(dto.email):
            errors["email"] = "Email is already in use."

        if errors:
            raise DomainValidationError(errors)

        user = self.user_repository.create(dto.email, dto.password)
        return {
            "id": user.id,
            "email": user.email,
        }

