import datetime
import time

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def sleep_in_time_range(start,end, sleep_len= 600):
    now = datetime.datetime.now()
    nowt = now.time()
    while time_in_range(start, end, nowt):
        now = datetime.datetime.now()
        nowt = now.time()
        print(nowt,'zzzz')
        time.sleep(sleep_len)
