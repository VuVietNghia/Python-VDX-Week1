import math

luaChonInput = input("Nhap lua chon(1. May tinh co ban, 2. Tinh chu vi dien tich, 3. Format chuoi ki tu): ")
luaChon = int(luaChonInput)

def mayTinh():
    so1 = float(input("Nhap so a: "))

    so2 = float(input("Nhap so b: "))

    phepTinh = input("Nhap phep tinh(+ - * /): ")
    so3 = None

    if phepTinh == '+':
        so3 = so1 + so2
    elif phepTinh == '-':
        so3 = so1 - so2
    elif phepTinh == '*':
        so3 = so1 * so2
    elif phepTinh == '/':
        if so2 == 0:
            print("Khong the chia cho 0")
            return
        else:
            so3 = so1 / so2

    print(f"{so1} {phepTinh} {so2} = {so3}")

def mayTinhHinhHoc():
    option = input("Nhap lua chon(1. Hinh vuong, 2. Hinh chu nhat, 3. Tam giac vuong): ")

    if option == '1':
        canhVuong = float(input("Nhap canh vuong: "))
        chuViHinhVuong = canhVuong * 4
        dienTichHinhVuong = canhVuong ** 2
        print(f"Chu vi hinh vuong: {chuViHinhVuong}")
        print(f"Dien tich hinh vuong: {dienTichHinhVuong}")
    elif option == '2':
        canhDai = float(input("Nhap canh dai: "))
        canhRong = float(input("Nhap canh rong: "))
        chuViHinhChuNhat = (canhDai + canhRong) * 2
        dienTichChuNhat = canhDai * canhRong
        print(f"Chu vi hinh chu nhat: {chuViHinhChuNhat}")
        print(f"Dien tich hinh chu nhat: {dienTichChuNhat}")
    elif option == '3':
        canhGocVuong1 = float(input("Nhap canh goc vuong 1: "))
        canhGocVuong2 = float(input("Nhap canh goc vuong 2: "))
        dienTichTamGiac = (canhGocVuong1 * canhGocVuong2) / 2
        chuViTamGiac = canhGocVuong1 + canhGocVuong2 + math.sqrt(canhGocVuong1 ** 2 + canhGocVuong2 ** 2)
        print(f"Dien tich tam giac vuong: {dienTichTamGiac}")
        print(f"Chu vi tam giac vuong: {chuViTamGiac}")
    else:
        print("Vui long nhap tu 1 - 3")

def dinhDangChuoi():
    danhSachChuoi = []
    while True:
        chuoi = input("Nhap chuoi ki tu (nhap 'x' de ket thuc): ")
        if chuoi.lower() == 'x':
            break
        if chuoi:  # Chỉ thêm chuỗi không rỗng vào danh sách
            danhSachChuoi.append(chuoi)
    
    if not danhSachChuoi:
        print("Khong co chuoi nao duoc nhap!")
        return
    
    luaChon = input("Nhap lua chon format du lieu(1. uppercase, 2. lowercase, 3. swapcase): ")
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
    
    print(f"Chuoi ban dau: {danhSachChuoi}")
    print(f"Chuoi da format: {danhSachKetQua}")

match luaChon:
    case 1:
        mayTinh()
    case 2:
        mayTinhHinhHoc()
    case 3:
        dinhDangChuoi()
    case _:
        print("Lua chon khong hop le")