def tinh_so_chai_bia(n_xu):
    # Bước 1: Mua ban đầu
    gia_bia = 28
    bia_mua = n_xu // gia_bia
    tong_bia = bia_mua
    vo_chai = bia_mua

    # Bước 2: Đổi vỏ chai thành bia mới
    while vo_chai >= 3:
        bia_doi = vo_chai // 3
        tong_bia += bia_doi
        vo_chai = bia_doi + (vo_chai % 3)  # Vỏ mới + vỏ dư

    print(f"Số chai bia có thể mua được là: {tong_bia}")

# Test theo đề bài
tinh_so_chai_bia(28)  # Output: Số chai bia có thể mua được là: 1
