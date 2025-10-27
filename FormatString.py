def formatString():
    danhSachChuoi = []
    while True:
        chuoi = input("Nhap danh sach chuoi (Nhap 'x' de huy): ")

        if chuoi.lower() == 'x':
            break
        if chuoi:
            danhSachChuoi.append(chuoi)

    if not danhSachChuoi:
        print("Chuoi trong")
        return

    luachon = input("Chon format chuoi (1. Uppercase, 2. Lowercase, 3. Swapcase): ")
    danhSachKetQua = []

    for chuoi in danhSachChuoi:
        if luachon == '1':
            ketQua = chuoi.upper()
        elif luachon == '2':
            ketQua = chuoi.lower()
        elif luachon == '3':
            ketQua = chuoi.swapcase()
        else:
            print("Ko phai lua chon tu 1 - 3")
            return
        danhSachKetQua.append(ketQua)

    print(f"Danh sach ban dau: {danhSachChuoi}")
    print(f"Danh sach ket qua: {danhSachKetQua}")
formatString()