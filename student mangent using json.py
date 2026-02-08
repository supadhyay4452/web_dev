import json
def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


    

def total(marks):
    return sum(marks)


students =load_students()

while True:
    print("\n--- MENU ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Show Topper")
    print("4. Show Failing Students")
    print("5. Average of all students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        n = int(input("Enter number of subjects: "))

        marks = []
        for j in range(n):
            m = int(input(f"Subject {j+1} marks: "))
            marks.append(m)

        total_marks = total(marks)
        avg = total_marks / n
        status = "Pass" if avg >= 40 else "Fail"

        students.append({
            "name": name,
            "marks": marks,
            "total": total_marks,
            "average": avg,
            "status": status
        })

        print("Student added successfully ✅")

    elif choice == "2":
        print("\n--- All Students ---")
        for s in students:
            print(s)

    elif choice == "3":
        if students:
            topper = max(students, key=lambda x: x["average"])
            print("\n--- Topper ---")
            print("Name:", topper["name"])
            print("Average:", topper["average"])
            print("Status:", topper["status"])
        else:
            print("No students added yet")

    elif choice == "4":
        print("\n--- Failing Students ---")
        found = False
        for s in students:
            if s["status"] == "Fail":
                print("Name:", s["name"], "| Avg:", s["average"])
                found = True
        if not found:
            print("No failing students 🎉")

    elif choice == "5":
        print("----Average of all students---")
        if students:
            total_avg=0
            for s in students:
                total_avg +=s["average"]
            class_avg = total_avg / len(students)
            print("Average of all students:", class_avg)
        else:print("No students available")


    elif choice == "6":
        save_students(students)
        print("Data saved to JSON. Exiting 👋")
        break



    else:
        print("Invalid choice")
