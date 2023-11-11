from django.urls import path

from .views import TemplateApiView


urlpatterns = [
    path('', TemplateApiView.as_view(template_name='index.html'), name='index'),
]
