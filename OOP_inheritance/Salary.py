class Nhanvien:
    def __init__(self, ten, lcb, so_ngay, hsl, hshq, thang) -> None:
        self.ten = ten
        self.lcb = lcb
        self.so_ngay = so_ngay
        self.hsl = hsl
        self.hshq = hshq
        self.thang = thang

    def __str__(self) -> str:
        return f"""Tên quản lý: '{self.ten}'
Tháng: {self.thang}
Lương cơ bản: {self.lcb} VND/ngày
Số ngày làm việc: {self.so_ngay}
Hệ số lương: {self.hsl}
Hệ số hiệu quả: {self.hshq}"""

    def ting_luong(self):
        luong_tong_chua_thuong = self.lcb * self.so_ngay * self.hsl - 1_000_000

        luong_nhan_chua_thuong = luong_tong_chua_thuong
        
        if luong_tong_chua_thuong > 9_000_000:
            luong_nhan_chua_thuong = 0.9 * luong_tong_chua_thuong

        luong_thuc_nhan = luong_nhan_chua_thuong * self.hshq

        if self.hshq < 1:
            luong_thuong = self.tinh_luong_thuong(luong_tong_chua_thuong)
            luong_thuc_nhan = luong_nhan_chua_thuong + luong_thuong

        return luong_thuc_nhan
    

    def hien_thi_luong(self):
        luong = int(self.ting_luong())
        luong_as_str = format(luong, ',d').replace(',', '.')
        print(f"Luong cua nhan vien {self.ten} nhan duoc trong thang {self.thang} la: {luong_as_str} VND.")

    
    def tinh_luong_thuong(self, luong_tong_chua_thuong):
       return luong_tong_chua_thuong * (self.hshq - 1) * 0.85

class QuanLy(Nhanvien):
    pass


ten = input("Nhap vao ten: ")
thang = input("Nhap vao thang: ")
lcb = int(input("Nhap vao lcb: "))
so_ngay = int(input("Nhap vao so ngay: "))
hsl = float(input("Nhap vao hsl: "))
hshq = float(input("Nhap vao hshq: "))

nhan_vien = Nhanvien(ten, lcb, so_ngay, hsl, hshq, thang)
nhan_vien.hien_thi_luong()


"""
1. Input: "Nguyen Hai Dang", "4 1000000 15 1.7 1.5"
Output: "Luong cua nhan vien Nguyen Hai Dang nhan duoc trong thang 4 la: 32.462.500 VND."


2. Input: "Nguyen Hai Quang", "6 1000000 20 1.8 1.9"
Output: "Luong cua nhan vien Nguyen Hai Quang nhan duoc trong thang 6 la: 58.275.000 VND."

3. Input: "Nguyen Thi Yen", "2 1000000 25 1.5 1.3"
Output: "Luong cua nhan vien Nguyen Thi Yen nhan duoc trong thang 2 la: 42.157.500 VND."

"""