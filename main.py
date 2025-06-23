import csv
from tabulate import tabulate

FILENAME = "students.csv"

def load_students():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_students(students):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['Name', 'ID', 'Math', 'Physics', 'Chemistry', 'GPA']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def calculate_gpa(marks):
    avg = sum(marks) / len(marks)
    if avg >= 80:
        return 4.0
    elif avg >= 70:
        return 3.5
    elif avg >= 60:
        return 3.0
    elif avg >= 50:
        return 2.5
    else:
        return 2.0

def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    math = float(input("Math marks: "))
    physics = float(input("Physics marks: "))
    chemistry = float(input("Chemistry marks: "))
    gpa = calculate_gpa([math, physics, chemistry])
    student = {
        'Name': name,
        'ID': student_id,
        'Math': math,
        'Physics': physics,
        'Chemistry': chemistry,
        'GPA': round(gpa, 2)
    }
    students = load_students()
    students.append(student)
    save_students(students)
    print("✅ Student added successfully!\n")

def view_students():
    students = load_students()
    if students:
        print(tabulate(students, headers="keys", tablefmt="grid"))
    else:
        print("❗ No student records found.\n")

def menu():
    while True:
        print("\n🎓 Student Result Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("👋 Exiting... Bye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
