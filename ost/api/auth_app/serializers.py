from rest_framework import serializers



class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


