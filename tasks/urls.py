from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('',views.index,name="index"),

    path('add-task/',views.add_task,name="task-add"),

    path('task/<int:pk>/view',views.task_view,name="task-view"),

    path('task/<int:pk>/edit/',views.edit_task,name='task-edit'),

    path('delete-task/<int:pk>/',views.task_delete,name="task-delete"),

    path('complete/tasks/',views.complete,name='complete'),

    path('incomplete/tasks/',views.incomplete,name='incomplete'),
    
]
