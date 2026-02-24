import json

from django.http import HttpRequest, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from apps.users.application.dto.user_registration_dto import UserRegistrationDTO
from apps.users.application.exceptions import DomainValidationError
from apps.users.application.services.user_registration_service import UserRegistrationService
from apps.users.infrastructure.repositories.django_user_repository import DjangoUserRepository


@method_decorator(csrf_exempt, name="dispatch")
class UserRegistrationController(View):
    http_method_names = ["post", "options"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        user_repository = DjangoUserRepository()
        self.user_registration_service = UserRegistrationService(user_repository)

    def options(self, request: HttpRequest, *args, **kwargs):
        return JsonResponse({}, status=204)

    def post(self, request: HttpRequest, *args, **kwargs):
        try:
            payload = json.loads(request.body or "{}")
        except json.JSONDecodeError:
            return JsonResponse(
                {"success": False, "message": "Invalid JSON payload."},
                status=400,
            )

        dto = UserRegistrationDTO.from_dict(payload)

        try:
            created_user = self.user_registration_service.register(dto)
        except DomainValidationError as exc:
            return JsonResponse(
                {"success": False, "errors": exc.errors},
                status=400,
            )

        return JsonResponse(
            {"success": True, "data": created_user},
            status=201,
        )

