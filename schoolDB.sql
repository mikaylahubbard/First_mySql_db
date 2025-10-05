-- create the database - only run once
CREATE DATABASE IF NOT EXISTS SchoolDB;
-- select the database
USE SchoolDB;
-- create 2 tables
CREATE TABLE IF NOT EXISTS Students(
    STUDENT_ID INT NOT NULL AUTO_INCREMENT,
    NAME VARCHAR(20),
    AGE INT,
    MAJOR CHAR(25),
    PRIMARY KEY (STUDENT_ID)
);
CREATE TABLE IF NOT EXISTS Courses(
    COURSE_ID INT NOT NULL AUTO_INCREMENT,
    COURSE_NAME VARCHAR(25),
    CREDITS INT,
    PRIMARY KEY (COURSE_ID)
);
CREATE TABLE IF NOT EXISTS Enrollments(
    ENROLLMENT_ID INT NOT NULL AUTO_INCREMENT,
    STUDENT_ID INT,
    COURSE_ID INT,
    GRADE CHAR(5),
    FOREIGN KEY (STUDENT_ID) REFERENCES Students(STUDENT_ID),
    FOREIGN KEY (COURSE_ID) REFERENCES Courses(COURSE_ID),
    PRIMARY KEY (ENROLLMENT_ID)
);
ALTER TABLE Students
ADD UNIQUE (NAME);
ALTER TABLE Courses
ADD UNIQUE (COURSE_NAME);
ALTER TABLE Enrollments
ADD UNIQUE (STUDENT_ID, COURSE_ID);
INSERT INTO Students (NAME, AGE, MAJOR)
VALUES ("Aaron Adams", 20, "Accounting"),
    ("Belle Brooks", 19, "Business"),
    ("Charlotte Carter", 20, "Computer Science"),
    ("Damien Downer", 21, "Data Analytics"),
    ("Emily Essex", 19, "Elementary Education") ON DUPLICATE KEY
UPDATE AGE =
VALUES(AGE),
    MAJOR =
VALUES(MAJOR);
INSERT INTO Courses (COURSE_NAME, CREDITS)
VALUES ("Software Engineering", 3),
    ("Classroom Management", 3),
    ("Computer Science 1", 4) ON DUPLICATE KEY
UPDATE CREDITS =
VALUES(CREDITS);
INSERT INTO Enrollments (STUDENT_ID, COURSE_ID, GRADE)
VALUES (3, 1, "B"),
    (3, 3, "A"),
    (5, 2, "A"),
    (4, 1, "C"),
    (1, 3, "A") ON DUPLICATE KEY
UPDATE GRADE =
VALUES(GRADE);
-- show all tables in the DB
SHOW tables;
-- Retrieve all Students
SELECT *
FROM Students;
SELECT *
FROM Students
WHERE AGE > 20;
SELECT *
FROM Courses
WHERE CREDITS > 3;
-- view all courses
SELECT *
FROM Courses;
SELECT *
FROM Enrollments;
-- print all enrollment info
SELECT s.NAME AS Student,
    c.COURSE_NAME AS Course,
    e.GRADE AS Grade
FROM Enrollments e
    JOIN Courses c ON e.COURSE_ID = c.COURSE_ID
    JOIN Students s ON e.STUDENT_ID = s.STUDENT_ID;
-- show all student who earned an a
SELECT DISTINCT s.NAME AS Student,
    c.COURSE_NAME AS Course,
    e.GRADE AS Grade
FROM Enrollments e
    JOIN Students s ON e.STUDENT_ID = s.STUDENT_ID
    JOIN Courses c ON e.COURSE_ID = c.COURSE_ID
WHERE e.GRADE = 'A';
-- count students in each course
SELECT c.COURSE_NAME AS Course,
    COUNT(e.STUDENT_ID) AS Num_Students
FROM Courses c
    LEFT JOIN Enrollments e ON c.COURSE_ID = e.COURSE_ID
GROUP BY c.COURSE_NAME;