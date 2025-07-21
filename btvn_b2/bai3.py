def dem_va_tinh_tong_chu_so(n):
    # Đổi số n thành chuỗi để xử lý
    chuoi_n = str(n)

    so_chu_so = len(chuoi_n)

    tong = sum(int(ch) for ch in chuoi_n)

    # In kết quả
    print(f"Số chữ số: {so_chu_so} Tổng chữ số: {tong}")

# Test
dem_va_tinh_tong_chu_so(54)
