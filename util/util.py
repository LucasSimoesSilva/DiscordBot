import datetime


def time_until(date: datetime.date, user_id) -> str:
    now = datetime.datetime.now()

    if date == now.date():
        if user_id is not None:
            return f'`HAPPY BIRTHDAY` <@{user_id}>!'
        return f'`HAPPY BIRTHDAY`'

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


def convert_date_to_sort(date: str):
    d = datetime.datetime.strptime(date, "%d-%m")
    return datetime.date(2000, d.month, d.day)