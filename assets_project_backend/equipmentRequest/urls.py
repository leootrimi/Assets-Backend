from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addRequest, name='add'),
    path('get/', views.getRequests, name='get'),
    path('get/<str:status>/', views.getByStatus, name='status'),
    path('approve/<int:id>/', views.approve_request, name='approve'),
    path('reject/<int:id>/', views.reject_request, name='reject'),
]
