from django.contrib.auth import authenticate, login
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token


class SignInService:

    def __init__(self, request):
        self.request = request

    def authenticate(self, username: str, password: str):
        user = authenticate(request=self.request, username=username, password=password)
        if not user:
            raise ValidationError({"detail": "Invalid username or password"})
        return user

    def login(self, user):
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        return token.key
