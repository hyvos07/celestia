from datetime import datetime

def time_ago(target_time_str):
    created_time = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S.%f")
    now = datetime.now()
    
    diff = now - created_time

    days = diff.days
    seconds = diff.seconds

    if days > 365:
        time_unit = 'years'
    elif days > 30:
        time_unit = 'months'
    elif days > 6:
        time_unit = 'weeks'
    elif days > 0:
        time_unit = 'days'
    elif seconds // 3600 > 0:
        time_unit = 'hours'
    elif seconds // 60 > 0:
        time_unit = 'minutes'
    else:
        time_unit = 'seconds'

    if time_unit == 'years':
        years = days // 365
        return 'a year' if years == 1 else f'{years} years'
    elif time_unit == 'months':
        months = days // 30
        return 'a month' if months == 1 else f'{months} months'
    elif time_unit == 'weeks':
        weeks = days // 7
        return 'a week' if weeks == 1 else f'{weeks} weeks'
    elif time_unit == 'days':
        return 'a day' if days == 1 else f'{days} days'
    elif time_unit == 'hours':
        hours = seconds // 3600
        return 'an hour' if hours == 1 else f'{hours} hours'
    elif time_unit == 'minutes':
        minutes = seconds // 60
        return 'a minute' if minutes == 1 else f'{minutes} minutes'
    else:
        return 'a second' if seconds == 1 else f'{seconds} seconds'

if __name__ == "__main__":
    date_str = "2023-12-31 23:59:59.999999" # Example date
    print(time_ago(date_str))