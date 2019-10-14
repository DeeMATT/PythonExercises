import time

import snaps

current_time = time.localtime()

hour = current_time.tm_hour
minute = current_time.tm_min
week_day = current_time.tm_wday
daysof_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

if week_day NOT IN daysof_week:
