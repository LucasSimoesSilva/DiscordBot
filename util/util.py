import datetime


def time_until(date: datetime.date) -> str:
    now = datetime.datetime.now()

    if date == now.date():
        return '`HAPPY BIRTHDAY`'

    target = datetime.datetime.combine(date, datetime.time.min)

    delta = target - now

    days = abs(delta.days)
    seconds = abs(delta.seconds)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    if delta.total_seconds() < 0:
        return f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds after your birthday'

    return f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds left until your birthday'
