N = int ( input( " Nhập số lượng phần tử của list : ")) 

lst = [ ] 
for i in range (N) : 
    so = int ( input(f'Nhập phần tử thứ { i + 1 } : '))
    lst.append(so ) 
print ( 'List đã nhập : ' , lst)
print(" ------------------")

X = int( input("Nhập số X : ")) 
xuat_hien = lst.count(X) 
print ( f'Số {X } xuất hiện {xuat_hien} lần trong List ') 
print(" ------------------")

# Thay thế phần tử từ vị trí 2 -> 7 (chỉ khi đủ độ dài)
if len(lst) >= 8:
    lst[2:8] = [8, 5, 4, 0, 1, 3]
else:
    print("List không đủ độ dài để thay thế từ vị trí 2 đến 7.")

print("List sau khi thay thế:", lst) 
print(" ------------------")

lon_nhat = max(lst ) 
nho_nhat = min( lst ) 

print ( " Số lớn nhất trong List : " , lon_nhat) 
print ( " Số nhỏ nhất trong list : " , nho_nhat )
print(" ------------------")

Y = int ( input ( " Nhập số Y : "))
lst.insert( 0 , Y ) 
print ( f" List sau khi chèn thêm {Y } : " , lst) 
print(" ------------------")


is_tang = all ( lst[i] < lst[ i + 1 ] for i in range ( len ( lst) - 1 )) 
is_giam = all ( lst[i] > lst [ i + 1 ] for i in range ( len( lst) - 1 )) 

if is_tang : 
    print ( " TĂNG ") 
elif is_giam : 
    print ( " GIẢM ") 

else : 
    print ( " NO ")
print(" ------------------")