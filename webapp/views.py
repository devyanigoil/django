from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar

def index(request,year):
    year = int(year)
    #month = int(month)
    if year<1900 or year>2099:
        year=date.today().year
    #month_name = calendar.month_name[month]
    title = "Calendar - %s" %(year)
    cal2 = HTMLCalendar().formatmonth(year,1)
    cal3 = HTMLCalendar().formatmonth(year,2)
    cal4 = HTMLCalendar().formatmonth(year,3)
    cal5 = HTMLCalendar().formatmonth(year,4)
    cal6 = HTMLCalendar().formatmonth(year,5)
    cal7 = HTMLCalendar().formatmonth(year,6)
    cal8 = HTMLCalendar().formatmonth(year,7)
    cal9 = HTMLCalendar().formatmonth(year,8)
    cal10 = HTMLCalendar().formatmonth(year,9)
    cal11 = HTMLCalendar().formatmonth(year,10)
    cal12 = HTMLCalendar().formatmonth(year,11)
    cal1 = HTMLCalendar().formatmonth(year,12)

    return HttpResponse("<h1>%s</h1><p>%s %s %s %s %s %s %s %s %s %s %s %s"%(title,cal2,cal3,cal4,cal5,cal6,cal7,cal8,cal9,cal10,cal11,cal12,cal1))
# Create your views here.
