def mayTinh():
    try:
        a = float(input("Nhap vao so thu nhat: "))
        b = float(input("Nhap vao so thu hai: "))
        phepTinh = input("Nhap vao phep tinh (+ - * /): ").strip()

        if phepTinh not in ['+', '-', '*', '/']:
            print("Phep tinh khong hop le!")
            return

        if phepTinh == '+':
            c = a + b
        elif phepTinh == '-':
            c = a - b
        elif phepTinh == '*':
            c = a * b
        elif phepTinh == '/':
            if b == 0:
                print("Khong the chia cho 0!")
                return
            else:
                c = a / b

        print(f"{a} {phepTinh} {b} = {c}")

    except ValueError:
        print("Vui long nhap so hop le!")


def chuViDienTich():
    print("1. Chu vi dien tich hinh vuong")
    print("2. Chu vi dien tich hinh chu nhat")
    print("3. Chu vi dien tich tam giac vuong")

    try:
        luaChon = input("Chon hinh muon tinh (1-3): ").strip()

        if luaChon == '1':
            canh = float(input("Nhap canh hinh vuong (cm): "))
            chuVi = canh * 4
            dienTich = canh ** 2
            print(f"Chu vi hinh vuong: {chuVi} cm")
            print(f"Dien tich hinh vuong: {dienTich} cm²")

        elif luaChon == '2':
            dai = float(input("Nhap chieu dai (cm): "))
            rong = float(input("Nhap chieu rong (cm): "))
            chuVi = (dai + rong) * 2
            dienTich = dai * rong
            print(f"Chu vi hinh chu nhat: {chuVi} cm")
            print(f"Dien tich hinh chu nhat: {dienTich} cm²")

        elif luaChon == '3':
            a = float(input("Nhap canh thuong (cm): "))
            b = float(input("Nhap canh ke (cm): "))
            import math
            canhHuyen = math.sqrt(a ** 2 + b ** 2)
            chuVi = a + b + canhHuyen
            dienTich = (a * b) / 2
            print(f"Chu vi tam giac vuong: {chuVi:.2f} cm")
            print(f"Dien tich tam giac vuong: {dienTich:.2f} cm²")

        else:
            print("Lua chon khong hop le!")

    except ValueError:
        print("Vui long nhap so hop le!")


def formatString():
    danhSachChuoi = []

    while True:
        chuoi = input("Nhap chuoi (x de ket thuc): ").strip()
        if chuoi.lower() == 'x':
            break
        if not chuoi:
            continue

        danhSachChuoi.append(chuoi)

    print("\n1. Format uppercase")
    print("2. Format lowercase")
    print("3. Format swapcase")

    try:
        luaChon = input("Chon cach format (1-3): ").strip()

        danhSachKetQua = []
        for chuoi in danhSachChuoi:
            if luaChon == '1':
                ketQua = chuoi.upper()
            elif luaChon == '2':
                ketQua = chuoi.lower()
            elif luaChon == '3':
                ketQua = chuoi.swapcase()
            else:
                print("Lua chon khong hop le!")
                return
            danhSachKetQua.append(ketQua)

        print("\n--- Ket qua ---")
        for i in range(len(danhSachChuoi)):
            print(f"Chuoi ban dau: '{danhSachChuoi[i]}' → Format: '{danhSachKetQua[i]}'")

    except Exception as e:
        print(f"Loi: {e}")

def maxAndAvg():
    danhSachSo = []

    while True:
        soNhap = input("Nhap danh sach so(x de huy): ")

        if soNhap == 'x':
            break

        try:
            so = float(soNhap)
            danhSachSo.append(so)
        except ValueError:
            print("So nhap ko hop le")

    tong = sum(danhSachSo)
    soLuong = len(danhSachSo)
    trungBinh = tong / soLuong

    print(f"Danh sach do ban dau: {danhSachSo}")
    print(f"Tong: {tong}")
    print(f"So luong: {soLuong}")
    print(f"Trung binh: {trungBinh}")


while True:
    print("\n" + "=" * 40)
    print("1. May tinh")
    print("2. Chu vi dien tich")
    print("3. Dinh dang chuoi")
    print("4. Trung binh")
    print("5. Thoat")
    print("=" * 40)

    try:
        option = int(input("Chon chuc nang (1-5): "))

        if option == 1:
            mayTinh()
        elif option == 2:
            chuViDienTich()
        elif option == 3:
            formatString()
        elif option == 4:
            maxAndAvg()
        elif option == 5:
            print("Ket thuc chuong trinh")
            break
        else:
            print("Vui long chon tu 1 den 5!")

    except ValueError:
        print("Vui long nhap so nguyen!")
