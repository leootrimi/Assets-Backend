from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.addModel, name = 'add' ),
    path('get/', views.getModel, name = 'get' ),
    path('get/<str:type>/', views.getByType, name = 'getType' ),
    path('get/<str:model>/count/', views.getCount, name = 'count'),
]
