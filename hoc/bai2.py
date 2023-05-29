
# tim nam nhuan

nam = int(input('Nhap nam : '))
if nam % 4 == 0:
    if nam % 100 == 0:
        if nam % 400 == 0:
            print(f'Nam {nam} la nam nhuan')
        else:
            print(f'Nam {nam} ko phai la nam nhuan')
    else:
        print(f'Nam {nam} la nam nhuan')
else:
    print(f'Nam {nam} ko phai nam nhuan')

n=int(input(' nhan n'))
if n%4==0:
    print('day la nam nhuan')
elif n%100==0:
    print('ko phai nam nhuan')
elif n%100==0 and n%400==0:
    print('nam nhuan')