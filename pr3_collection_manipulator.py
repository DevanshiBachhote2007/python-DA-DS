print("Welcome to the Student Data Organizer!")

def display_menu():
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

students = []


all_subjects = set()



while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = int(input("Student ID: "))  
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(",")

        
        subjects = [s.strip() for s in subjects]


        unique_info = (student_id, dob)


        student_data = {
            "id_dob": unique_info,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(student_data)

        all_subjects.update(subjects)

        print(f"\nStudent {name} added successfully!")

    elif choice == "2":

        if not students:
            print("No student records available.")
        else:
            print("\n--- Student Records ---")
            for student in students:
                sid, dob = student["id_dob"]
                
                print(f"Student ID: {sid} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | Subjects: {', '.join(student['subjects'])}") 
                print("DOB: {}".format(dob))  
                print(" ID: %d, Name: %s" % (sid, student['name'])) 
                print("-" * 50)

    elif choice == "3":
        s_id = int(input("Enter Student ID to update: "))

        for student in students:
            if student["id_dob"][0] == s_id:
                print("What would you like to update?")
                print("1. Age")
                print("2. Subjects")
                update_choice = input("Enter choice: ")

                if update_choice == "1":
                    new_age = int(input("Enter new age: "))
                    student["age"] = new_age
                    print("Age updated successfully!")
                elif update_choice == "2":
                    new_subjects = input("Enter new subjects (comma-separated): ").split(",")
                    new_subjects = [s.strip() for s in new_subjects]
                    student["subjects"] = new_subjects
                    all_subjects.update(new_subjects)
                    print("Subjects updated successfully!")
                else:
                    print("Invalid choice.")
                break
        else:
            
            print("Student not found.")

    elif choice == "4":
   
        sid = int(input("Enter Student ID to delete: "))
        for i, student in enumerate(students):
            if student["id_dob"][0] == sid:
                del students[i]  
                print(f"Student with ID {sid} deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "5":
      
        print("\nUnique Subjects Offered:")
        for subject in sorted(all_subjects):
            print(subject)

    elif choice == "6":
        print("Thank you for using the Student Data Organizer. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
