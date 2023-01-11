from django.urls import path 
from . import views
# from .views import api_home

urlpatterns = [
    # path('', views.api_home),
    path('api/v1/fruits', views.api_v1_fruits),
    path('api/v1/fruits/<int:id>', views.api_v1_fruits_getId),    
    path('api/v1/fruits/<int:id>/', views.api_v1_fruits_getId),    
    path('api/v1/fruits/<str:id>/', views.api_v1_fruits_getId),    
    path('api/v1/fruits/', views.api_v1_fruits)
]

