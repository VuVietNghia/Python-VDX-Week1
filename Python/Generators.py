# Ví dụ: list comprehension tạo ra một LIST đầy đủ ngay lập tức (lưu toàn bộ kết quả trong bộ nhớ).
list_comp = [x * x for x in range(5)]
print(list_comp)  # [0, 1, 4, 9, 16]

# Generator expression tạo ra một GENERATOR object (một iterator).
# Điểm khác biệt chính:
# - List comprehension: trả về list chứa tất cả giá trị ngay lập tức (eager).
# - Generator expression: trả về generator, sinh giá trị "theo yêu cầu" (lazy), tiết kiệm bộ nhớ.
gen_exp = (x * x for x in range(5))
print(gen_exp)         # In ra object generator, ví dụ: <generator object <genexpr> at 0x...>

# Để lấy các giá trị từ generator, ta phải lặp qua nó hoặc chuyển thành list.
# Lưu ý: generator bị "tiêu thụ" khi lặp; sau khi đã chuyển thành list hoặc lặp hết,
# generator sẽ rỗng.
print(list(gen_exp))   # [0, 1, 4, 9, 16]

# Nếu in tiếp, sẽ thấy không còn giá trị vì generator đã bị tiêu thụ:
print(list(gen_exp))   # []  (đã bị rỗng)

# Nếu cần dùng lại, tạo lại generator hoặc dùng list để lưu kết quả.
gen_exp = (x * x for x in range(5))  # tạo lại
for v in gen_exp:
  print(v)  # 0 1 4 9 16

# Ví dụ generator bằng hàm với yield:
def gen_squares(n):
  # yield sinh từng giá trị một, không trả về toàn bộ danh sách
  for i in range(n):
    yield i * i

g = gen_squares(5)
print(next(g))  # 0
print(list(g))  # [1, 4, 9, 16]  (phần còn lại)

# Tóm tắt ngắn gọn:
# - Dùng generator khi dữ liệu lớn hoặc khi muốn sinh giá trị "khi cần" để tiết kiệm bộ nhớ.
# - Generator chỉ có thể lặp 1 lần. Nếu cần nhiều lần, lưu kết quả vào list hoặc tạo lại generator.
# @nghiavu  <-- tag bạn theo yêu cầu
# ...existing code...