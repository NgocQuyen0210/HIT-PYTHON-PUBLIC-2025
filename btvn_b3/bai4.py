def chuan_hoa ( ho_ten ) :  
    # xóa khỏag trống , đưa về chữ thường 
    ho_ten = ho_ten.strip().lower()  

    # tách từ 
    tu = ho_ten.split() 

    # viết hoa chữ đầu 
    chuan_hoa = ' '.join(word.capitalize() for word in tu)
    
    return chuan_hoa

input_name = input("Nhập họ tên cần chuẩn hóa: ")
output_name = chuan_hoa(input_name)

# In ra kết quả
print("Họ tên sau khi chuẩn hóa:", output_name)