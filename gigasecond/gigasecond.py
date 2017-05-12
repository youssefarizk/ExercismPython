import datetime

def add_gigasecond(instant):
    delta = datetime.timedelta(seconds = 10**9)
    return instant + delta

print (add_gigasecond(datetime.datetime.today()))