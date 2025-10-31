from datetime import datetime, timedelta
import random

def random_datetime(start: datetime, end: datetime) -> datetime:
    if start > end:
        start, end = end, start
    delta = end - start

    rand_seconds = random.randrange(int(delta.total_seconds()) + 1)
    return start + timedelta(seconds=rand_seconds)

start = datetime(2023, 1, 1, 0, 0, 0)
end   = datetime(2025, 12, 31, 23, 59, 59)
dt = random_datetime(start, end)
print(dt)