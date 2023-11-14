def rut_gon_phan_so(tu, mau):
    ucln = 1
    for i in range(2, min(abs(tu), abs(mau)) + 1):
        if tu % i == 0 and mau % i == 0:
            ucln = i
# rút gọn phân số
    tu_rut_gon = tu // ucln
    mau_rut_gon = mau // ucln
# Xuất phân số đã rút gọn
    print(tu, "/", mau, "=", tu_rut_gon, "/", mau_rut_gon)

def tinh_tong_phan_so(tu1, mau1, tu2, mau2):
    # tính tổng phân số
    tu_tong =  tu1 * mau2 + tu2 * mau1
    mau_tong = mau1 * mau2
    # rút gọn phân số
    rut_gon_phan_so(tu_tong, mau_tong)

tu1 = int(input("Nhập tử số thứ nhất: "))
mau1 = int(input("Nhập mẫu số thứ nhất: "))
tu2 = int(input("Nhập tử số thứ hai: "))
mau2 = int(input("Nhập mẫu số thứ hai: "))

print("Tổng hai phân số: ")
tinh_tong_phan_so(tu1, mau1, tu2, mau2)