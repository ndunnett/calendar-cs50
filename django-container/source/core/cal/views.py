import datetime
import calendar

from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms
from .util import *
from core.util import *


def this_month(request):
    return redirect("month", year=datetime.date.today().year, month=datetime.date.today().month)


class MonthView(LoginRequiredMixin, ListView):
    model = models.Booking
    template_name = "calendar/month.html"
    
    def get_queryset(self):
        month_start = datetime.date(self.kwargs["year"], self.kwargs["month"], 1)
        month_end = month_start
        while month_end.month == month_start.month:
            month_end += datetime.timedelta(days=1)
        month_end -= datetime.timedelta(days=1)

        queryset = models.Booking.objects.none()
        for client in self.request.user.profile.clients.all():
            queryset |= models.Booking.objects.filter(start__lte=month_end, end__gte=month_start, project__client=client)
        return queryset.order_by('start')

    def get_context_data(self, **kwargs):
        month = self.kwargs["month"]
        year = self.kwargs["year"]
        html_calendar = calendar.HTMLCalendar()

        context = super().get_context_data(**kwargs)
        context["calendar_active"] = " active"
        context["calendar_date"] = datetime.date(year, month, 1)
        context["todays_date"] = datetime.date.today()
        context["previous_month"] = context["calendar_date"] - datetime.timedelta(days=28)
        context["next_month"] = context["calendar_date"] + datetime.timedelta(days=35)
        context["month_name"] = ' '.join([calendar.month_name[month], str(year)])
        context["week_header"] = mark_safe(html_calendar.formatweekheader())
        context["month"] = html_calendar.monthdays2calendar(year, month)
        return context


class BookingDetailView(LoginRequiredMixin, DetailView):
    model = models.Booking
    template_name = "calendar/booking_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["calendar_active"] = " active"
        return context


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = models.Booking
    template_name = "calendar/booking_create.html"

    fields = ['resource', 'project', 'notes', 'start', 'end', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["calendar_active"] = " active"
        return context

    def get_form(self):
        form = super().get_form()
        form.fields['start'].widget = CustomDateInput()
        form.fields['end'].widget = CustomDateInput()
        return form

    def get_success_url(self):
        return reverse("month", kwargs={'year': self.object.start.year, 'month': self.object.start.month})


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Booking
    template_name = "calendar/booking_update.html"

    fields = ['resource', 'project', 'notes', 'start', 'end', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["calendar_active"] = " active"
        return context

    def get_form(self):
        form = super().get_form()
        form.fields['start'].widget = CustomDateInput()
        form.fields['end'].widget = CustomDateInput()
        return form
    
    def get_success_url(self):
        return reverse("month", kwargs={'year': self.object.start.year, 'month': self.object.start.month})


class BookingListView(LoginRequiredMixin, ListView):
    model = models.Booking
    template_name = "calendar/booking_list.html"
    paginate_by = 20
    
    def get_queryset(self):
        queryset = models.Booking.objects.none()
        for client in self.request.user.profile.clients.all():
            queryset |= models.Booking.objects.filter(end__gte=datetime.date.today(), project__client=client)

        return queryset.order_by('start')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["calendar_active"] = " active"
        context["pagination_range"] = context["paginator"].get_elided_page_range(number=context["page_obj"].number, on_each_side=1, on_ends=1)
        return context


class MyBookingsView(BookingListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(resource=self.request.user.profile)
