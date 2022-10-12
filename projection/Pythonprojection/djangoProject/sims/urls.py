from django.urls import path
from sims import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('edit/', views.edit),
    path('delete/', views.delete),
    path('search/', views.search),
]
