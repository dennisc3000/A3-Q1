
import os
import psycopg2


# Connect to the PostgreSQL database
def connectDatabase():
    return psycopg2.connect(
        dbname="student_db",
        user="postgres",
        password=os.environ["DB_PASSWORD"],
        host="localhost",
        port="5432"
    )


# Retrieve and display all student records.
def getAllStudents():
    conn = connectDatabase()

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM students ORDER BY student_id"
            )
            students = cursor.fetchall()

            if not students:
                print("No students found.")
            else:
                print("\nStudent Records:")
                for student in students:
                    print(
                        f"ID: {student[0]}, "
                        f"Name: {student[1]} {student[2]}, "
                        f"Email: {student[3]}, "
                        f"Enrollment Date: {student[4]}"
                    )
    finally:
        conn.close()


# Insert a new student record into the database.
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connectDatabase()

    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO students
                    (first_name, last_name, email, enrollment_date)
                    VALUES (%s, %s, %s, %s)
                    RETURNING student_id
                    """,
                    (first_name, last_name, email, enrollment_date)
                )
                student_id = cursor.fetchone()[0]

        print(f"Student added successfully. ID: {student_id}")
    finally:
        conn.close()


# Update the email of a student with the specified ID.
def updateStudentEmail(student_id, new_email):
    conn = connectDatabase()

    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE students
                    SET email = %s
                    WHERE student_id = %s
                    """,
                    (new_email, student_id)
                )
                affected_rows = cursor.rowcount

        if affected_rows == 0:
            print("Student ID not found.")
        else:
            print(f"Email updated for student ID {student_id}.")
    finally:
        conn.close()


# Delete the student record with the specified ID.
def deleteStudent(student_id):
    conn = connectDatabase()

    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM students
                    WHERE student_id = %s
                    """,
                    (student_id,)
                )
                affected_rows = cursor.rowcount

        if affected_rows == 0:
            print("Student ID not found.")
        else:
            print(f"Student ID {student_id} deleted successfully.")
    finally:
        conn.close()


# Display the menu and process the user's selection.
def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. View all students")
        print("2. Add student")
        print("3. Update student email")
        print("4. Delete student")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        try:
            if choice == "1":
                getAllStudents()

            elif choice == "2":
                first_name = input("First name: ").strip()
                last_name = input("Last name: ").strip()
                email = input("Email: ").strip()
                enrollment_date = input(
                    "Enrollment date (YYYY-MM-DD): "
                ).strip()

                addStudent(
                    first_name,
                    last_name,
                    email,
                    enrollment_date or None
                )

            elif choice == "3":
                student_id = int(input("Student ID: "))
                new_email = input("New email: ").strip()

                updateStudentEmail(student_id, new_email)

            elif choice == "4":
                student_id = int(input("Student ID: "))

                deleteStudent(student_id)

            elif choice == "5":
                print("Exiting application.")
                break

            else:
                print("Invalid choice. Please select 1-5.")

        except ValueError:
            print("Invalid input. Student ID must be an integer.")

        except (psycopg2.Error, KeyError) as error:
            print(f"Database or configuration error: {error}")

        if choice in ("1", "2", "3", "4"):
            input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
