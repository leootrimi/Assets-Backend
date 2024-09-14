from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.addEmployers, name = 'add' ),
    path('get/', views.getEmployers, name = 'get' ),
    path('getname/', views.getEmployersData, name = 'options'),
    path('<int:id>/', views.getEmployerById, name= 'getByID'),
]
