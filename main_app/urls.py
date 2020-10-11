from django.urls import path
from . import views

urlpatterns = [
  path('', views.landing, name='landing'),
  path('stands/', views.stands_index, name='index'),
]