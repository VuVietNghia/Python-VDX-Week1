import datetime
import time

while True:
    now = datetime.datetime.now()
    time_str = now.strftime('%H:%M:%S')

    # THÊM: flush=True để ép buộc in ra ngay lập tức
    print(f"Thời gian hiện tại: {time_str} ", end='\r', flush=True)

    time.sleep(1)