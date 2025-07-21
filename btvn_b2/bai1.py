def songaytrongthang(thang, nam):
    if(nam % 4==0 and nam % 100 !=0) or (nam %400 ==0):
        namnhuan=True
    else:
        namnhuan=False;
    #ktra thang
    if thang in [1,3,5,7,8,10,12]:
        return 31
    elif thang in [4,6,9,11]:
        return 30
    elif thang ==2:
        return 29
    else:
        print(" thang k hop le ")
print("test 1 :", songaytrongthang(10,2021))


