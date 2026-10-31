Student Registration System

## 1. Project Information

*Project Title:* Student Registration System  

*Module:* PROG211 - Object-Oriented Programming 1  

*Institution:* Limkokwing University of Creative Technology, Sierra Leone  

*Programming Language:* Python 3  

*Project Type:* Individual Assignment

## 2. Introduction

The Student Registration System is a menu-driven Python application designed to manage basic student registration records. It allows users to register new students, view registered students, search for a student, update student information, delete student records, and count the total number of registered students.

The project demonstrates the application of Object-Oriented Programming (OOP) concepts in solving a practical problem in an educational environment.

## 3. Problem Statement

Managing student information manually can be time-consuming and may lead to errors, duplicate records, or difficulty finding and updating information. This project provides a simple computer-based system to make basic student record management easier and more organized.

## 4. Project Objectives

The objectives of this project are to:

- Develop a menu-driven student registration application.

- Apply classes and objects in Python.

- Demonstrate encapsulation through organized classes and methods.

- Allow users to create, view, search, update, and delete student records.

- Validate user input and prevent duplicate student IDs.

- Practise writing readable, maintainable, and reusable code.

## 5. System Features

The system provides the following functions:

1. Register a new student.

2. Display all registered students.

3. Search for a student using their student ID.

4. Update student information.

5. Delete a student record.

6. Display the total number of registered students.

7. Display university information.

8. Exit the application.

## 6. Object-Oriented Programming Concepts

### Student Class

The Student class represents an individual student. It stores the student's ID, full name, department, and level. Its methods display student information and update student details.

### StudentRegistrationSystem Class

The StudentRegistrationSystem class manages the registration process. It contains methods for registering, displaying, searching, updating, and deleting student records.

### Objects

Objects are created from the Student class to represent individual students.

### Encapsulation

The program organizes student-related data and operations into classes, helping keep the code structured and easier to maintain.

### Methods

Methods perform specific tasks, such as registering students, searching records, and displaying information.

### Lists

A Python list stores the student objects while the program is running.

## 7. Digital Public Goods (DPG) Principles

This project considers relevant principles associated with Digital Public Goods:

- *Open-source potential:* The source code can be shared and reviewed. A suitable open-source licence should be added before claiming the project is formally open source.

- *Accessibility:* The text-based menu provides a simple interface for users.

- *Privacy:* The program uses basic student information and does not require passwords or online accounts.

- *Reusability:* The classes and methods can be extended for future student-management projects.

This is an educational project and has not been formally certified as a Digital Public Good.

## 8. System Requirements

- Python 3 installed on the computer.

- Visual Studio Code or another Python-compatible editor.

- A terminal or command prompt.

## 9. Installation and Execution

### Step 1: Download or Clone the Project

Download the project files or clone the repository from GitHub.

### Step 2: Open the Project Folder

Open the Student_Registration_System folder in Visual Studio Code.

### Step 3: Run the Application

Open the VS Code terminal and run:

bash

python main.py



If your computer uses the Windows Python launcher, you can run:

bash

py main.py



### Step 4: Use the Menu

Follow the numbered menu displayed in the terminal. Enter the number corresponding to the operation you want to perform.

## 10. Testing

The following tests should be performed before submitting the project:

| Test | Expected Result |

|---|---|

| Register a student | Student record is created |

| Enter a duplicate student ID | System rejects the duplicate |

| Display all students | Registered students are displayed |

| Search for an existing ID | Matching student is displayed |

| Search for an unknown ID | Appropriate message is displayed |

| Update a student | Student details are updated |

| Delete a student | Student record is removed |

| Enter an invalid menu option | System handles the invalid option |

| Exit the application | Program closes |

Actual results should be recorded after each test has been performed.

## 11. Limitations

- Student records are stored in memory only.

- All records are lost when the program closes.

- The application does not use a database.

- The application does not support multiple users or online registration.

## 12. Future Improvements

Future versions could include:

- Database storage using SQLite or MySQL.

- Student login and administrator authentication.

- Registration dates and course information.

- A graphical user interface.

- Exporting student records to a file.

## 13. Project Structure

text

Student_Registration_System/

├── main.py

└── README.md



## 14. Author Information

*Student Name:* [Alice isatu Bangura]  

*Student ID:* [905006445] 

*Module:* PROG211 - Object-Oriented Programming 1  

*Lecturer:* [Mr Julius Laggah]  

*Submission Date:* [30/10/2026]

## 15. Repository

*GitHub Repository:* [https://github.com/alicebangura04/Student_Registration_System]