# Subjects for each semester
subjects=[
    ["Python", "Database", "Networking"],
    ["Computer System", "Web Design", "Maths"],
    ["Introduction to AI", "Probability and Statistics", "Java"],
    ["R Programming","Web Applications","Distributed Systems"],
    ["Internet of Things", "Human Computer Interaction", "Cloud Architecture"],
    ["Advance Database", "Advance Java", "Machine Learning"]
]

# list to store student records
students=[]


# Student class to store student information and marks
class Student:
    def __init__(self, id, name, semester):
        self.id = id
        self.name = name
        self.semester = semester
        # Dictionary to store marks for each subject
        self.marks ={}
    
    def student_marks(self):
        print(f"Assign Student Marks for semester {self.name}.")
        for index,subject in enumerate(subjects, start=1):
            if self.semester==index:
                for sub in subject: 
                    marks = float(input(f"Enter the marks of {sub}: "))
                    if marks<0 or marks>100:
                        print("Enter marks between 0-100")
                        return
                    self.marks[sub]=marks
                print(f"Marks of {self.name} is assigned.")
    
    def average(self):
        total = 0
        count = 0
        for sub, grade in self.marks.items():
            total += grade
            count += 1
        avg = total/count
        if avg>=90 and avg<=100:
            grade = "A+"
        elif avg>=80 and avg<90:
            grade = "A"
        elif avg>=70 and avg<80:
            grade = "B+"
        elif avg>=60 and avg<70:
            grade="B"
        elif avg>=50 and avg<60:
            grade="C+"
        elif avg>=40 and avg <50:
            grade="C"
        elif avg>=0 and avg<40:
            grade="D"
        return (
            f"Percentage:\t{avg:.2f}"
            f"\nGrade:\t{grade}"
        )
            
    
    # Function to return string representation of the student object    
    def __str__(self):
            return (
                f"{self.id} {self.name} {self.semester}"
            )
                                            

# Function to add student records
def addStudent():
    try:
        print("\n\nAdd Student records")
        id = input("Enter the student id [NPxxxx]: ")
        name =input("Enter the name of the student: ")
        semester = int(input("Enter the Semester [1-6]:"))
        if not id or not name or not semester:
            print("Enter all information.\n")
            return
        if semester not in range(1,7):
            print("Choose semester between 1-6.\n")
            return
        if len(id)<6 or not id.startswith("NP") or not id[2:].isdigit():
            print("Student id consist 6 letters. Format [NPxxxx], remaining four is digit.\n")
            return
        if not students:
            student = Student(id, name, semester)
            students.append(student)
            print("Student records added successfully!\n")
        else:
            # Check if student with the same id already exists
            if any(stu.id == id for stu in students):
                print(f"Student with {id} already exists.\n")
                return
            else:
                student = Student(id, name, semester)
                students.append(student)
                print("Student records added successfully!\n")
                    
                       
    except Exception as e:
        print(e)

# Function to display student records
def displayStudent():
    try:
        print("="*25)
        print("Display Students")
        print("="*25)
        if not students:
            print("No Student Records!!\n")
            return
        else:
            print("ID\t- Name\t-Semester")
            for stu in students:
                print(stu)
            print()
    except Exception as e:
        print(e)

# Function to assign marks
def assignMarks():
    try:
        print("\n\nAssign Grades")
        id = input("Enter id of student: ")
        if not id:
            print("ID is missing!!\n")
            return
        if len(id)<6 or "NP" not in id or not id[2:].isdigit():
            print("ID format is [NPxxxx].\n")
            return
        if not students:
            print("Add Student first!!!\n")
            return
        for stu in students:
            if stu.id == id:
                stu.student_marks()
                print()
                return
        else:
            print(f"No student found with {id}.\n")
    except Exception as e:
        print(e)

# Function to search student
def searchStudent():
    try:
        print("\n\nSearch Student")
        id = input("Enter id of student: ")
        if not id:
            print("ID is missing!!\n")
            return
        if len(id)<6 or "NP" not in id or not id[2:].isdigit():
            print("ID format is [NPxxxx].\n")
            return
        if not students:
            print("Add Student first!!!\n")
            return
        for stu in students:
            if stu.id == id:
                print("ID-\tName-\tSemester-")
                print(stu)
                if not stu.marks:
                    print("No marks assigned yet.\n")
                    return
                else:
                    print("Marks:")
                    for subject, mark in stu.marks.items():
                        print(f"{subject}: {mark}")
                    print(stu.average())
                    print()
                    
                break
        else:
            print(f"No student found with {id}.\n")
            return
                
    except Exception as e:
        print(e) 

# Main function to run the Student Management System
def main():
    while True:
        print("="*35)
        print("-"*3, "Welcome to Student Manangement System")
        print("="*35,"-"*3)
        print("1. Add Students")
        print("2. Display Student")
        print("3. Assign Marks")
        print("4. Search Student")
        print("5. Exit")
        choice = input("Enter you choice: ")
        if choice == "1":
            addStudent()
        elif choice =="2":
            displayStudent()
        elif choice == "3":
            assignMarks()
        elif choice == "4":
            searchStudent()
        elif choice == "5":
            print("Thank You")
            return
        else:
            print("Enter the mentioned choices.")

if __name__ == "__main__":
    main()


        
