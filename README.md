# SQL Assignment

MySQL + Python  Assignments

Part 1: Database Setup & Basic Queries

- Create a database named SchoolDB.

- Create two tables: 

  - Students with columns: student_id, name, age, major.
  - Courses with columns: course_id, course_name, credits.
  - student_id, course_id should be primary keys
    
- Insert at least 5 students and 3 courses into the tables.

- Write queries to:

  - Retrieve all students.
  - Find students older than 20.
  - List all courses with credits greater than 3.

Part 2: Relationships with Keys

- Create an Enrollments table with columns: enrollment_id, student_id, course_id, grade.
- Add a foreign key for student_id referencing Students.
- Add a foreign key for course_id referencing Courses.
- Insert at least 5 enrollment records.

- Write queries to:

  - List all students with the courses they are enrolled in.
  - Show all students who got grade 'A' in any course.
  - Count how many students are enrolled in each course.

Part 3: Python + MySQL Integration
- Write a Python script to:
  - Connect to SchoolDB using mysql.connector.
  - Build a Python-based Student-Course Management System with the following menu:
    - Add Student
    - Add Course
    - Enroll Student in Course
    - Show Student’s Enrollments
    - Exit
 
## To Run

Necessary downloads:

- python
- mySQL
- Various packages:

| **Package**              | **Purpose**                                          | **Install Command**                  |
| ------------------------ | ---------------------------------------------------- | ------------------------------------ |
| `mysql-connector-python` | Connects Python to a MySQL database                  | `pip install mysql-connector-python` |
| `tabulate`               | Pretty-prints query results as formatted tables      | `pip install tabulate`               |
| `pyfiglet`               | Generates ASCII-art headers for your menu            | `pip install pyfiglet`               |
| `sqlparse`               | Safely splits SQL scripts into executable statements | `pip install sqlparse`               |


