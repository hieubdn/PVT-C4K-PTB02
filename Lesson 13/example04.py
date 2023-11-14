def dien_tich_phong(canh):
    return canh * canh
def so_vien_gach(dien_tich_phong, dien_tich_vien_gach):
    return dien_tich_phong / dien_tich_vien_gach

canh_can_phong = 80
s_phong = dien_tich_phong(canh_can_phong)
s_vien_gach = 0.4
so_luong_can = so_vien_gach(s_phong, s_vien_gach)
print(f"Với phòng có diện tích {s_phong} m^2, thì cần {so_luong_can} viên gạch")

