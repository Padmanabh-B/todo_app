from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('task_list/', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
]