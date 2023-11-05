from math import sqrt

n = int(input('nhap n: '))
tong = 0
def checkPrimenum(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return n

for i in range (2,n+1):
    if checkPrimenum(i):
        tong+=i
print(tong)