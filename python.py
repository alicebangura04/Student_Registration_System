class Student_Registration_System:

    """Represents an individual student."""

    university = "Limkokwing University of Creative Technology, Sierra Leone"

    def __init__(self, student_id, full_name, department, level):

        self.student_id = student_id

        self.full_name = full_name

        self.department = department

        self.level = level

    def display_info(self):

        """Display the details of a student."""

        print(f"Student ID : {self.student_id}")

        print(f"Full Name  : {self.full_name}")

        print(f"Department : {self.department}")

        print(f"Level      : {self.level}")

    def update_details(self, full_name, department, level):

        """Update a student's details when new values are provided."""

        if full_name:

            self.full_name = full_name

        if department:

            self.department = department

        if level:

            self.level = level

    @classmethod

    def display_university(cls):

        """Display the university name."""

        print(f"Institution: {cls.university}")

class Student_Registration_System:

    """Manages student records."""

    def _init_(self):

        # A list stores Student objects during the program session.

        self.students = []

    def find_student(self, student_id):

        """Find a student by ID and return the object if found."""

        for student in self.students:

            if student.student_id.lower() == student_id.lower():

                return student

        return None

    def register_student(self, student_id, full_name, department, level):

        """Register a new student."""

        if self.find_student(student_id) is not None:

            print("\nError: This student ID is already registered.")

            return

        student = Student(student_id, full_name, department, level)

        self.students.append(student)

        print("\nStudent registered successfully!")

    def display_students(self):

        """Display all registered students."""

        if not self.students:

            print("\nNo students have been registered yet.")

            return

        print("\n" + "=" * 45)

        print("             REGISTERED STUDENTS")

        print("=" * 45)

        for number, student in enumerate(self.students, start=1):

            print(f"\nStudent {number}")

            print("-" * 30)

            student.display_info()

        print("\nTotal students:", len(self.students))

    def search_student(self, student_id):

        """Search for and display one student."""

        student = self.find_student(student_id)

        if student is None:

            print("\nStudent not found.")

        else:

            print("\nStudent found!")

            print("-" * 30)

            student.display_info()

    def update_student(self, student_id):

        """Update an existing student's details."""

        student = self.find_student(student_id)

        if student is None:

            print("\nStudent not found.")

            return

        print("\nEnter the new details.")

        print("Press Enter to keep the current value.")

        full_name = input(

            f"Full name [{student.full_name}]: "

        ).strip()

        department = input(

            f"Department [{student.department}]: "

        ).strip()

        level = input(

            f"Level [{student.level}]: "

        ).strip()

        student.update_details(full_name, department, level)

        print("\nStudent details updated successfully!")

    def delete_student(self, student_id):

        """Delete a student after confirmation."""

        student = self.find_student(student_id)

        if student is None:

            print("\nStudent not found.")

            return

        print(f"\nStudent: {student.full_name}")

        confirmation = input(

            "Are you sure you want to delete this record? (y/n): "

        ).strip().lower()

        if confirmation == "y":

            self.students.remove(student)

            print("Student record deleted successfully.")

        else:

            print("Deletion cancelled.")

    def display_total_students(self):

        """Display the number of registered students."""

        print(f"\nTotal registered students: {len(self.students)}")

def get_required_input(prompt):

    """Ask for input until the user enters a non-empty value."""

    while True:

        value = input(prompt).strip()

        if value:

            return value

        print("This field cannot be empty. Please try again.")

def display_menu():

    """Display the main menu."""

    print("\n" + "=" * 45)

    print("        STUDENT REGISTRATION SYSTEM")

    print("=" * 45)

    print("1. Register New Student")

    print("2. View All Students")

    print("3. Search for Student")

    print("4. Update Student Details")

    print("5. Delete Student Record")

    print("6. View Total Students")

    print("7. Display University")

    print("8. Exit")

    print("=" * 45)

def main():

    """Run the Student Registration System."""

    system = Student_Registration_System()

    while True:

        display_menu()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":

            print("\n--- REGISTER NEW STUDENT ---")

            student_id = get_required_input("Student ID: ")

            full_name = get_required_input("Full name: ")

            department = get_required_input("Department: ")

            level = get_required_input("Level/Semester: ")

            def register_student(student_id, full_name, department, level):

                student_id, full_name, department, level
            

        elif choice == "2":

            system.display_students()

        elif choice == "3":

            student_id = get_required_input(

                "Enter the student ID to search: "

            )

            system.search_student(student_id)

        elif choice == "4":

            student_id = get_required_input(

                "Enter the student ID to update: "

            )

            system.update_student(student_id)

        elif choice == "5":

            student_id = get_required_input(

                "Enter the student ID to delete: "

            )

            system.delete_student(student_id)

        elif choice == "6":

            system.display_total_students()

        elif choice == "7":

            system.display_university()

        elif choice == "8":

            print("\nThank you for using the Student Registration System.")

            print("Goodbye!")

            break

        else:

            print("\nInvalid choice. Please select a number from 1 to 8.")

if __name__ == "__main__":
    main()

