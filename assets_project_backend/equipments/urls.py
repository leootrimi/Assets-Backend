from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.addEquipment, name = 'add' ),
    path('get/', views.getEquipments, name = 'get' ),
    path('count/', views.count_equipment, name='count'),
    path('total/', views.total_equipment_price, name='total-price'),
    path('<str:serial_no>/', views.equipment_detail, name='equipment-detail'),
    path('count/<str:model>/', views.getCount, name='count-equipment'),

]
