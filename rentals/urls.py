from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet,BikeViewSet,CarViewSet,TruckViewSet,CustomerViewSet, car_list,rentalRecordViewSet,logout
from . import views


router= DefaultRouter()
router.register(r'owners',OwnerViewSet)
router.register(r'cars',CarViewSet)
router.register(r'bikes',BikeViewSet)
router.register(r'trucks',TruckViewSet)

urlpatterns = [
      path('api', include(router.urls)),
      path('',views.home, name='home' ),
      path('signup/',views.signup, name='signup' ),
      path('login/',views.login_user, name='login' ),
      path('addCar/',views.addCar, name='addCar' ),
      path('cars/', car_list, name='car_list'),
      path('logout/', views.logout_user, name='logout'),
      path('add_owner_profile/', views.add_owner_profile, name='add_owner_profile'),
      path('owner_dashboard/', views.dashboard,name='dashboard'),
      path('addBike/',views.add_bike, name='addBike' ),
      path('addTruck/',views.add_truck, name='addTruck' ), 
      path('vehicles/', views.vehicle_list, name='vehicle_list'),
      path('booking_ride/', views.book_ride,name='book_ride'),
      path('user_dashboard/', views.user_dashboard,name='user_dashboard'),     
]
