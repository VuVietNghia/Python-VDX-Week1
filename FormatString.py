def formatString():
    while True:
        danhSachChuoi = input("Nhap chuoi ki tu(nhap x de huy): ")

        if danhSachChuoi.lower() == 'x':
            return
        if danhSachChuoi:
            break

    luaChon = input("Nhap lua chon format du lieu(1. uppercase, 2. lowercase, 3. swapcase): ")

    if luaChon == '1':
        ketQua = danhSachChuoi.upper()
    elif luaChon == '2':
        ketQua = danhSachChuoi.lower()
    elif luaChon == '3':
        ketQua = danhSachChuoi.swapcase()

    print(f"Chuoi ban dau: {danhSachChuoi}")
    print(f"Chuoi da format: {ketQua}")
formatString()