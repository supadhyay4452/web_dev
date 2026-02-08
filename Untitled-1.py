def total(marks):
    return sum(marks)

students = []

count = int(input("Enter number of students: "))

for i in range(count):
    print(f"\nStudent {i+1}")
    name = input("Enter name: ")
    n = int(input("Enter number of subjects: "))

    marks = []
    for j in range(n):
        m = int(input(f"Subject {j+1} marks: "))
        marks.append(m)

    total_marks = total(marks)
    average = total_marks / n
    status = "Pass" if average >= 40 else "Fail"

    students.append({
        "name": name,
        "marks": marks,
        "total": total_marks,
        "average": average,
        "status": status
    })

students.sort(key=lambda x: x["average"], reverse=True)
top_student=students[0]

print("\n--- Student Report ---")
for s in students:
    print(s)
print("\n-----top student--")
print("Name :",top_student["name"])
print("Marks :",top_student["marks"])
print("Average :",top_student["average"])
print("Status:",top_student["status"])