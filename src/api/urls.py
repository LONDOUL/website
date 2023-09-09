from django.urls import path
from api.views import hello_word, ListStudents, planet_list, display_data

urlpatterns = [
    path('rest-api/', hello_word),
    path('planets/', display_data),
    path('students/', ListStudents.as_view(), name='list-students')
]