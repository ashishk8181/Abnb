import calendar
from django.utils import timezone

class Day:
    def __init__(self, day, year, month, past):
        self.day = day
        self.year = year
        self.month = month
        self.past = past
    
    def __str__(self) -> str:
        return str(self.day)

class Calendar(calendar.Calendar):
    def __init__(self, year, month):
        super().__init__(firstweekday=6)
        self.year = year
        self.month = month
        self.day_names = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
        self.months = ('January', 'February', 'March', 'April', 'May', 'June',\
                     'July', 'August', 'September', 'October', 'November', 'December')

    def get_days(self):
        weeks = self.monthdays2calendar(self.year, self.month)
        days = []
        for week in weeks:
            for day, _ in week:
                now = timezone.localtime(timezone.now())
                today = now.day
                month = now.month
                past = False
                if month == self.month:
                    if day <= today:
                        past = True
                new_day = Day(day=day, past=past, month=self.month, year=self.year)
                print(now)
                days.append(new_day)
        return days

    def get_month(self):
        return self.months[self.month-1]