import json

# Nhập dữ liệu từ người dùng
employees = []
counter = 1

print("Nhập thông tin nhân viên (nhập tên là 'done' để kết thúc):")

while True:
    name = input("Nhập tên: ").strip()
    if name.lower() == 'done':
        break

    age_input = input("Nhập tuổi: ").strip()
    try:
        age = int(age_input)
    except ValueError:
        print("Tuổi không hợp lệ, vui lòng nhập lại.")
        continue

    position = input("Nhập vị trí trong công ty: ").strip()

    employee = {
        "id": counter,
        "name": name,
        "age": age,
        "position": position
    }

    employees.append(employee)
    counter += 1

# Chuyển đổi sang JSON
json_data = json.dumps(employees, ensure_ascii=False, indent=4)

# Ghi vào file JSON
file_path = "/home/nghiavu/Desktop/data.json"
try:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(json_data)
    print(f"Dữ liệu đã được lưu vào: {file_path}")
except Exception as e:
    print(f"Lỗi khi ghi file: {e}")