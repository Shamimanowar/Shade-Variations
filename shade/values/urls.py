from django.urls import path
from rest_framework import views
from . import views

urlpatterns = [
    path('shade/', views.ShadeListCreate.as_view()),
    path('shade/<id>/', views.ShadeRetrievUpdateDelete.as_view()),
]