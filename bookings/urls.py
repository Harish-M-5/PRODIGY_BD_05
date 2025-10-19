from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelRoomViewSet, BookingViewSet
from .auth_views import RegisterView, LoginView

router = DefaultRouter()
router.register(r'rooms', HotelRoomViewSet, basename='rooms')
router.register(r'bookings', BookingViewSet, basename='bookings')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),

    path('', include(router.urls)),
]
