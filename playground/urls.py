from django.urls import path
from . import views

#URLconfiguration mondule
urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.default),
    ]