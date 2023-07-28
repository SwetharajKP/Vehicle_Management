from django.urls import path
from . import views

urlpatterns = [
    path('',views.vehicle_list,name='vehicle_list'),
    path('vehicle_detail/<int:vehicle_id>/',views.vehicle_detail,name='vehicle_detail'),
    path('vehicle_create/', views.vehicle_create, name='vehicle_create'),
    path('vehicle_update/<int:vehicle_id>/', views.vehicle_update, name='vehicle_update'),
    path('vehicle_delete/<int:vehicle_id>/', views.vehicle_delete, name='vehicle_delete'),
]