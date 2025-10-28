def dinhDangChuoi():
    danhSachChuoi = []
    while True:
        chuoi = input("Nhap chuoi vao danh sach (nhap x de hoan thanh): ")

        if chuoi.lower() == 'x':
            break
        if chuoi:
            danhSachChuoi.append(chuoi)
    if not danhSachChuoi:
        print("Danh sach chuoi rong.")
        return
    
    luaChon = input("Chon kieu format (1. upper, 2. lower, 3. swapcase): ")
    danhSachKetQua = []

    for chuoi in danhSachChuoi:
        if luaChon == '1':
            ketQua = chuoi.upper()
        elif luaChon == '2':
            ketQua = chuoi.lower()
        elif luaChon == '3':
            ketQua = chuoi.swapcase()
        else:
            print("Lua chon khong hop le.")
            return
        
        danhSachKetQua.append(ketQua)

    print(f"Danh sach chuoi ban dau: {danhSachChuoi}")
    print(f"Danh sach chuoi da format: {danhSachKetQua}")
dinhDangChuoi()