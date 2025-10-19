from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Root URL view
def home(request):
    return JsonResponse({"message": "Welcome to Prodigy Hotel Booking API"})

urlpatterns = [
    path('', home, name='home'),  # Root URL
    path('admin/', admin.site.urls),  # Admin panel
    path('api/', include('bookings.urls')),  # All app APIs
]
