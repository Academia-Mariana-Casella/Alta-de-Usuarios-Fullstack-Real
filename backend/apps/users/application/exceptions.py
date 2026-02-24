class DomainValidationError(Exception):
    def __init__(self, errors: dict[str, str]):
        super().__init__("Domain validation failed")
        self.errors = errors

