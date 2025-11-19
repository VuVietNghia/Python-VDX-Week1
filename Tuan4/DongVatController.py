import DongVatEntity

def animal_world():
    # --- VÍ DỤ 1: TẠO ĐỐI TƯỢNG MÈO (Kế thừa từ DongVat) ---
    # Lưu ý: Bên file phải class tên là Meo, nên ở đây gọi DongVatEntity.Meo
    cat = DongVatEntity.Meo(
        ten_dong_vat="Mimi",
        mau_long="Vàng trắng",
        hanh_dong="Bắt chuột",
        loai_meo="Mèo Mướp"
    )

    # --- VÍ DỤ 2: TẠO ĐỐI TƯỢNG CHÓ (Cũng kế thừa từ DongVat) ---
    dog = DongVatEntity.Cho(
        ten_dong_vat="Lu",
        mau_long="Đen tuyền",
        hanh_dong="Giữ nhà",
        loai_cho="Chó Corgi"
    )

    print("--- HIỂU VỀ KẾ THỪA ---")

    # 1. Lớp con dùng thuộc tính của Lớp cha
    # (Dù trong class Meo/Cho không viết self.ten_dong_vat, nhưng nó vẫn có nhờ super())
    print(f"Tên của mèo là: {cat.ten_dong_vat}")  # In ra: Mimi
    print(f"Tên của chó là: {dog.ten_dong_vat}")  # In ra: Lu

    # 2. Lớp con dùng thuộc tính riêng của nó
    print(f"Loài mèo: {cat.loai_meo}")
    print(f"Loài chó: {dog.loai_cho}")

    print("\n--- GỌI HÀM RIÊNG ---")
    # Gọi hàm hiển thị (theo cách bạn đang viết code hiện tại)
    cat.hien_thi_meow()
    dog.hien_thi_gau()

# Chạy chương trình
animal_world()