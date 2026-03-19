total_students = 30
total_days = 5

attendance_list = []

# Taking attendance
for i in range(1, total_students + 1):
    print("Student", i)
    student_record = []

    for j in range(1, total_days + 1):
        a = int(input("Enter attendance for Day " + str(j) + " (1/0): "))
        student_record.append(a)

    attendance_list.append(student_record)

# Counting total present
total_present = 0

for student_record in attendance_list:
    for day_attendance in student_record:
        total_present = total_present + day_attendance

# Calculating percentage
total_classes = total_students * total_days
percentage = (total_present / total_classes) * 100

print("Attendance Percentage =", percentage, "%")