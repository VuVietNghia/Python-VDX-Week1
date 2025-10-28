def changecase(func):
  # Đây là một decorator: hàm nhận vào một hàm (func) và trả về một hàm mới (myinner).
  # Mục đích của decorator này là chuyển kết quả trả về của func sang chữ IN HOA.
  def myinner(*args, **kwargs):
    # *args và **kwargs cho phép myinner nhận bất kỳ tham số vị trí và tham số từ khoá nào
    # rồi chuyển tiếp chúng sang func khi gọi.
    return func(*args, **kwargs).upper()
  return myinner

# Áp dụng decorator changecase cho hàm myfunction.
# Việc viết @changecase tương đương với: myfunction = changecase(myfunction)
@changecase
def myfunction(nam):
  # Hàm gốc trả về một chuỗi chào.
  return "Hello " + nam

# Khi gọi myfunction("John"), thực tế sẽ gọi myinner, bên trong gọi myfunction gốc,
# sau đó kết quả được .upper() để in hoa toàn bộ.
print(myfunction("John"))
# ...existing code...