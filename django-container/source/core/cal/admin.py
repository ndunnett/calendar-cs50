from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from cal.models import *
from . import forms


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


admin.site.unregister(User)
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    inlines = (ProfileInline,)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['pk', 'resource', 'project', 'start', 'end', 'notes']
    list_filter = ['resource', 'project', 'start', 'end']
    search_fields = ['notes']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = forms.ProjectForm
    list_display = ['name', 'client']
    list_filter = ['client']
    search_fields = ['name']
