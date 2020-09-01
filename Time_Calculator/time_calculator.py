def add_time(start, duration):
    start_time, am_pm = start.split()
    start_hours, start_minutes = start_time.split(":")
    duration_hours, duration_minutes = duration.split(":")

    sum_hours = int(start_hours) + int(duration_hours)
    sum_minutes = int(start_minutes) + int(duration_minutes)

    hours_from_minutes = sum_minutes // 60

    final_hour = ((sum_hours - 12) if sum_hours >= 12 else sum_hours) + hours_from_minutes
    final_hour_format = (('0' + str(final_hour)) if len(str(final_hour)) == 1 else final_hour)

    final_minute = ((sum_minutes - 60) if sum_minutes >= 60 else sum_minutes)
    final_minute_format = (('0' + str(final_minute)) if len(str(final_minute)) == 1 else final_minute)

    if (int(start_hours) + int(duration_hours) + (sum_minutes / 60)) > 12:
        if am_pm == 'AM':
            period = 'PM'
        else:
            period = 'AM'
    else:
        period = am_pm

    new_time = f'{str(final_hour_format)}:{str(final_minute_format)} {period}'

    return new_time
