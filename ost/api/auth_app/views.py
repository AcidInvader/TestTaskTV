from rest_framework.response import Response

from . import serializers
from rest_framework.generics import GenericAPIView
from .services import SignInService


class SignInView(GenericAPIView):
    permission_classes = ()
    serializer_class = serializers.SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = SignInService(request)
        user = service.authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        print(user)
        token = service.login(user)
        return Response({"token": token})
