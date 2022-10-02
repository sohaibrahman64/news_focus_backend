# To commit
def convert_to_datetime(date_time_str):
    from datetime import datetime
    date_time_obj = datetime.strptime(date_time_str, '%a, %d %b %Y %H:%M:%S GMT')
    return date_time_obj


# Commit 3
def format_datetime(date_time):
    from datetime import datetime
    date_time_obj = datetime.strftime(date_time, '%d %b')
    return date_time_obj
