#!/usr/bin/env python3

from tabulate import tabulate
from pyfiglet import figlet_format
import mysql.connector
import sqlparse

class Db:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,    
            database=database
        )
        self.cursor = self.db.cursor()
        
    def execute_intial_script(self, sql_script):    
        self.db.commit()
        
        with open(sql_script, "r") as f:
            sql_script = f.read()
        statements = sqlparse.split(sql_script)
        
        for stmt in statements:
            stmt = stmt.strip()
            if stmt:
                try:
                    self.cursor.execute(stmt)
                    if self.cursor.with_rows:  # e.g., SELECT query
                        rows = self.cursor.fetchall()  # fetch or discard
                        headers = [i[0] for i in self.cursor.description]
                        print(tabulate(rows, headers=headers, tablefmt="psql"))
                except mysql.connector.Error as err:
                    print(f"Error executing: {stmt}\n{err}")
        self.db.commit()

    def close(self):
        self.cursor.close()
        self.db.close()
  
        
    def add_student(self, name, age, major):
        sql = "INSERT INTO Students (NAME, AGE, MAJOR) VALUES (%s, %s, %s)"
        values = (name, age, major)
        try:
            self.cursor.execute(sql, values)
            self.db.commit()
            print(f"Student '{name}' added successfully.")
        except mysql.connector.Error as err:
            print(f"Error inserting student: {err}")
        
        
    def add_course(self, course_name, credits):
        sql = "INSERT INTO Courses (COURSE_NAME, CREDITS) VALUES (%s, %s)"
        values = (course_name, credits)
        try:
            self.cursor.execute(sql, values)
            self.db.commit()
            print(f"Course '{course_name}' added successfully.")
        except mysql.connector.Error as err:
            print(f"Error inserting course: {err}")
    
    def enroll_student(self, student_name, course_name, grade):
        # normalize input
        student_name = student_name.strip().lower()
        course_name = course_name.strip().lower()
        
        # find student id
        self.cursor.execute(
            "SELECT STUDENT_ID FROM Students WHERE LOWER(NAME) = %s",
            (student_name,)
        )
        student = self.cursor.fetchone()
        if not student:
            print("Student not found.")
            return
        student_id = student[0]
        
        # find course id
        self.cursor.execute(
            "SELECT COURSE_ID FROM Courses WHERE LOWER(COURSE_NAME) = %s",
            (course_name,)
        )
        course = self.cursor.fetchone()
        if not course:
            print("Course not found.")
            return
        course_id = course[0]
       

        sql = "INSERT INTO Enrollments (STUDENT_ID, COURSE_ID, GRADE) VALUES (%s, %s, %s)"
        values = (student_id, course_id, grade)
        try:
            self.cursor.execute(sql, values)
            self.db.commit()
            print(f"Student enrolled successfully.")
        except mysql.connector.Error as err:
            print(f"Error enrolling student.")
    
    
    def show_student_enrollments(self):
        sql = """
        SELECT s.NAME AS Student, c.COURSE_NAME AS Course, e.GRADE AS Grade
        FROM Enrollments e
        JOIN Students s ON e.STUDENT_ID = s.STUDENT_ID
        JOIN Courses c ON e.COURSE_ID = c.COURSE_ID
        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        headers = [col[0] for col in self.cursor.description]
        print(tabulate(rows, headers=headers, tablefmt="psql"))
        
    
    def present_to_user(self):
        ascii_art = figlet_format("Student Grades", font='standard')
        print(ascii_art)
        
        print("MENU:\n\t1. Add Student \n\t2. Add Course \n\t3. Enroll a Student \n\t4. Show Student Enrollments\n\nNote: scroll up to view part 1 of the assignment\n")
        
        active = True
        while active:
            choice = input("Which function would you like to run (Enter 1-4, or 'q' to quit): ")
            choice = choice.lower()
            match choice:
                case "1":
                    name = input("\nEnter Student Name: ")
                    try:
                        age = int(input("Enter Student Age: "))
                    except ValueError:
                        print("Invalid Input. Please enter a whole number.")
                        break
                    major = input("Enter Student Major: ")
                    self.add_student(name, age, major)
                case "2":
                    course_name = input("\nEnter Course Name: ")
                    try:
                        credits = int(input("Enter Number of Credits: "))
                    except ValueError:
                        print("Invalid Input. Please enter a whole number.")
                        break
                    self.add_course(course_name, credits)
                case "3":
                    student_name = input("\nEnter Student Name: ")
                    course_name = input("Input Course Name: ")
                    grade = input("Enter Letter Grade: ")
                    self.enroll_student(student_name, course_name, grade)
                case "4":
                    self.show_student_enrollments()
                case "q":
                    active = False;
                case _: 
                    print("Invalid input. Please enter a number 1-4 or 'q' to quit")
        

        
if __name__ == "__main__":
    # connect to/initialize databse
    database = Db(
        host="localhost",
        user="root",
        password="DonutIsSpelled0K",
        database="SchoolDB"
    )

    # Run full script to set up the initial tables and values
    database.execute_intial_script("SchoolDB.sql")
    
    #run basic UI in terminal
    database.present_to_user()

    database.close()
