thonfrom datetime import datetime

def format_duration(seconds):
    return str(datetime.timedelta(seconds=seconds))

def parse_duration(duration):
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds