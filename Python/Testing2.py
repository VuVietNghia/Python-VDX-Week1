import random

def play_guessing_game():
    """
    Hàm chính cho trò chơi đoán số.
    Sử dụng: import random, while, if-elif-else, try-except, input/print.
    """
    # 1. Biến và Kiểu dữ liệu (int)
    soNho = int(input("Nhap so nho: "))
    soLon = int(input("Nhap so lon: "))
    secret_number = random.randint(soNho, soLon)
    guess = 0
    attempts = 0

    print(f"\n--- Chào mừng đến với trò chơi ĐOÁN SỐ ({soNho}-{soLon}) ---")

    # 2. Vòng lặp (while)
    while guess != secret_number:
        user_input = input("Hãy nhập số bạn đoán: ")
        attempts += 1

        # 3. Xử lý lỗi (try-except)
        try:
            guess = int(user_input)
        except ValueError:
            print("Lỗi: Vui lòng chỉ nhập số nguyên.")
            continue  # Quay lại đầu vòng lặp

        # 4. Cấu trúc điều khiển (if-elif-else)
        if guess < secret_number:
            print("Số bạn đoán quá nhỏ!")
        elif guess > secret_number:
            print("Số bạn đoán quá lớn!")
        else:
            print(f"🎉 Chúc mừng! Bạn đã đoán đúng số {secret_number} sau {attempts} lần thử!")

def get_list_statistics(numbers_list):
    """
    Hàm nhận vào một danh sách số và trả về một từ điển (dict)
    chứa các giá trị thống kê.
    Sử dụng: function, parameters, return, list, dict, basic operations.
    """
    # 1. Xử lý trường hợp danh sách rỗng
    if not numbers_list:
        return {
            "average": 0,
            "maximum": None,
            "minimum": None,
            "count": 0
        }

    # 2. Các phép toán cơ bản
    total_sum = sum(numbers_list)
    count = len(numbers_list)
    average = total_sum / count
    maximum = max(numbers_list)
    minimum = min(numbers_list)

    # 3. Trả về một dictionary
    return {
        "average": average,
        "maximum": maximum,
        "minimum": minimum,
        "count": count
    }

def run_statistics_program():
    """
    Hàm lấy input từ người dùng, gọi hàm tính toán
    và format dữ liệu đầu ra.
    Sử dụng: string manipulation (.split), for loop, try-except, f-string.
    """
    print("\n--- Chương trình TÍNH TOÁN THỐNG KÊ DANH SÁCH ---")
    user_input = input("Nhập một danh sách các số (cách nhau bằng dấu phẩy, ví dụ: 10, 5.5, -3): ")

    # 1. Biến (list) và Xử lý lỗi (try-except)
    numbers = []
    # Dùng .split() để tách chuỗi thành danh sách các chuỗi nhỏ
    string_numbers = user_input.split(',')

    # 2. Vòng lặp (for) và Xử lý lỗi
    for s_num in string_numbers:
        try:
            # Dùng .strip() để xóa khoảng trắng thừa
            # Chuyển đổi sang float để chấp nhận cả số nguyên và số thực
            numbers.append(float(s_num.strip()))
        except ValueError:
            print(f"Cảnh báo: Bỏ qua giá trị không hợp lệ '{s_num}'")

    # 3. Gọi hàm và nhận kết quả (kiểu dict)
    stats = get_list_statistics(numbers)

    # 4. Format dữ liệu (f-string)
    print("\n--- KẾT QUẢ THỐNG KÊ ---")
    # Dùng :.2f để format số float chỉ lấy 2 chữ số thập phân
    print(f"  Số lượng phần tử: {stats['count']}")
    print(f"  Giá trị trung bình: {stats['average']:.2f}")
    print(f"  Giá trị lớn nhất: {stats['maximum']}")
    print(f"  Giá trị nhỏ nhất: {stats['minimum']}")

def main():
    """
    Hàm menu chính của chương trình.
    """
    while True:
        print("\n======================")
        print("PYTHON CƠ BẢN TỔNG HỢP")
        print("1. Chơi trò đoán số")
        print("2. Tính toán thống kê danh sách")
        print("3. Thoát")
        choice = input("Vui lòng chọn chức năng (1-3): ")

        if choice == '1':
            play_guessing_game()
        elif choice == '2':
            run_statistics_program()
        elif choice == '3':
            print("Tạm biệt!")
            break  # Thoát khỏi vòng lặp while True
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

# Dòng này đảm bảo hàm main() chỉ chạy khi file này được thực thi trực tiếp
if __name__ == "__main__":
    main()