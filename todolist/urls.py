from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [ 
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('create-task/', create_task, name='create_task'),
    path('status/<int:id>/', status, name='status'),
    path('delete/<int:id>/', delete, name='delete'),
    path('json/', show_json_by_id, name='show_json_by_id'),
    path('add/', create_task_ajax, name='create_task_ajax'),
]
