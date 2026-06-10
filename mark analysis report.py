"""
n=int(input("enter no: of students"))
students=[]
for i in range(n):
    student_name=input("enter student name")
    marks=int(input("enter student marks"))
    students.append(marks)
print("max marks",max(students))
print("min marks",min(students))
print("total",sum(students))
avg=sum(students)//n
print("avg",avg)
"""
#MARKS ANALYSIS REPORT
"""
students=int(input("enter number of students"))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"enter the marks of students {i}"))
    marks.append(mark)
for i in marks:
    print(i)
print("Marks Analysis Report.............")
print("highest marks",max(marks))
print("lowest marks",min(marks))
print("total marks",sum(marks))
print("average marks",sum(marks)/students)
"""
