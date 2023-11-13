#cach1
# n=input('nhap day so')
# tong=0
# tach=n.split(',')
# print(tach)
# for i in tach:
#     tong+=int(i)
# print(tong)

#cach2
# arr=[1,2,3,4]
# print(sum(arr))

#cach3
n=input('nhap day so')
lst=list(map(int,n.split(',')))# hàm map() để chuyển chuỗi thành danh sách số
print(sum(lst))
