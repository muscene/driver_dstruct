from django.urls import path
from . import views
app_name = 'car_tracking'
urlpatterns = [
    # Owner views
    path('owners/', views.OwnerListView.as_view(), name='owner-list'),
    path('owners/<int:pk>/', views.OwnerDetailView.as_view(), name='owner-detail'),

    # Car views
    path('cars/', views.CarListView.as_view(), name='car-list'),
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car-detail'),

    # Driver Profile view
    path('driver-profile/<int:pk>/', views.DriverProfileView.as_view(), name='driver-profile'),
]
