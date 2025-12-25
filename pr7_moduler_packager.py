import datetime
import time
import math
import random
import string
import uuid


class StudentModule:
    def datetime_menu(self):
        while True:
            print("\nDatetime and Time Operations")
            print("1. Show current date and time")
            print("2. Difference between two dates")
            print("3. Custom date format")
            print("4. Stopwatch")
            print("5. Countdown Timer")
            print("6. Back")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                now = datetime.datetime.now()
                current = now.strftime("%Y-%m-%d %H:%M:%S")
                print("Current Date and Time:", current)

            elif ch == 2:
                d1 = input("Enter first date (YYYY-MM-DD): ")
                d2 = input("Enter second date (YYYY-MM-DD): ")
                date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
                diff = abs((date2 - date1).days)
                print("Difference:", diff, "days")

            elif ch == 3:
                now = datetime.datetime.now()
                formatted = now.strftime("%A, %d %B %Y")
                print("Formatted Date:", formatted)

            elif ch == 4:
                input("Press Enter to start...")
                start = time.time()
                input("Press Enter to stop...")
                end = time.time()
                print("Elapsed Time:", round(end - start, 2), "seconds")

            elif ch == 5:
                sec = int(input("Enter seconds: "))
                for i in range(sec, 0, -1):
                    print(i)
                    time.sleep(1)
                print("Time up!")

            elif ch == 6:
                break

            print("------------------------")


    def math_menu(self):
        while True:
            print("\nMathematical Operations")
            print("1. Factorial")
            print("2. Compound Interest")
            print("3. Trigonometric Values")
            print("4. Area of Shapes")
            print("5. Back")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                num = int(input("Enter number: "))
                fact = math.factorial(num)
                print("Factorial:", fact)

            elif ch == 2:
                p = float(input("Enter principal: "))
                r = float(input("Enter rate (%): "))
                t = float(input("Enter time (years): "))
                amount = p * (1 + r/100) ** t
                print("Compound Interest:", round(amount, 2))

            elif ch == 3:
                angle = int(input("Enter angle in degrees: "))
                rad = math.radians(angle)
                print("sin:", math.sin(rad))
                print("cos:", math.cos(rad))
                print("tan:", math.tan(rad))

            elif ch == 4:
                print("1. Circle")
                print("2. Rectangle")
                s = int(input("Select shape: "))

                if s == 1:
                    r = float(input("Enter radius: "))
                    area = math.pi * r * r
                    print("Area of Circle:", area)

                elif s == 2:
                    l = float(input("Enter length: "))
                    w = float(input("Enter width: "))
                    area = l * w
                    print("Area of Rectangle:", area)

            elif ch == 5:
                break

            print("------------------------")


    def random_menu(self):
        while True:
            print("\nRandom Data Generation")
            print("1. Random Number")
            print("2. Random List")
            print("3. Random Password")
            print("4. Random OTP")
            print("5. Back")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                num = random.randint(1, 100)
                print("Random Number:", num)

            elif ch == 2:
                size = int(input("Enter list size: "))
                lst = []
                for i in range(size):
                    lst.append(random.randint(1, 100))
                print("Random List:", lst)

            elif ch == 3:
                length = int(input("Enter password length: "))
                chars = string.ascii_letters + string.digits
                password = ""
                for i in range(length):
                    password += random.choice(chars)
                print("Password:", password)

            elif ch == 4:
                otp = ""
                for i in range(6):
                    otp += random.choice(string.digits)
                print("OTP:", otp)

            elif ch == 5:
                break

            print("------------------------")


    def uuid_menu(self):
        uid = uuid.uuid4()
        print("Generated UUID:", uid)
        print("------------------------")


    def file_menu(self):
        while True:
            print("\nFile Operations")
            print("1. Create File")
            print("2. Write File")
            print("3. Read File")
            print("4. Append File")
            print("5. Back")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                name = input("Enter file name: ")
                try:
                    open(name, "x")
                    print("File created successfully")
                except:
                    print("File already exists")

            elif ch == 2:
                name = input("Enter file name: ")
                data = input("Enter data: ")
                f = open(name, "w")
                f.write(data)
                f.close()
                print("Data written")

            elif ch == 3:
                name = input("Enter file name: ")
                f = open(name, "r")
                print("File Content:")
                print(f.read())
                f.close()

            elif ch == 4:
                name = input("Enter file name: ")
                data = input("Enter data: ")
                f = open(name, "a")
                f.write("\n" + data)
                f.close()
                print("Data appended")

            elif ch == 5:
                break

            print("------------------------")


    def module_menu(self):
        print("\nExplore Module Attributes")
        name = input("Enter module name: ")

        if name == "math":
            print(dir(math))
        else:
            print("Module not found")


# -------- MAIN --------

obj = StudentModule()

print("====================================")
print("Welcome to Multi Utility Toolkit")
print("====================================")

while True:
    print("\nMain Menu")
    print("1. Datetime & Time")
    print("2. Mathematical Operations")
    print("3. Random Utilities")
    print("4. UUID Generator")
    print("5. File Operations")
    print("6. Explore Module")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.datetime_menu()
    elif choice == 2:
        obj.math_menu()
    elif choice == 3:
        obj.random_menu()
    elif choice == 4:
        obj.uuid_menu()
    elif choice == 5:
        obj.file_menu()
    elif choice == 6:
        obj.module_menu()
    elif choice == 7:
        print("Thank you for using the Toolkit!")
        break
    else:
        print("Invalid choice")