users={}
students={}
attendance_records={}

file = open('geek.txt', 'r')
def register_user(username,password):
    if username not in users:
        users[username]=password
        return True
print (file.read())   

def login_user(username,password):
    if username in users and users[username]==password:
        return True
    return False

def add_student(student_id,name):
    students[student_id]=name

def view_students():
    print("StudentID \t Name")
    for student_id,name in students.items():
        print(f"{student_id } \t\t {name}")

def update_student(student_id , name):
    if student_id in students:
        students[student_id]=name
        return True
    return False

def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        for date,attendance_list in attendance_records.items():
            attendance_records[date]=[record for record in attendance_list if record['student_id']!=student_id]
        return True
    return False

def mark_attendance(date, student_ids):
    if date not in attendance_records:
        attendance_records[date] = []

    for student_id in student_ids:
        if student_id in students:
            attendance_records[date].append({'student_id': student_id, 'status': 'Present'})
        else:
            print(f"Student with ID {student_id} does not exist.")

def view_attendance(date):
    if date in attendance_records:
        print(f"Attendance for {date}:")
        for record in attendance_records[date]:
            student_id = record['student_id']
            status = record['status']
            name = students.get(student_id, "Unknown")
            print(f"Student ID: {student_id} \t Name: {name} \t Status: {status}")
    else:
        print("No attendance records for this date.")


def view_student_attendance(student_id): 
    print(f"Attendance records for Student ID: {student_id}")
    for date, attendance_list in attendance_records.items():
        for record in attendance_list:
            if record['student_id'] == student_id:
                status = record['status']
                print(f"Date: {date} \t Status: {status}")
                break
        else:
            print(f"No attendance record found for Student ID: {student_id}")


def generate_report():
    print("Attendance Report:")
    print("Date \t\t Present Count")
    for date, attendance_list in attendance_records.items():
        present_count = sum(1 for record in attendance_list if record['status'] == 'Present')
        print(f"{date} \t {present_count}")

def main():
    is_logged_in=False
    while True:
        print("\nAttendance Management System")
        if not is_logged_in:
            print("1.REGISTER USER")
            print("2.LOGIN")
        else:
            print("3.ADD")
            print("4.VIEW")
            print("5.UPDATE")
            print("6.DELETE")
            print("7.MARK ATTENDANCE")
            print("8.VIEW ATTENDANCE")
            print("9.VIEW STUDENT ATTENDANCE")
            print("10.GENERATE REPORT")
            print("11.LOGOUT")
            
        
        print("12.Exit")
        choice=int(input("Enter your choice:"))
        if not is_logged_in:
            if choice == 1:
                username = input("Enter username: ")
                password = input("Enter password: ")
                if register_user(username, password):
                    print("User registration successful.")
                else:
                    print("Username already exists.")
            elif choice == 2:
                username = input("Enter username: ")
                password = input("Enter password: ")
                if login_user(username, password):
                    is_logged_in = True  # Set is_logged_in to True on successful login
                    print("Login successful.")
                else:
                    print("Invalid username or password.")
            
        else: 
            if choice==3:
                student_id=input("Enter student id:")
                student_name=input("Enter student name:")
                add_student(student_id,student_name)
                print("student data added successfully")
            elif choice == 4:
                view_students()
            elif choice == 5:
                student_id=input("Enter student Id to update:")
                name=input("Enter student name:")
                if update_student(student_id,name):
                    print("student information updated successfully")
                else:
                    print("Student with specificed ID not found")
            elif choice == 6:
                 student_id=input("Enter student ID to delete:")
                 if delete_student(student_id):
                     print("student data deleted successfully")
                 else:
                     print("Student data not found")
            elif choice == 7:
                date = input("Enter date (YYYY-MM-DD): ")
                student_ids = input("Enter comma-separated student IDs: ").split(',')
                mark_attendance(date, student_ids)
            elif choice == 8:
                date = input("Enter date (YYYY-MM-DD) to view attendance: ")
                view_attendance(date)
            elif choice == 9:
                student_id = input("Enter student ID to view attendance: ")
                view_student_attendance(student_id)
            elif choice == 10:
                generate_report()
            elif choice == 11:
                is_logged_in = False
                print("Logged out successfully.")
            elif choice == 12:
                print("Exiting the Attendance Management System.")
                break
            else:
                print("Invalid choice. Please try again.")
main()                   