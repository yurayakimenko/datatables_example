from datetime import datetime, timedelta

def parse_start_end(period):
    if period == 'week':
        end = datetime.now() + timedelta(hours=24)
        timedelta_val = timedelta(weeks=1)
        start = end - timedelta_val
    elif period == 'month':
        end = datetime.now() + timedelta(hours=24)
        timedelta_val = timedelta(days=30)
        start = end - timedelta_val
    elif period == 'hour':
        end = datetime.now()
        timedelta_val = timedelta(hours=1)
        start = end - timedelta_val
    elif period == '30min':
        end = datetime.now()
        timedelta_val = timedelta(hours=0.5)
        start = end - timedelta_val
    elif period == '15min':
        end = datetime.now()
        timedelta_val = timedelta(hours=0.25)
        start = end - timedelta_val
    else:
        if len(period.split("_")) < 2:
            end = datetime.strptime(period, "%d/%m/%Y") + timedelta(hours=24)
            timedelta_val = timedelta(hours=24)
            start = end - timedelta_val
        else:
            start_end = period.split("_")
            start = datetime.strptime(start_end[0], "%d/%m/%Y")
            end = datetime.strptime(start_end[1], "%d/%m/%Y") + timedelta(hours=24)
            timedelta_val = end - start
    return start, end
