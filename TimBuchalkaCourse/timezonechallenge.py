import datetime
import pytz

available_zones = {'1':"Africa/Tunis",
                   '2':"Asia/Kolcata",
                   '3':"Australia/Adelaide",
                   '4':"Europe/Brussels",
                   '5':"Europe/London"}

print("Please choose a timezone (or 0 to quit):")
for place in sorted(available_zones)