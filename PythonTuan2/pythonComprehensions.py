doubles = []

for x in range(1, 11):
    doubles.append(x * 2)

doubles = [x * 2 for x in range(1, 11)]
triplets = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(doubles)
print(triplets)
print(squares)

traiCays = [traiCay.upper() for traiCay in ["apple", "banana", "cherry"]]

print(traiCays)

traiCays = [traiCay[0] for traiCay in ["apple", "banana", "cherry"]]
print(traiCays)

numbers = [1, -2, 3, -4, -5, 6]
positive = [num for num in numbers if num > 0]
print(positive)

listNhan3s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listNhan3 = [num * 3 for num in listNhan3s if num % 2 == 0]
print(listNhan3)

listXe = []

class XeHoi:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau

# Tạo ra hai đối tượng (hai chiếc xe) từ lớp XeHoi
xe_cua_toi = XeHoi("Toyota", "Đỏ")
xe_cua_ban = XeHoi("Ford", "Xanh")

listXe.append(xe_cua_toi)
listXe.append(xe_cua_ban)

print(listXe)

# Tổng hợp các trường dữ liệu
class KhachHang:
    # khởi tạo (constructor) tự động gọi khi tạo đối tượng mới
    def __init__(self, hoTen, email, password, ngaySinh, gioiTinh, soDienThoai):
        # self là từ khóa đặc biệt trong Python, nó đại diện cho đối tượng hiện tại
        self.hoTen = hoTen
        self.email = email
        self.password = password
        self.ngaySinh = ngaySinh
        self.gioiTinh = gioiTinh
        self.soDienThoai = soDienThoai


    # phương thức (method) cho biết class trên sẽ chạy như thế nào
    def getInfo(self):
        return f"Họ tên: {self.hoTen}, Email: {self.email}, Mật khẩu: {self.password}, Ngày sinh: {self.ngaySinh}, Giới tính: {self.gioiTinh}, Số điện thoại: {self.soDienThoai}"

# tạo ra hai đối tượng (hai khách hàng) từ lớp KhachHang (truyền đối số vào class KhachHang)
khachHang1 = KhachHang("Nguyễn Văn A", "nguyenvana@gmail.com", "123456", "1990-01-01", "Nam", "0909090909")
khachHang2 = KhachHang("Nguyễn Thị B", "nguyenthib@gmail.com", "123456", "1990-01-01", "Nữ", "0909090909")

print(khachHang1.hoTen)