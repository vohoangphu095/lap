from math import sqrt

n=int(input("nhap 1 so: "))
def check_snt(n):
    if n<2:
        return False
    else:
        for i in range(2,int(sqrt(n)+1)):
            if n%i==0:
                return False
        return True

a=check_snt(n)
if a==True:
    print('day la snt')
else:
    print('khong')
