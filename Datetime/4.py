
from datetime import datetime, timedelta
from dateutil import tz
JST = tz.tzoffset('JST', 9 * 3600) # 3600 seconds per hour
dt = datetime(2021, 10, 15, 12, 0, tzinfo=JST)
print(dt)
# 2021-10-15 12:00:00+09:00
print(dt.tzname)
