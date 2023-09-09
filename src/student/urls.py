from django.urls import path
from .views import student, student_db, student_db_json, index

urlpatterns = [
    path('list/', student_db, name='students'),
    path('list/<int:id_student>/', student_db),
    path('json/', student_db_json),
    path('json/<int:id_student>/', student_db_json),
    path('', student, name='home'),
    path('data/', index, name='students-news'),
    path('data/<int:id_student>/', index, name='student-by-id'),
    path('<str:name>/', student),
]