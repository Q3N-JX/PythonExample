
from datetime import datetime, timedelta, timezone
ID = timezone(timedelta(hours=+12))
dt = datetime(2021, 10, 15, 12, 0, 0, tzinfo=ID)
print(dt)
# 2021-10-15 12:00:00+09:00
print(dt.tzname())
# UTC+12:00
dt = datetime(2021, 10, 15, 12, 0, 0, tzinfo=timezone(timedelta(hours=9), 'ID'))
print(dt.tzname)
