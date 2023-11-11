# from typing import TYPE_CHECKING, Any
#
# from django.contrib.auth.base_user import BaseUserManager
#
# if TYPE_CHECKING:
#     from .models import UserType
#
#
# class UserManager(BaseUserManager):
#
#     def create_user(self, email: str, password: str, **extra_fields: Any) -> 'UserType':
#         _email: str = self.normalize_email(email)
#         user = self.model(email=_email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email: str, password: str, **extra_fields: Any) -> 'UserType':
#         extra_fields['is_staff'] = True
#         extra_fields['is_superuser'] = True
#         extra_fields['is_active'] = True
#         return self.create_user(email, password, **extra_fields)