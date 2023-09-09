from django.urls import path
from tasks.views import task_list, create_task, update_task, delete_task, export_csv, export_json, register, login, \
    logout_view

urlpatterns = [
    path('', task_list, name='task-list'),
    path('task/create/', create_task, name='task-create'),
    path('task/<int:task_id>/update/', update_task, name='task-update'),
    path('task/<int:task_id>/delete/', delete_task, name='task-delete'),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('task/logout/', logout_view, name="logout"),
    path('export-csv/', export_csv, name='export-csv'),
    path('export-json/', export_json, name='export-json'),
]