from dataclasses import dataclass


@dataclass(frozen=True)
class UserRegistrationDTO:
    email: str
    password: str
    repeat_password: str

    @staticmethod
    def from_dict(payload: dict) -> "UserRegistrationDTO":
        return UserRegistrationDTO(
            email=str(payload.get("email", "")).strip(),
            password=str(payload.get("password", "")),
            repeat_password=str(payload.get("repeat_password", "")),
        )

