student = ["sajid",90,22,"delhi"];
print(student[0])
student[0] = "yash" #chnaged the data
print(student)

#**************list slicing**********

marks = [23,45,67,8,9]
print(marks[1:4])

marks.append(4)
print(marks)

marks.sort() #sort in accending
print(marks)

marks.sort(reverse=True) #sort in decending
print(marks)

marks.reverse()
print(marks)

marks.insert(2,3)
print(marks)

marks.pop(4)
print(marks) 