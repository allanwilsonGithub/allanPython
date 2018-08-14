import pytz
import datetime


country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {0} is {1}".format(country, local_time))
