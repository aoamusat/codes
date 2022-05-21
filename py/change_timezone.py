import datetime

tz = datetime.timezone(datetime.timedelta(hours=-3))
dia_hj = datetime.datetime.now(tz)
print(dia_hj.strftime('%a'), dia_hj)