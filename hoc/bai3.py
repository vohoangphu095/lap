
student_heights = input("Input a list of student heights ").split()#tach chuoi thanh danh sach
#split(',' tach chuoi co dau phay)
total = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

    total += student_heights[n]
print('total of student heights: ', round(total / len(student_heights)))

maxv= None
for n in student_heights:
    if maxv is None or n>maxv:
        maxv=n
print('max la',maxv)

minv= None
for n in student_heights:
    if minv is None or n<minv:
        minv=n
print('min la',minv)


#tong so le 1-100
tong = 0
for n in range(1,101,2):# hoac range(99,0,-2)
    tong +=n
print(tong)

