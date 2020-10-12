from django.urls import path
from . import views

urlpatterns = [
  path('', views.landing, name='landing'),
  path('stands/', views.stands_index, name='index'),
  path('stands/create/', views.StandCreate.as_view(), name='stands_create'),
  path('stands/<int:stand_id>/', views.stands_detail, name='detail'),
  path('stands/<int:pk>/update/', views.StandUpdate.as_view(), name='stands_update'),
  path('stands/<int:pk>/delete/', views.StandDelete.as_view(), name='stands_delete'),
]