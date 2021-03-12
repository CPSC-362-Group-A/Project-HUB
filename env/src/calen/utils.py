from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        self.firstweekday = 6
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        '''
        expired_events = events.filter(end_time=datetime.now())
        for event in expired_events:
            event.delete()
'''     
        events_per_day = events.filter(start_time__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li> {event.get_html_url} </li>'
        '''if day == datetime.today():
            return f"<td><span class='active'>{day}</span></td>"'''
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
        calen = f'<table style="font-family:Brush Script MT, cursive; font-weight:bold" border="3" bgcolor="#e2ffec" bordercolor="#ffbe78" cellpadding="0" cellspacing="0" class="calendar">\n'
        calen += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        calen += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            calen += f'{self.formatweek(week, events)}\n'
        return calen

