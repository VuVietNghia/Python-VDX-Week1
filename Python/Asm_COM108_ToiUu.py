import random
import math  # Sử dụng thư viện math cho UCLN, BCNN

# --- Hằng số toàn cục ---
# Dùng hằng số giúp dễ dàng thay đổi giá trị sau này
GIA_GIO_KARAOKE = 150_000  # 150,000

# Bảng giá điện (số kWh trong bậc, đơn giá)
BAC_THANG_TIEN_DIEN = [
    (50, 1.678),  # Bậc 1: 0 - 50 kWh
    (50, 1.734),  # Bậc 2: 51 - 100 kWh
    (100, 2.014),  # Bậc 3: 101 - 200 kWh
    (100, 2.536),  # Bậc 4: 201 - 300 kWh
    (100, 2.834),  # Bậc 5: 301 - 400 kWh
    (float('inf'), 2.927)  # Bậc 6: Từ 401 kWh trở đi
]

# Mệnh giá tiền để đổi
MENH_GIA_TIEN = [500, 200, 100, 50, 20, 10, 5, 2, 1]


# --- Các hàm logic (Chỉ tính toán và trả về kết quả) ---

# Chức năng 1: Kiểm tra số
def la_so_nguyen(number):
    """Kiểm tra một số có phải là số nguyên (kể cả từ float)."""
    # .is_integer() là cách chuẩn để kiểm tra
    return number.is_integer()


def la_so_nguyen_to(number):
    """Kiểm tra số nguyên tố. Trả về True/False."""
    if number < 2:
        return False
    # Chỉ cần kiểm tra đến căn bậc 2 của number
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def la_so_chinh_phuong(number):
    """Kiểm tra số chính phương. Trả về True/False."""
    if number < 0:
        return False
    root = int(math.sqrt(number))
    return root * root == number


# Chức năng 10 (Hàm hỗ trợ): Rút gọn phân số
def rut_gon_phan_so(tu, mau):
    """Rút gọn phân số bằng cách tìm UCLN."""
    if mau == 0:
        return None  # Không thể rút gọn nếu mẫu là 0
    ucln = math.gcd(tu, mau)
    return tu // ucln, mau // ucln


# --- Các hàm chạy chức năng (Bao gồm Input/Output) ---

def chuong_trinh_kiem_tra_so():
    """Chạy chức năng 1: Kiểm tra số."""
    print("Bạn đã chọn kiểm tra số")
    try:
        number = float(input("Nhập vào số: "))

        if not la_so_nguyen(number):
            print(f"{number} không phải là số nguyên.")
            return

        # Nếu là số nguyên, chuyển đổi và kiểm tra
        number_int = int(number)
        print(f"{number_int} là số nguyên.")

        # Kiểm tra nguyên tố
        if la_so_nguyen_to(number_int):
            print(f"{number_int} LÀ số nguyên tố.")
        else:
            print(f"{number_int} KHÔNG phải là số nguyên tố.")

        # Kiểm tra chính phương
        if la_so_chinh_phuong(number_int):
            print(f"{number_int} LÀ số chính phương.")
        else:
            print(f"{number_int} KHÔNG phải là số chính phương.")

    except ValueError:
        print("Lỗi: Vui lòng nhập một số hợp lệ!")


def chuong_trinh_ucln_bcnn():
    """Chạy chức năng 2: Tìm UCLN và BCNN."""
    print("Bạn đã chọn tìm UCLN và BCNN của 2 số")
    try:
        x, y = map(int, input("Nhập vào 2 số (cách nhau bằng dấu cách): ").split())

        # math.gcd và math.lcm là cách tối ưu nhất (có từ Python 3.9)
        ucln = math.gcd(x, y)
        bcnn = math.lcm(x, y)  # (x * y) // ucln

        print(f"Ước chung lớn nhất của {x} và {y}: {ucln}")
        print(f"Bội chung nhỏ nhất của {x} và {y}: {bcnn}")
    except ValueError:
        print("Lỗi: Vui lòng nhập 2 số nguyên hợp lệ!")


def chuong_trinh_tinh_tien_karaoke():
    """Chạy chức năng 3: Tính tiền karaoke."""
    print("\nTính tiền karaoke")
    try:
        gioDau = int(input("Nhập vào giờ bắt đầu (12-23): "))
        gioCuoi = int(input("Nhập vào giờ kết thúc (12-23): "))

        if not (12 <= gioDau <= 23 and 12 <= gioCuoi <= 23 and gioDau < gioCuoi):
            print("Lỗi: Nhập giờ trong khoảng (12 -> 23) và giờ kết thúc > giờ bắt đầu")
            return

    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")
        return

    tongGio = gioCuoi - gioDau
    print(f"Tổng số giờ hát: {tongGio}h")

    tienGoc = tongGio * GIA_GIO_KARAOKE
    tienSauGiamGia3Gio = tienGoc

    # 1. Tính giảm giá cho giờ > 3
    if tongGio > 3:
        soGioVuot = tongGio - 3
        tienGiamGia3Gio = soGioVuot * GIA_GIO_KARAOKE * 0.3
        tienSauGiamGia3Gio = tienGoc - tienGiamGia3Gio
        print(f"Giảm giá {tienGiamGia3Gio:,.0f} VND (cho {soGioVuot}h vượt mốc 3 giờ)")

    tienCuoiCung = tienSauGiamGia3Gio

    # 2. Tính giảm giá khung giờ vàng (áp dụng sau khi đã giảm giá 3 giờ)
    if 14 <= gioDau <= 17:
        tienGiamGioVang = tienSauGiamGia3Gio * 0.1
        tienCuoiCung = tienSauGiamGia3Gio - tienGiamGioVang
        print(f"Giảm giá khung giờ vàng 10%: {tienGiamGioVang:,.0f} VND")

    print(f"Tổng tiền phải trả: {tienCuoiCung:,.0f} VND")


def chuong_trinh_tinh_tien_dien():
    """Chạy chức năng 4: Tính tiền điện (Đã tối ưu)."""
    print("Bạn đã chọn chức năng tính tiền điện")
    try:
        soDien = float(input("\nNhập vào số điện (kWh): "))
        if soDien < 0:
            print("Số điện phải lớn hơn hoặc bằng 0.")
            return
    except ValueError:
        print("Vui lòng nhập một số hợp lệ!")
        return

    tongTien = 0
    soDienConLai = soDien

    for (so_kwh_trong_bac, don_gia) in BAC_THANG_TIEN_DIEN:
        if soDienConLai <= 0:
            break

        dienSuDungBacNay = min(soDienConLai, so_kwh_trong_bac)
        tongTien += dienSuDungBacNay * don_gia
        soDienConLai -= dienSuDungBacNay

    print(f"Tiền điện cần đóng là: {tongTien:,.2f} VND")


def chuong_trinh_doi_tien():
    """Chạy chức năng 5: Đổi tiền."""
    print("Bạn đã chọn chức năng đổi tiền")
    try:
        amount = int(input("Nhập mệnh giá tiền cần đổi: "))
        if amount < 0:
            print("Bạn cần nhập số tiền lớn hơn hoặc bằng 0")
            return
    except ValueError:
        print("Vui lòng nhập số nguyên!")
        return

    print(f"Số tiền {amount:,.0f} VND được đổi thành:")
    soTienConLai = amount

    # Dùng dictionary để lưu kết quả sạch sẽ hơn
    ketQuaDoi = {}

    for menhGia in MENH_GIA_TIEN:
        soTo = soTienConLai // menhGia
        if soTo > 0:
            ketQuaDoi[menhGia] = soTo
            soTienConLai %= menhGia

    if not ketQuaDoi:
        print("0 đồng.")
    else:
        for menhGia, soTo in ketQuaDoi.items():
            print(f" - {soTo} tờ {menhGia:,.0f} VND")


def in_bang_tra_gop(tienVay, laiSuatThang, kyHan):
    """Hàm chung để in bảng kê trả góp (Dùng cho cả F6 và F7)."""
    tienGocHangThang = tienVay / kyHan
    tienConLai = tienVay

    print("\nBảng chi tiết vay trả góp (lãi trên dư nợ giảm dần)")
    print("---------------------------------------------------------------------------------")
    print(f"{'Kỳ hạn':<6} | {'Lãi phải trả':<15} | {'Gốc phải trả':<15} | {'Tổng phải trả':<16} | {'Tiền còn lại':<15}")
    print("---------------------------------------------------------------------------------")

    tongLai = 0
    for i in range(1, kyHan + 1):
        tienLai = tienConLai * laiSuatThang
        tongLai += tienLai
        tienPhaiTra = tienGocHangThang + tienLai
        tienConLai -= tienGocHangThang

        # Đảm bảo kỳ cuối cùng tiền còn lại là 0 (tránh sai số float)
        if i == kyHan:
            tienConLai = 0

        print(f"{i:<6} | {tienLai:15,.2f} | {tienGocHangThang:15,.2f} | {tienPhaiTra:16,.2f} | {tienConLai:15,.2f}")

        if i % 12 == 0 and i < kyHan:
            print(f"------------------------------- Hết năm {i // 12} -----------------------------------")

    print("---------------------------------------------------------------------------------")
    print(f"Tổng tiền gốc đã trả: {tienVay:,.2f}")
    print(f"Tổng tiền lãi đã trả: {tongLai:,.2f}")
    print(f"Tổng cộng (gốc + lãi): {(tienVay + tongLai):,.2f}")


def chuong_trinh_lai_suat_vay():
    """Chạy chức năng 6: Tính lãi suất vay."""
    print("Bạn đã chọn tính lãi suất vay ngân hàng")
    try:
        tienVay = int(input("\nNhập số tiền muốn vay: "))
        if tienVay <= 0:
            print("Tiền vay phải là số dương.")
            return
    except ValueError:
        print("Vui lòng nhập số nguyên!")
        return

    # Các thông số nên được định nghĩa rõ ràng
    LAI_SUAT_NAM = 0.05 * 12  # Giả sử 5%/tháng là 60%/năm
    LAI_SUAT_THANG = 0.05
    KY_HAN = 12  # 12 tháng

    print(
        f"Đang tính với lãi suất {LAI_SUAT_THANG * 100:.1f}%/tháng ({LAI_SUAT_NAM * 100:.1f}%/năm) trong {KY_HAN} tháng.")
    in_bang_tra_gop(tienVay, LAI_SUAT_THANG, KY_HAN)


def chuong_trinh_vay_mua_xe():
    """Chạy chức năng 7: Vay tiền mua xe."""
    print("Bạn đã chọn vay tiền mua xe")
    try:
        tienXe = int(input("\nNhập giá trị xe: "))
        if tienXe <= 0:
            print("Giá trị xe phải là số dương.")
            return

        # Giá trị 500_000 trong code gốc của bạn quá nhỏ
        VAY_XE_TOI_DA = 500_000_000  # Giả định là 500 triệu
        print(f"Chính sách: Vay tối đa {VAY_XE_TOI_DA:,.0f} VND")

        tienTraTruocGoiY = tienXe * 0.2
        print(f"Số tiền trả trước gợi ý (20%): {tienTraTruocGoiY:,.0f}")

        tienVay = int(input("Nhập số tiền bạn muốn vay: "))

        if tienVay <= 0:
            print("Tiền vay phải là số dương.")
            return
        if tienVay > VAY_XE_TOI_DA:
            print(f"Số tiền vay của bạn ({tienVay:,.0f}) vượt quá mức quy định ({VAY_XE_TOI_DA:,.0f})!")
            return
        if tienVay > tienXe * 0.8:
            print(f"Số tiền vay ({tienVay:,.0f}) vượt quá 80% giá trị xe ({tienXe * 0.8:,.0f})!")
            return

    except ValueError:
        print("Vui lòng nhập số nguyên!")
        return

    LAI_SUAT_THANG = 0.075 / 12  # Giả sử lãi suất 7.5%/năm
    KY_HAN = 24  # Giả sử vay 2 năm (288 tháng như code gốc là 24 năm, quá dài)

    print(
        f"Đang tính với lãi suất {LAI_SUAT_THANG * 100:.2f}%/tháng ({LAI_SUAT_THANG * 12 * 100:.1f}%/năm) trong {KY_HAN} tháng.")
    in_bang_tra_gop(tienVay, LAI_SUAT_THANG, KY_HAN)


def xep_loai_hoc_luc(dtb):
    """Hàm logic con: Trả về chuỗi xếp loại học lực."""
    if dtb >= 9:
        return "Xuất sắc"
    elif dtb >= 8:
        return "Giỏi"
    elif dtb >= 6.5:
        return "Khá"
    elif dtb >= 5:
        return "Trung bình"
    else:
        return "Yếu"


def chuong_trinh_thong_tin_sv():
    """Chạy chức năng 8: Thông tin sinh viên."""
    print("Bạn đã chọn sắp xếp thông tin sinh viên")
    try:
        n = int(input("Mời nhập vào số sinh viên: "))
        if n <= 0:
            print("Phải nhập ít nhất 1 sinh viên.")
            return
    except ValueError:
        print("Vui lòng nhập số nguyên!")
        return

    sv = []
    for i in range(n):
        print(f"\n--- Nhập thông tin sinh viên {i + 1} ---")
        hoten = input("Họ tên sinh viên: ")

        while True:  # Vòng lặp để bắt nhập điểm đúng
            try:
                dtb = float(input(f"Điểm trung bình của {hoten}: "))
                if 0 <= dtb <= 10:  # Điểm hệ 10
                    break
                else:
                    print("Lỗi: Nhập điểm trong khoảng 0 đến 10")
            except ValueError:
                print("Lỗi: Vui lòng nhập số thực!")

        sv.append({"hoten": hoten, "dtb": dtb})

    # Sắp xếp giảm dần theo điểm
    sv.sort(key=lambda x: x["dtb"], reverse=True)

    print("\n---------- DANH SÁCH SINH VIÊN (ĐÃ SẮP XẾP) ----------")
    for s in sv:
        hoc_luc = xep_loai_hoc_luc(s['dtb'])
        print(f"SV: {s['hoten']:<25} | ĐTB: {s['dtb']:<4.1f} | Học lực: {hoc_luc}")


def chuong_trinh_fpoly_lott():
    """Chạy chức năng 9: Game FPOLY-LOTT."""
    print("Bạn đã chọn game FPOLY-LOTT")
    try:
        # Nhập 2 số trên cùng 1 dòng
        numberA, numberB = map(int, input("\nNhập vào 2 số (1-15), cách nhau bằng dấu cách: ").split())
        if not (1 <= numberA <= 15 and 1 <= numberB <= 15):
            print("Vui lòng chỉ nhập số từ 1 đến 15.")
            return
    except ValueError:
        print("Vui lòng nhập 2 số nguyên hợp lệ!")
        return

    # random.seed() là không cần thiết, Python tự làm điều này.
    print("Kết quả xổ số FPOLY-LOTT")
    print("----------------------")

    # Tạo 1 danh sách kết quả
    ket_qua_xo_so = [random.randint(1, 15) for _ in range(2)]
    print(f"{ket_qua_xo_so[0]:^10} {ket_qua_xo_so[1]:^10}")

    count = 0
    # Dùng set để xử lý trường hợp người dùng nhập 2 số giống nhau
    so_cua_ban = {numberA, numberB}

    for so in so_cua_ban:
        if so in ket_qua_xo_so:
            count += 1  # Tăng 1 nếu số đó có trong kết quả

    # Xử lý trường hợp đặc biệt: 2 số trúng là 1 số (vd: user 5,5; kq 5,8)
    # Hoặc 2 số trúng trùng nhau (vd: user 5,8; kq 5,5)
    # Logic chuẩn là đếm số lượng số *khác biệt* trúng
    if ket_qua_xo_so[0] in so_cua_ban:
        count = 1
    if ket_qua_xo_so[1] in so_cua_ban:
        # Nếu số thứ 2 trúng VÀ khác số thứ 1 (hoặc số 1 ko trúng)
        if ket_qua_xo_so[1] != ket_qua_xo_so[0] or (ket_qua_xo_so[0] not in so_cua_ban):
            count += 1

    # Logic đơn giản nhất là theo code gốc:
    count = 0
    if numberA in ket_qua_xo_so or numberB in ket_qua_xo_so:
        if numberA in ket_qua_xo_so:
            count += 1
        if numberB in ket_qua_xo_so and numberB != numberA:  # Tránh TH user nhập 5, 5 và kq là 5
            count += 1
        # Xử lý TH user nhập (5, 8) và KQ là (5, 5)
        if numberA in ket_qua_xo_so and numberB in ket_qua_xo_so and ket_qua_xo_so[0] == ket_qua_xo_so[1]:
            count = 2  # Vẫn tính là 2
        # Logic gốc của bạn
        if numberA == ket_qua_xo_so[0] or numberB == ket_qua_xo_so[0]:
            count += 1
        if numberA == ket_qua_xo_so[1] or numberB == ket_qua_xo_so[1]:
            count += 1
        # Trường hợp 2 số user trùng nhau và trúng 1 số trong KQ
        if numberA == numberB and numberA in ket_qua_xo_so:
            count = 2 if ket_qua_xo_so[0] == ket_qua_xo_so[1] else 1

    # Đơn giản hóa logic: Đếm số lượng số trúng
    trung_so_A = numberA in ket_qua_xo_so
    trung_so_B = numberB in ket_qua_xo_so
    count = 0
    if trung_so_A or trung_so_B:
        # Logic này giả định user trúng giải nếu 1 trong 2 số của họ xuất hiện
        # Và trúng giải đặc biệt nếu cả 2 số của họ đều xuất hiện
        # (Kể cả khi KQ là [5, 5] và user là [5, 8])
        if trung_so_A:
            count += 1
        if trung_so_B:
            count += 1

        # Nếu user nhập 2 số giống nhau (5, 5) và trúng (KQ [5, 8])
        if numberA == numberB and trung_so_A:
            count = 1  # Chỉ tính 1 giải

    print("\n----------------------")
    if count == 0:
        print("Rất tiếc, chúc bạn may mắn lần sau.")
    elif count == 1:
        print("🎉 Chúc mừng bạn đã trúng giải NHÌ! 🎉")
    else:  # count >= 2
        print("🏆🏆 Chúc mừng bạn đã trúng giải NHẤT! 🏆🏆")


def chuong_trinh_tinh_toan_phan_so():
    """Chạy chức năng 10: Tính toán phân số (Có rút gọn)."""
    print("Bạn đã chọn tính toán phân số")
    try:
        print("Nhập vào phân số 1 (dạng tu mau): ", end="")
        tu1, mau1 = map(int, input().split())
        print("Nhập vào phân số 2 (dạng tu mau): ", end="")
        tu2, mau2 = map(int, input().split())
        if mau1 == 0 or mau2 == 0:
            print("Lỗi: Mẫu số không được bằng 0!")
            return
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng (2 số nguyên cách nhau)!")
        return

    # Tính toán
    tong_tu = tu1 * mau2 + tu2 * mau1
    tong_mau = mau1 * mau2
    hieu_tu = tu1 * mau2 - tu2 * mau1
    hieu_mau = mau1 * mau2
    tich_tu = tu1 * tu2
    tich_mau = mau1 * mau2
    thuong_tu = tu1 * mau2
    thuong_mau = mau1 * tu2

    # In kết quả CÓ RÚT GỌN
    print("\n--- Kết quả (đã rút gọn) ---")
    rt_tong = rut_gon_phan_so(tong_tu, tong_mau)
    rt_hieu = rut_gon_phan_so(hieu_tu, hieu_mau)
    rt_tich = rut_gon_phan_so(tich_tu, tich_mau)

    print(f"Tổng:   {tu1}/{mau1} + {tu2}/{mau2} = {rt_tong[0]}/{rt_tong[1]}")
    print(f"Hiệu:   {tu1}/{mau1} - {tu2}/{mau2} = {rt_hieu[0]}/{rt_hieu[1]}")
    print(f"Tích:   {tu1}/{mau1} * {tu2}/{mau2} = {rt_tich[0]}/{rt_tich[1]}")

    # Kiểm tra chia cho 0 khi tính thương
    if thuong_mau == 0:
        print(f"Thương: {tu1}/{mau1} / {tu2}/{mau2} = Không thể chia cho 0")
    else:
        rt_thuong = rut_gon_phan_so(thuong_tu, thuong_mau)
        print(f"Thương: {tu1}/{mau1} / {tu2}/{mau2} = {rt_thuong[0]}/{rt_thuong[1]}")


def thoat_chuong_trinh():
    """Chạy chức năng 11: Thoát."""
    print("Bạn đã chọn thoát. Tạm biệt!")
    return "exit"  # Trả về tín hiệu để thoát vòng lặp


def in_menu():
    """In menu chính cho người dùng."""
    print("\n+##------------------* Menu *------------------##+")
    print("| 1. Kiểm tra số (nguyên tố, chính phương)    |")
    print("| 2. Tìm UCLN và BCNN của 2 số               |")
    print("| 3. Tính tiền Karaoke                       |")
    print("| 4. Tính tiền điện                          |")
    print("| 5. Đổi tiền                                |")
    print("| 6. Tính lãi suất vay ngân hàng (12 tháng)  |")
    print("| 7. Tính lãi vay mua xe                     |")
    print("| 8. Sắp xếp thông tin sinh viên             |")
    print("| 9. Game FPOLY-LOTT                         |")
    print("| 10. Tính toán phân số (có rút gọn)         |")
    print("| 11. Thoát chương trình                     |")
    print("+##------------------*======*------------------##+")


# --- Hàm Main chính ---
def main():
    """
    Hàm main điều hướng chương trình.
    Sử dụng dictionary 'lua_chon' để gọi hàm tương ứng.
    Đây là cách làm sạch sẽ, dễ bảo trì hơn 1 chuỗi if/elif dài.
    """

    # Bộ điều hướng (router) chức năng
    # Ánh xạ lựa chọn của người dùng (số) tới hàm cần chạy
    lua_chon = {
        1: chuong_trinh_kiem_tra_so,
        2: chuong_trinh_ucln_bcnn,
        3: chuong_trinh_tinh_tien_karaoke,
        4: chuong_trinh_tinh_tien_dien,
        5: chuong_trinh_doi_tien,
        6: chuong_trinh_lai_suat_vay,
        7: chuong_trinh_vay_mua_xe,
        8: chuong_trinh_thong_tin_sv,
        9: chuong_trinh_fpoly_lott,
        10: chuong_trinh_tinh_toan_phan_so,
        11: thoat_chuong_trinh,
    }

    while True:
        in_menu()
        try:
            chon = int(input("Nhập chức năng (1-11): "))
        except ValueError:
            print("Lỗi: Vui lòng nhập một số từ 1 đến 11!")
            continue

        # Lấy hàm tương ứng với lựa chọn từ dictionary
        ham_can_chay = lua_chon.get(chon)

        if ham_can_chay:
            ket_qua = ham_can_chay()  # Gọi hàm
            if ket_qua == "exit":
                break  # Thoát vòng lặp nếu hàm trả về "exit"
        else:
            print("Chức năng không hợp lệ! Vui lòng chọn lại.")

        # Tạm dừng màn hình
        input("\n--- Nhấn Enter để tiếp tục ---")


# Chỉ chạy hàm main() khi file này được thực thi trực tiếp
if __name__ == "__main__":
    main()