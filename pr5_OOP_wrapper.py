class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(person):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)
        self.emp_id = emp_id
        self.salary = salary

    
    def _del_(self):
        print(f"Employee Destroyed: {self.emp_id}, {self.name}")

    def set_emp_id(self,emp_id):
        self.emp_id = emp_id
    def set_salary(self,salary):
        self.salary = salary

    def get_emp_id(self): 
        return self.emp_id
    def get_salary(self):  
        return self.salary
  
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Id: {get_emp_id}")
        print(f"Salary: {get_salary}")

class Manager(Employee):
    def __init__(self,name,age,emp_id,salary,department):
        super().__init__(name,age,emp_id,salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self,name,age,emp_id,salary,prog_lang):
        super().__init__(name,age,emp_id,salary)
        self.prog_lang = prog_lang

    def display(self):
        super().display()
        print(f"Programming language: {self.prog_lang}")


objects = []
print("--- Python OOP Project : Employee Management System ---")

while True:

    print("\nChoose an operation.")
    print("1. Create a Person.")
    print("2. Create an Employee.")
    print("3. Create a Manager.")
    print("4. Create a Developer.")
    print("5. Show Details.")
    print("6. Exit.")

    option=int(input("\nEnter your choice: "))

    if option==1:
        nam=input("Enter name: ")
        ag= int(input("Enter Age: "))

        person1=person(nam,ag)
        objects.append(person1)
        print(f"Person created with Name: {person1.name} and Age: {person1.age}.")

    elif option==2:
        nam=input("Enter name: ")
        ag= int(input("Enter Age: "))
        id= input("Enter Employee Id: ")
        sal= float(input("Enter Salary: "))

        emp1=Employee(nam,ag,id,sal)
        objects.append(emp1)
        print(f"Employee created with Name: {emp1.name}, Age: {emp1.age}, Id: {emp1.emp_id} and Salary: ${emp1.salary}.")

    elif option==3:
        nam=input("Enter name: ")
        ag= int(input("Enter Age: "))
        id= input("Enter Employee Id: ")
        sal= float(input("Enter Salary: "))
        depart= input("Enter Department: ")

        manag1=Manager(nam,ag,id,sal,depart)
        objects.append(manag1)
        print(f"Manager created with Name: {manag1.name}, Age: {manag1.age}, Id: {manag1.emp_id}, Salary: ${manag1.salary}, Department: {manag1.department}.")

    elif option==4:
        nam=input("Enter name: ")
        ag= int(input("Enter Age: "))
        id= input("Enter Employee Id: ")
        sal= float(input("Enter Salary: "))
        lang= input("Enter Programming language: ")

        dlpr1=Developer(nam,ag,id,sal,lang)
        objects.append(developer)
        print(f"Manager created with Name: {dlpr1.name}, Age: {dlpr1.age}, Id: {dlpr1.emp_id}, Salary: ${dlpr1.salary}, Programming Language: {dlpr1.prog_lang}.")

    elif option==5:
        if not objects:
            print("Details not found yet.*Create from above choices first*.")
        
        else:
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            print("4. Developer")
            opt=int(input("Enter your choice:"))

            for i in objects:
                if opt== 1 and isinstance(i,person):
                    print("\nPerson Details:")
                    i.display()
            
                elif opt== 2 and isinstance(i,Employee):
                    print("\nEmployee Details:")
                    i.display()

                elif opt== 3 and isinstance(i,Manager):
                    print("\nManager Details:")
                    i.display()
        
                elif opt== 4 and isinstance(i,Developer):
                    print("\nDeveloper Details:")
                    i.display()

                else:
                    print("Invalid choice.")

    elif option==6:
        print("Exiting the system. All resources have been freed.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")



