from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/<int:month>', views.MonthView.as_view(), name='month'),
    path('thismonth', views.this_month, name='thismonth'),
    path('bookings/new', views.BookingCreateView.as_view(), name='booking-create'),
    path('bookings/<int:pk>', views.BookingDetailView.as_view(), name='booking-detail'),
    path('bookings/<int:pk>/edit', views.BookingUpdateView.as_view(), name='booking-update'),
    path('bookings', views.BookingListView.as_view(), name='booking-list'),
    path('bookings/me', views.MyBookingsView.as_view(), name='booking-list-me'),
]
