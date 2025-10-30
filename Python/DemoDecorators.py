import json

sinhVien = {
    "ten": "Nghia",
    "tuoi": 20,
    "ngheNghiep": "Dev"
}

filePath = "/home/nghiavu/Desktop/output.json"

try:
    #"w" (write/ghi đè), "a" (append/nối thêm)
    with open(file=filePath, mode="w") as file:
        json.dump(sinhVien, file, indent=4)
        print(f"Đã thêm dữ liệu vào file {filePath} thành công.")

except PermissionError:
    # Xử lý lỗi khi không có quyền ghi vào file hoặc thư mục
    print(f"Lỗi: Không có quyền truy cập để ghi vào file {filePath}.")