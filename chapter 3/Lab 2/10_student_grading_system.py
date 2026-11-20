name = input("Enter student name: ")

marks = []

for i in range(1, 4):
    mark = float(input("Enter marks for subject " + str(i) + ": "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A"

elif average >= 80:
    grade = "B"

elif average >= 70:
    grade = "C"

elif average >= 60:
    grade = "D"

else:
    grade = "F"

print("\nStudent:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)