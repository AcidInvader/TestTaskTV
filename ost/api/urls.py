from django.urls import path, include


urlpatterns = [
    path('', include('api.auth_app.urls')),
    path('', include('api.blog.urls')),
]