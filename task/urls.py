from django.urls import path

from project.urls import home

from . import views

app_name = 'task'

urlpatterns = [
    path('create/', views.create_task, name="create_task"),
    path('', home, name="home"),
    path('update/<int:id>', views.update_task, name="update_task"),
    path('delete/<int:id>', views.delete_task, name="delete_task"),
]
