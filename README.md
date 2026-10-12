# Student Management System

A simple, menu-driven **Student Management System built with Python**. This project is designed to practise Python fundamentals and Object-Oriented Programming (OOP) by managing student records, semester-wise subjects, marks, average percentages, and grades.

## Features

- **Add Students:** Register students with a unique student ID, name, and semester.
- **Display Students:** View all registered student records.
- **Assign Marks:** Enter marks for subjects based on the student's semester.
- **Validate Marks:** Accept marks between 0 and 100.
- **Search Students:** Find student records using their student ID.
- **Calculate Average:** Calculate the average marks of subjects with recorded marks.
- **Grade Calculation:** Assign a grade based on the calculated average.
- **Duplicate ID Prevention:** Prevent registration of students with an existing ID.
- **Menu-Driven Interface:** Use a simple command-line menu to navigate the system.

## Technologies Used

- **Programming Language:** Python 3
- **Concepts:** Object-Oriented Programming (OOP), classes, objects, constructors, instance attributes, methods, dictionaries, lists, loops, conditional statements, exception handling, and string formatting.

## Project Structure

```text
python-student-management-system/
│
├── student_management.py
└── README.md
```

`student_management.py` contains the application code. The `README.md` file provides project documentation.

## Semester-Wise Subjects

The system currently supports six semesters, with three subjects assigned to each semester.

| Semester | Subjects |
|---|---|
| 1 | Python, Database, Networking |
| 2 | Computer System, Web Design, Maths |
| 3 | Introduction to AI, Probability and Statistics, Java |
| 4 | R Programming, Web Applications, Distributed Systems |
| 5 | Internet of Things, Human Computer Interaction, Cloud Architecture |
| 6 | Advance Database, Advance Java, Machine Learning |

## Grade Calculation

The application calculates the average of the marks recorded for a student and assigns a grade according to the following scale.

| Average Percentage | Grade |
|---|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B+ |
| 60–69.99 | B |
| 50–59.99 | C+ |
| 40–49.99 | C |
| Below 40 | D |

**Note:** This grading scale is defined for this project and can be modified according to an institution's assessment policy.

## How to Run the Project

### Prerequisites

- Python 3 installed on your computer.
- A code editor such as Visual Studio Code, or any terminal that supports Python.

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/python-student-management-system.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Open the Project Folder

```bash
cd python-student-management-system
```

### Step 3: Run the Application

```bash
python student_management.py
```

Depending on your system, you may need to use:

```bash
python3 student_management.py
```

## How to Use

After running the program, a menu appears with the following options:

```text
========================================
--- Welcome to Student Management System
========================================
1. Add Students
2. Display Student
3. Assign Grades
4. Search Student
5. Exit
Enter your choice:
```

1. Select **1** to register a student.
2. Enter the student ID in the format `NPxxxx`, the student's name, and a semester from 1 to 6.
3. Select **2** to display all registered students.
4. Select **3** to enter subject marks for a registered student.
5. Select **4** to search for a student and view their marks, average percentage, and grade.
6. Select **5** to exit the application.

## Object-Oriented Programming Concepts

This project demonstrates several fundamental OOP concepts.

- **Class:** The `Student` class defines the structure of a student record.
- **Object:** Each registered student is represented by a `Student` object.
- **Constructor (`__init__`):** Initializes the student's ID, name, semester, and marks dictionary.
- **Instance Attributes:** Store individual student information and marks.
- **Instance Methods:** `student_marks()` collects marks, while `average()` calculates the average and grade.
- **Magic Method (`__str__`):** Provides a readable string representation of a student object.
- **Encapsulation:** Groups student data and related operations inside the `Student` class.

## Current Limitations

- Student records are stored in memory and are lost when the program closes.
- Marks are entered through the command line.
- Invalid non-numeric marks can interrupt the mark-entry process.
- The system currently provides basic input validation and does not include a graphical user interface or database.
- The grade calculation assumes the entered marks belong to the relevant semester's subjects.

## Future Improvements

Possible improvements for future versions include:

- Save and load student records using JSON files.
- Integrate SQLite for permanent data storage.
- Improve input validation and allow users to correct invalid entries.
- Display student results in a formatted table.
- Add subject-wise grades and result reports.
- Implement student record update and delete operations.
- Organize the project into separate Python modules and packages.
- Add automated tests using `unittest` or `pytest`.
- Develop a web-based interface using Flask or Django.

## Learning Objectives

This project was developed as a practical learning exercise to apply Python fundamentals and OOP concepts to a real-world-style problem. It provides a foundation for building larger applications involving data management, validation, calculations, and persistent storage.

## Author

**Sujal Shrestha**

GitHub: [https://github.com/Suj41/](https://github.com/)

## License

This project is available for educational and learning purposes. A license can be added to clarify how others may use, modify, and distribute the code.