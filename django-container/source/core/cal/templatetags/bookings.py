import calendar
import datetime

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def filtered_bookings(context, all_bookings, day, weekday):
    """
    Takes queryset of bookings for the month and filters down to bookings for specific day
    """
    if day > 0:
        calendar_date = context['calendar_date']
        date = datetime.date(calendar_date.year, calendar_date.month, day)
        days_bookings = all_bookings.filter(start__lte=date, end__gte=date).extra(where=['%s IS TRUE' % (calendar.day_name[weekday].lower())])
        return days_bookings.order_by('project__client', 'project')
    else:
        return None
