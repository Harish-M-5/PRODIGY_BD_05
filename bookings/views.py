from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import HotelRoom, Booking
from .serializers import HotelRoomSerializer, BookingSerializer
from .permissions import IsOwnerOrReadOnly
from .utils import calculate_total_price
from datetime import datetime

class HotelRoomViewSet(viewsets.ModelViewSet):
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'], url_path='search')
    def search_rooms(self, request):
        check_in = request.query_params.get('check_in')
        check_out = request.query_params.get('check_out')

        rooms = HotelRoom.objects.filter(is_available=True)

        if check_in and check_out:
            try:
                check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
                check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()
            except ValueError:
                return Response(
                    {"error": "Invalid date format. Use YYYY-MM-DD"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            booked_rooms = Booking.objects.filter(
                check_in__lt=check_out_date, check_out__gt=check_in_date
            ).values_list('room_id', flat=True)
            rooms = rooms.exclude(id__in=booked_rooms)

        serializer = HotelRoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        room = serializer.validated_data['room']
        check_in = serializer.validated_data['check_in']
        check_out = serializer.validated_data['check_out']

        overlapping = Booking.objects.filter(
            room=room,
            check_in__lt=check_out,
            check_out__gt=check_in
        ).exists()

        if overlapping:
            raise serializers.ValidationError("Room is already booked for this date range.")

        total_price = calculate_total_price(room.price_per_night, check_in, check_out)
        serializer.save(user=self.request.user, total_price=total_price)

    @action(detail=False, methods=['post'], url_path='reserve')
    def reserve_room(self, request):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
