import random
import time
from datetime import datetime

# Chức năng 1: Kiểm tra số nguyên
def checkSN(number):
    return 1 if number == int(number) else -1

def checkSoNguyenTo(number):
    if not isinstance(number, int):
        return
    if number < 2:
        print(f"{number} khong phai so nguyen to")
        return
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
    if count == 0:
        print(f"{number} la so nguyen to")
    else:
        print(f"{number} khong phai la so nguyen to")

def soChinhPhuong(number):
    if not isinstance(number, int):
        return
    check = -1
    for i in range(2, number // 2 + 1):
        if i * i == number:
            check = 1
            break
    if check == 1:
        print(f"{number} la so chinh phuong")
    else:
        print(f"{number} khong phai la so chinh phuong")

# Chức năng 2: Tìm UCLN và BCNN
def timUocChungLonNhat(x, y):
    while y != 0:
        tam = y
        y = x % y
        x = tam
    return x

def timBoiChungLonNhat(x, y):
    ucln = timUocChungLonNhat(x, y)
    return (x * y) // ucln

# Chức năng 3: Tính tiền karaoke
def tinhTienKaraoke():
    T = 150000
    while True:
        print("\nTinh tien karaoke")
        try:
            gioDau = int(input("Nhap vao gio bat dau: "))
            gioCuoi = int(input("Nhap vao gio ket thuc: "))
            if gioDau < 12 or gioCuoi > 23 or gioDau >= gioCuoi:
                print("Nhap gio trong khoang (12 -> 23) va gio ket thuc > gio bat dau")
                continue
            break
        except:
            print("Vui long nhap so nguyen hop le!")

    tongGio = gioCuoi - gioDau
    print(f"Gio cuoi {gioCuoi}h - gio dau {gioDau}h = {tongGio}h")
    tienGio = tongGio * T

    kmv = 0
    if gioDau >= 14 and gioDau <= 17:
        print("Khuyen mai khung gio vang 10%")
        if tongGio > 3:
            km4 = (tongGio - 3) * 0.3 * T
            tienGio = tongGio * T - km4
            print(f"So gio vuot: {tongGio - 3} => tien KM: {km4}")
        kmv = tienGio * 0.1
        print(f"Tien gio truoc KMV: {int(tienGio)}")
        print(f"Tien KMV: {int(kmv)}")
        tienGio -= kmv
    else:
        if tongGio > 3:
            km4 = (tongGio - 3) * 0.3 * T
            tienGio = tongGio * T - km4
            print(f"So gio vuot: {tongGio - 3} => tien KM: {km4}")

    print(f"Tien phai tra: {int(tienGio)}")

# Chức năng 4: Tính tiền điện
def tinhTienDien():
    while True:
        try:
            soDien = float(input("\nNhap vao so dien: "))
            if soDien < 0:
                print("Nhap so dien > 0")
                continue
            break
        except:
            print("Vui long nhap so hop le!")

    if soDien < 51:
        tienDong = soDien * 1.678
    elif soDien < 101:
        tienDong = (50 * 1.678) + ((soDien - 50) * 1.734)
    elif soDien < 201:
        tienDong = (50 * 1.678) + (50 * 1.734) + ((soDien - 100) * 2.014)
    elif soDien < 301:
        tienDong = (50 * 1.678) + (50 * 1.734) + (100 * 2.014) + ((soDien - 200) * 2.536)
    elif soDien < 401:
        tienDong = (50 * 1.678) + (50 * 1.734) + (100 * 2.014) + (100 * 2.536) + ((soDien - 300) * 2.834)
    else:
        tienDong = (50 * 1.678) + (50 * 1.734) + (100 * 2.014) + (100 * 2.536) + (100 * 2.834) + ((soDien - 400) * 2.927)

    print(f"Tien dien can dong la: {tienDong:.2f}")

# Chức năng 5: Đổi tiền
def doiTien(amount):
    menhGia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    soTo = [0] * 9

    for i in range(9):
        if amount >= menhGia[i]:
            soTo[i] = amount // menhGia[i]
            amount %= menhGia[i]

    for i in range(9):
        if soTo[i] > 0:
            print(f"{soTo[i]} to {menhGia[i]}")

# Chức năng 6: Tính lãi suất vay
def tinhLaiSuatVay():
    try:
        tienVay = int(input("\nNhap so tien muon vay: "))
    except:
        print("Vui long nhap so nguyen!")
        return

    laiSuatThang = 0.05
    kyHan = 12
    tienGoc = tienVay / kyHan
    tienCon = tienVay

    print("\nBang lai suat vay ngan hang")
    print("Ky han | Lai phai tra | Goc phai tra | So tien phai tra | So tien con lai")
    print("-----------------------------------------------------------------------")

    for i in range(1, kyHan + 1):
        tienLai = tienCon * laiSuatThang
        tienTra = tienGoc + tienLai
        tienCon -= tienGoc
        print(f"{i:6d} | {tienLai:12.2f} | {tienGoc:12.2f} | {tienTra:16.2f} | {tienCon:15.2f}")

# Chức năng 7: Vay tiền mua xe
def vayTienMuaXe():
    try:
        tienXe = int(input("\nNhap gia tri xe: "))
    except:
        print("Vui long nhap so nguyen!")
        return

    tienTraTruoc = tienXe * 0.2
    print(f"Tien tra truoc: {int(tienTraTruoc)}")

    try:
        tienVay = int(input("\nNhap so tien muon vay: "))
    except:
        print("Vui long nhap so nguyen!")
        return

    if tienVay > 500000:
        tienTraTruoc = tienXe - 500000
        print("So tien vay cua ban vuot qua muc quy dinh")
        return

    laiSuatThang = 0.05
    kyHan = 288
    tienGoc = tienVay / kyHan
    tienCon = tienVay
    nam = 1

    print("\nBang lai suat vay ngan hang")
    print("Ky han | Lai phai tra | Goc phai tra | So tien phai tra | So tien con lai")
    print("---------------------------------------------------------------------------------")

    for i in range(1, kyHan + 1):
        tienLai = tienCon * laiSuatThang
        tienTra = tienGoc + tienLai
        tienCon -= tienGoc
        print(f"{i:6d} | {tienLai:12.2f} | {tienGoc:12.2f} | {tienTra:16.2f} | {tienCon:15.2f}")
        if i % 12 == 0:
            nam += 1
            print(f"-------------------------------Ket thuc {nam} nam-----------------------------------")

# Chức năng 8: Thông tin sinh viên
def thongTinSV():
    try:
        n = int(input("Moi nhap vao so sinh vien: "))
    except:
        print("Vui long nhap so nguyen!")
        return

    sv = []
    for i in range(n):
        print(f"\nHo ten sinh vien {i+1}: ", end="")
        hoten = input()
        while True:
            try:
                dtb = float(input("Nhap diem trung binh: "))
                if 0 <= dtb <= 11:
                    break
                else:
                    print("Nhap diem trong khoang 0 den 11")
            except:
                print("Vui long nhap so thuc!")
        sv.append({"hoten": hoten, "dtb": dtb})

    # Sắp xếp giảm dần theo điểm
    sv.sort(key=lambda x: x["dtb"], reverse=True)

    print("\n----------Danh sach sinh vien----------")
    for s in sv:
        print(f"\nSinh vien: {s['hoten']}")
        print(f"Diem trung binh: {s['dtb']:.1f}", end="")
        if s['dtb'] >= 9:
            print(" - Hoc luc xuat sac")
        elif s['dtb'] >= 8:
            print(" - Hoc luc gioi")
        elif s['dtb'] >= 6.5:
            print(" - Hoc luc kha")
        elif s['dtb'] >= 5:
            print(" - Hoc luc trung binh")
        else:
            print(" - Hoc luc yeu")

# Chức năng 9: Game FPOLY-LOTT
def fpoly_lott():
    try:
        numberA = int(input("\nNhap vao so thu 1: "))
        numberB = int(input("Nhap vao so thu 2: "))
    except:
        print("Vui long nhap so nguyen!")
        return

    random.seed(time.time())
    print("Ket qua xo so FPOLY-LOTT")
    print("----------------------")
    count = 0
    for _ in range(2):
        randomNumber = random.randint(1, 15)
        print(f"{randomNumber:10d}", end="")
        if numberA == randomNumber or numberB == randomNumber:
            count += 1
    print("\n----------------------")

    if count == 0:
        print("Chuc ban may man lan sau")
    elif count == 1:
        print("Chuc mung ban da trung giai nhi")
    else:
        print("Chuc mung ban da trung giai nhat")

# Chức năng 10: Tính toán phân số
def tinhToanPhanSo():
    try:
        print("\nNhap vao phan so 1 (tu mau): ", end="")
        tu1, mau1 = map(int, input().split())
        print("Nhap vao phan so 2 (tu mau): ", end="")
        tu2, mau2 = map(int, input().split())
        if mau1 == 0 or mau2 == 0:
            print("Mau so khong duoc bang 0!")
            return
    except:
        print("Vui long nhap dung dinh dang!")
        return

    tong_tu = tu1 * mau2 + tu2 * mau1
    tong_mau = mau1 * mau2
    hieu_tu = tu1 * mau2 - tu2 * mau1
    hieu_mau = mau1 * mau2
    tich_tu = tu1 * tu2
    tich_mau = mau1 * mau2
    thuong_tu = tu1 * mau2
    thuong_mau = mau1 * tu2

    print(f"\nTong 2 phan so: {tong_tu}/{tong_mau}")
    print(f"Hieu 2 phan so: {hieu_tu}/{hieu_mau}")
    print(f"Tich 2 phan so: {tich_tu}/{tich_mau}")
    print(f"Thuong 2 phan so: {thuong_tu}/{thuong_mau}")

# Menu chính
def main():
    while True:
        print("\n+##------------------*Menu*------------------##+")
        print("|1. Kiem tra so nguyen                         |")
        print("|2. Tim uoc so chung va boi so chung cua 2 so  |")
        print("|3. Chuong trinh tinh tien cho quan Karaoke    |")
        print("|4. Tinh tien dien                             |")
        print("|5. Chuc nang doi tien                         |")
        print("|6. Tinh lai xuat vay ngan hang vay tra gop    |")
        print("|7. Vay tien mua xe                            |")
        print("|8. Sap xep thong tin sinh vien                |")
        print("|9. Game FPOLY-LOTT                            |")
        print("|10. Tinh toan phan so                         |")
        print("|11. Thoat chuong trinh                        |")
        print("+##------------------*====*------------------##+")

        try:
            chon = int(input("Nhap chuc nang (1-11): "))
        except:
            print("Vui long nhap so tu 1 den 11!")
            continue

        if chon == 1:
            print("Ban da chon kiem tra so nguyen")
            try:
                number = float(input("Nhap vao so: "))
                ckSoNguyen = checkSN(number)
                if ckSoNguyen > 0:
                    print(f"{number:.2f} la so nguyen, ", end="")
                    checkSoNguyenTo(int(number))
                    soChinhPhuong(int(number))
                else:
                    print(f"{number:.2f} khong phai so nguyen")
            except:
                print("Vui long nhap so hop le!")

        elif chon == 2:
            print("Ban da chon tim uoc so chung va boi so chung cua 2 so")
            try:
                x, y = map(int, input("Nhap vao 2 so: ").split())
                ucln = timUocChungLonNhat(x, y)
                bcnn = timBoiChungLonNhat(x, y)
                print(f"Uoc chung lon nhat cua {x} va {y}: {ucln}")
                print(f"Boi chung lon nhat cua {x} va {y}: {bcnn}")
            except:
                print("Vui long nhap 2 so nguyen!")

        elif chon == 3:
            print("Ban da chon tinh tien karaoke")
            tinhTienKaraoke()

        elif chon == 4:
            print("Ban da chon chuc nang tinh tien dien")
            tinhTienDien()

        elif chon == 5:
            print("Ban da chon chuc nang doi tien")
            try:
                amount = int(input("Nhap menh gia tien can doi: "))
                if amount >= 0:
                    doiTien(amount)
                else:
                    print("Ban can nhap so tien lon hon hoac bang 0")
            except:
                print("Vui long nhap so nguyen!")

        elif chon == 6:
            print("Ban da chon tinh lai xuat vay ngan hang vay tra gop")
            tinhLaiSuatVay()

        elif chon == 7:
            print("Ban da chon vay tien mua xe")
            vayTienMuaXe()

        elif chon == 8:
            print("Ban da chon sap xep thong tin sinh vien")
            thongTinSV()

        elif chon == 9:
            print("Ban da chon game FPOLY-LOTT")
            fpoly_lott()

        elif chon == 10:
            print("Ban da chon tinh toan phan so")
            tinhToanPhanSo()

        elif chon == 11:
            print("Ban da chon thoat chuong trinh")
            break

        else:
            print("Chuc nang khong hop le! Vui long chon lai.")

        input("\nNhan Enter de tiep tuc...")

if __name__ == "__main__":
    main()