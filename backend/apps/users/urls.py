from django.urls import path

from apps.users.presentation.controllers.user_registration_controller import UserRegistrationController

urlpatterns = [
    path("register/", UserRegistrationController.as_view(), name="users-register"),
]

