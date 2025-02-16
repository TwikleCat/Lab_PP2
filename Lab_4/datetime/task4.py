from datetime import datetime, time

def diff(dt2, dt1):
    timedelta=dt2-dt1
    return timedelta.days*24*3600+timedelta.seconds

date1 = datetime.strptime('2025-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()

print(diff(date2, date1))