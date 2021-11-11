import datetime

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from cal.models import Profile
from cal.views import this_month


def home_view(request):
    # context = {"home_active": " active"}
    # return render(request, 'content/home.html', context)
    return redirect(this_month)


class MyDetailsUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "core/my_details.html"

    fields = ['first_name', 'last_name', 'email', 'mobile']

    def get_object(self, queryset=None):
        queryset = self.get_queryset().filter(user=self.request.user)
        obj = queryset.get()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_form(self):
        form = super().get_form()
        return form
    
    def get_success_url(self):
        return reverse('my_details')
