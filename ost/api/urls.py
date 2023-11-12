from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('', include('api.auth_app.urls')),
    path('', include('api.blog.urls')),
]
