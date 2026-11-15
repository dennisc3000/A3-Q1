# A3-Q1

A Python application that connects to PostgreSQL to perform CRUD operations on student records using `psycopg2`.

## Demonstration Video



The video demonstrates the database setup, all four CRUD functions, and their results in pgAdmin.

## Requirements

- Python 3
- PostgreSQL and pgAdmin 4
- psycopg2-binary

## Database Setup

1. Open pgAdmin 4 and connect to PostgreSQL.
2. Create a database named `student_db`.
3. Open the Query Tool for `student_db`.
4. Execute `query.sql` to create the `students` table and insert the three initial records.

## Application Setup and Execution

1. Open the project folder in VS Code.
2. Open the terminal and install the required library:

```powershell
python -m pip install psycopg2-binary
```

3. Set your PostgreSQL password:

```powershell
$env:DB_PASSWORD = "your_postgresql_password"
```

4. Run the application from the project folder:

```powershell
python crud.py
```

The application connects to `student_db` using the `postgres` user on `localhost:5432`.

## Application Functions

The application provides a menu with 4 operations:

1. **getAllStudents()** — Retrieves and displays all student records.
2. **addStudent()** — Inserts a new student record.
3. **updateStudentEmail()** — Updates a student's email using their ID.
4. **deleteStudent()** — Deletes a student using their ID.

Select an option from the menu and follow the prompts.

## Verifying Operations

After each operation, go to pgAdmin, open the Query Tool for `student_db` and execute:

```sql
SELECT * FROM students ORDER BY student_id;
```

Run this query after each operation to verify changes.
