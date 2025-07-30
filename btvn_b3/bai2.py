k = int ( input( " Nhập số phần tử của list : ")) 

a = [] 
for i in range ( k ) : 
    so = int ( input ( f'Nhập phần tử thứ { i + 1 } : ')) 
    a.append( so ) 

print ( " List đã nhập : " , a ) 

n = int ( input (" Nhập n : ")) 
m = int ( input( " NHập m : "))

if n * m > k:
    print("NO")
else:
    X = []
    index = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[index])
            index += 1
        X.append(row)
    
    print("Ma trận thu được là:")
    for row in X:
        print(row)