def add_time(start, duration, day='monday'):
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

    sum_hours_in_minutes = sum_hours * 60
    sum_total_minutes = sum_hours_in_minutes + sum_minutes

    def updated_period(am_or_pm):
        if am_pm == 'PM' and (sum_total_minutes // 720) % 2 == 0:
            period = 'PM'
        elif am_pm == 'AM' and (sum_total_minutes // 720) % 2 == 1:
            period = 'PM'
        else:
            period = 'AM'
        return period

    updated_am_pm = updated_period(am_pm)

    new_time = f'{str(final_hour_format)}:{str(final_minute_format)} {updated_am_pm}'

    return new_time
