hour = int(input('Starting time (hours): '))
min = int(input('Starting time (minutes): '))
duration = int(input('Event duration (minutes): '))

minutes = min + duration
hour_calc = minutes // 60
min_calc = minutes % 60

event_start = str(hour) + ":" + str(min)
event_end = str(hour + hour_calc) + ":" + str(min_calc)

print(event_start)
print(event_end)