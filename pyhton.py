def total(marks):
    t = 0
    for n in marks:
        t += n
    return t

# List to store all students
students = []

# Number of students
num_students = int(input("Enter how many students are coming: "))

for s in range(num_students):
    print(f"\nStudent {s+1}:")
    name = input("Enter your name: ")
    n = int(input("Enter number of subjects: "))
    marks = []
    
    for i in range(n):
        k = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(k)
    
    total_marks = total(marks)
    average = total_marks / n
    status = "Pass" if average >= 40 else "Fail"
    
    student = {
        "name": name,
        "marks": marks,
        "total": total_marks,
        "average": average,
        "status": status
    }
    students.append(student)

# Sort students by average descending
students.sort(key=lambda x: x["average"], reverse=True)
top_student = students[0]
fstudents=[]
for student in students:
    if student["status"] == "Fail":
        fstudents.append(student)

    student.append(fstudents)



print("\nTop Student")
print("Name:", top_student["name"])
print("Average:", top_student["average"])
print("Status:", top_student["status"])

#  failing students name
print("\nFailing Students")
if len(fstudents) == 0:
    print("No failing students")
else:
    for fs in fstudents:
        print("Name:", fs["name"], "| Average:", fs["average"])



# Print all results
print("\n--- All Student Results ---")
for student in students:
    print("\nName:", student["name"])
    print("Marks:", student["marks"])
    print("Total:", student["total"])
    print("Average:", student["average"])
    print("Status:", student["status"])
