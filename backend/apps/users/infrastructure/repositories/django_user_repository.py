from django.contrib.auth import get_user_model

from apps.users.domain.repositories.user_repository import UserRepository


class DjangoUserRepository(UserRepository):
    def __init__(self):
        self.user_model = get_user_model()

    def exists_by_email(self, email: str) -> bool:
        return self.user_model.objects.filter(email__iexact=email).exists()

    def create(self, email: str, password: str):
        return self.user_model.objects.create_user(email=email, password=password)

