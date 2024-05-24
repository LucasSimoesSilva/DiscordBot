import datetime


def time_until(date) -> str:
    target_date = f"{date} 00:00:00"

    formatted_date = datetime.datetime.strptime(target_date, "%d-%m-%Y %H:%M:%S")
    current_date = datetime.datetime.now()

    date_diference = formatted_date - current_date

    days = date_diference.days
    seconds = date_diference.seconds
    hours = int(seconds / 3600)
    minutes = int((seconds - hours * 3600) / 60)
    seconds = seconds - hours * 3600 - minutes * 60

    if str(datetime.date.today()).__eq__(f'{formatted_date.date()}'):
        return '`HAPPY BIRTHDAY`'
    elif int(days) < 0:
        return f'{int(days)*-1} days, {hours} hours, {minutes} minutes, {seconds} seconds after your birthday'
    return f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds left until your birthday'
