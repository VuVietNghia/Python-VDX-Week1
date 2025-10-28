def maxAndAvg():
    danhSachSo = []

    while True:
        nhapSo = input("Nhap so vao danh sach(nhap x de hoan thanh): ")

        if nhapSo == 'x':
            break

        try:
            so = float(nhapSo)
            danhSachSo.append(so)
        except ValueError:
            print("So nhap ko hop le")

    tong = sum(danhSachSo)
    soLuong = len(danhSachSo)
    trungBinh = tong / soLuong

    print(f"So luong so trong list: {soLuong}")
    print(f"Tong: {tong}")
    print(f"Trung binh: {trungBinh}")
maxAndAvg()
