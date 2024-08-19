from django.urls import path

from . import views


urlpatterns = [
    path('apply/', views.applyForApplication.as_view()),
    path('applications/', views.GetApplications.as_view()),
]

