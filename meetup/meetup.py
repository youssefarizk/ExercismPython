import calendar
import datetime

MeetupDayException = Exception

def meetup_day(year, month, day_, mode):
    
    dayToString = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }

    modeDic = {
        '1st': [datetime.date(year,month,day) for day in range(8)[1:]],
        '2nd': [datetime.date(year,month,day) for day in range(15)[8:]],
        '3rd': [datetime.date(year,month,day) for day in range(22)[15:]],
        '4th': [datetime.date(year,month,day) for day in range(29)[22:]],
        '5th': [datetime.date(year,month,day) for day in range(29)[29:] if day in range(calendar.monthrange(year,month)[1]+1)],
        'teenth': [datetime.date(year,month,day) for day in range(21)[10:]],
        'last': [datetime.date(year,month,day) for day in range(calendar.monthrange(year,month)[1]+1)[calendar.monthrange(year,month)[1]-6:]]
    }

    findDay = dayToString[day_]

    for i in modeDic[mode]:
        if i.weekday() == findDay:
            return i
    
    raise MeetupDayException

