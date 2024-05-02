from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index, name='index'),
    path('add_userprofile/', views.add_userprofile, name='add_userprofile'),
    path('customer_profile/', views.CustomerProfileView.as_view(), name='customer_profile'),
    path('seller_profile/', views.SellerProfileView.as_view(), name='seller_profile'),
    path('services/', views.service_list, name='service-list'),
    path('services/<int:pk>/', views.service_detail, name='service-detail'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('add_nextappointment/', views.add_nextappointment, name='add_nextappointment'),
    path('', views.test_view, name='test'),
    path('service_test', views.services_test_view, name='test'),


]