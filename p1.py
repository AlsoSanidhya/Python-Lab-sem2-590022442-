students = 5
days = 5
total_present = 0

for student in range(1, students + 1):
    print("\nStudent", student)
    
    for day in range(1, days + 1):
        attendance = int(input("Enter attendance for day " + str(day) + " (1=Present, 0=Absent): "))
        total_present = total_present + attendance

total_classes = students * days
percentage = (total_present / total_classes) * 100

print("\nTotal Attendance Percentage of the Class =", percentage, "%")
1