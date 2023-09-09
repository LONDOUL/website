from django.urls import path
from scripts_api.views import index

urlpatterns = [
    path('api/', index, name='films'),
]