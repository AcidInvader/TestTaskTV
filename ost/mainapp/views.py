from typing import TYPE_CHECKING
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView

if TYPE_CHECKING:
    from rest_framework.request import Request


class TemplateApiView(APIView):
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    template_name: str = ''

    def get(self, request: 'Request', *args, **kwargs):
        return Response()
