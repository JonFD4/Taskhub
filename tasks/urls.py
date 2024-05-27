# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.read_task, name='task_detail'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/update/<int:pk>/', views.update_task, name='update_task'),
    path('task/delete/<int:pk>/', views.delete_task, name='delete_task'),

    # Category urls
    path('category/', views.category_list, name='category_list'),
    path('create/', views.create_category, name='create_category'),
    path('<int:category_id>/update/', views.update_category, name='update_category'),
    path('category/<int:category_id>/delete/', views.delete_category, name='delete_category'),
]
