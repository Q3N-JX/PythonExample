
from datetime import datetime
from dateutil import tz
local = tz.gettz() # Local time
PT = tz.gettz('ID/Jakarta') # Jakarta Time
dt_l = datetime(2021, 10, 15, 12, tzinfo=local) # ID
dt_pst = datetime(2021, 10, 15, 12, tzinfo=PT)
dt_pdt = datetime(2021, 10, 15, 12, tzinfo=PT)
print(dt_l)
# 2021-10-15 12:00:00+00:00
print(dt_pst)
# 2021-10-15 12:00:00
print(dt_pdt)
# 2021-10-15 12:00:00
