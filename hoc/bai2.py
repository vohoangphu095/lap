
student_heights = input("Input a list of student heights ").split()
average = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

    average += student_heights[n]
print('average of student heights: ', average / len(student_heights))


