class DongVat:
    def __init__(self, ten_dong_vat, mau_long, hanh_dong):
        self.ten_dong_vat = ten_dong_vat
        self.mau_long = mau_long
        self.hanh_dong = hanh_dong

class Meo(DongVat):
    def __init__(self, ten_dong_vat, mau_long, hanh_dong, loai_meo):
        super().__init__(ten_dong_vat, mau_long, hanh_dong)
        self.loai_meo = loai_meo

    def hien_thi_meow(self):
        print(f"Loai meo: {self.loai_meo}, mau long: {self.mau_long}")

class Cho(DongVat):
    def __init__(self, ten_dong_vat, mau_long, hanh_dong, loai_cho):
        super().__init__(ten_dong_vat, mau_long, hanh_dong)
        self.loai_cho = loai_cho

    def hien_thi_gau(self):
        print(f"Loai cho: {self.loai_cho}, mau long: {self.mau_long}")