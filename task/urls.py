from django.urls import path

from . import views

app_name = 'task'

urlpatterns = [
    path('create/', views.create_task, name="create_task"),
    path('update/', views.update_task, name="update_task"),
]
