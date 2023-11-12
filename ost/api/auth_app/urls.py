from django.urls import path
from .views import SignInView

app_name = 'auth_app'

urlpatterns = [
    path('sign-in/', SignInView.as_view()),
]