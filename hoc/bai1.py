# tim chan le

n = int(input('nhap n '))
if n % 2 == 0:
    print(f'{n} la so chan')
else:
    print(f'{n} la so le')

# tim nam nhuan

nam = int(input(' nhap nam '))
if nam % 4 == 0:
    if nam % 100 == 0:
        if nam % 400 == 0:
            print(f'{nam} la nam nhuan')
        else:
            print(f'{nam} ko phai la nam nhuan')
    else:
        print(f'{nam} la nam nhuan')
else:
    print(f'{nam} ko phai nam nhuan')
