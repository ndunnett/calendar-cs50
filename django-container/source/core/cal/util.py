from django.urls import reverse
from django.forms import DateInput

from . import models


class CustomDateInput(DateInput):
    input_type = 'date'

    def __init__(self, attrs=None, format=None):
        super().__init__(attrs)
        self.format = format or '%Y-%m-%d'
