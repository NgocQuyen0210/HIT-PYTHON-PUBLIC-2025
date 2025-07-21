def tinh_thue_va_luong_rong(luong):
    # Xác định mức thuế
    if luong >= 15000000:
        thue = luong * 0.30
    elif luong >= 7000000:
        thue = luong * 0.20
    else:
        thue = luong * 0.10

    # Tính lương ròng
    luong_rong = luong - thue

    # In kết quả
    print(f"Thuế: {float(thue)} Thu nhập: {float(luong_rong)}")
tinh_thue_va_luong_rong(5000000)  # Output: Thuế: 500000 Thu nhập: 4500000
