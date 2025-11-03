from datetime import datetime, timedelta
import random

def random_datetime(start: datetime, end: datetime) -> datetime:
    if start > end:
        start, end = end, start
    delta = end - start

    rand_seconds = random.randrange(int(delta.total_seconds()) + 1)
    return start + timedelta(seconds=rand_seconds)

# Hàm để nhập và kiểm tra định dạng ngày tháng
def input_datetime(prompt):
    while True:
        try:
            # Yêu cầu người dùng nhập theo định dạng cụ thể
            date_str = input(f"{prompt} (định dạng: YYYY-MM-DD HH:MM:SS): ")
            # Chuyển đổi chuỗi thành đối tượng datetime
            return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng YYYY-MM-DD HH:MM:SS")
            print("Ví dụ: 2023-01-01 00:00:00")

# Nhập thời gian bắt đầu và kết thúc từ người dùng
start = input_datetime("Nhập thời gian bắt đầu")
end = input_datetime("Nhập thời gian kết thúc")

dt = random_datetime(start, end)
print(f"\nThời gian ngẫu nhiên: {dt}")