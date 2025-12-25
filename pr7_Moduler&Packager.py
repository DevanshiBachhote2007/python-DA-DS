# this code not run in online compiler because it requires user input and file operations

import datetime
import time
import math
import random
import string
import uuid
import importlib
from custom_modules import file_ops

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:\n")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            now = datetime.datetime.now()
            print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        elif choice == '2':
            date1 = input("Enter the first date (YYYY-MM-DD): ")
            date2 = input("Enter the second date (YYYY-MM-DD): ")
            d1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
            d2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
            diff = abs(d2 - d1)
            print(f"Difference: {diff.days} days")
        elif choice == '3':
            date_str = input("Enter date (YYYY-MM-DD): ")
            fmt = input("Enter format (e.g., %d/%m/%Y): ")
            dt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            print(dt.strftime(fmt))
        elif choice == '4':
            print("Starting stopwatch... Press Enter to stop")
            start = time.time()
            input()
            end = time.time()
            print(f"Elapsed time: {end - start:.2f} seconds")
        elif choice == '5':
            seconds = int(input("Enter countdown time in seconds: "))
            for i in range(seconds, 0, -1):
                print(i)
                time.sleep(1)
            print("Time's up!")
        elif choice == '6':
            break
        else:
            print("Invalid choice")

    print("================================")
    

def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            num = int(input("Enter a number: "))
            print(f"Factorial: {math.factorial(num)}")
        elif choice == '2':
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest (in %): "))
            t = float(input("Enter time (in years): "))
            ci = p * (1 + r/100)**t
            print(f"Compound Interest: {ci:.2f}")
        elif choice == '3':
            angle = float(input("Enter angle in degrees: "))
            print(f"sin: {math.sin(math.radians(angle)):.2f}")
            print(f"cos: {math.cos(math.radians(angle)):.2f}")
            print(f"tan: {math.tan(math.radians(angle)):.2f}")
        elif choice == '4':
            shape = input("Enter shape (circle, rectangle): ").lower()
            if shape == 'circle':
                r = float(input("Enter radius: "))
                print(f"Area: {math.pi * r**2:.2f}")
            elif shape == 'rectangle':
                l = float(input("Enter length: "))
                w = float(input("Enter width: "))
                print(f"Area: {l * w:.2f}")
            else:
                print("Shape not supported")
        elif choice == '5':
            break
        else:
            print("Invalid choice")

def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            min_v = int(input("Min: "))
            max_v = int(input("Max: "))
            print(random.randint(min_v, max_v))
        elif choice == '2':
            size = int(input("Size: "))
            lst = [random.randint(1,100) for i in range(size)]
            print(lst)
        elif choice == '3':
            length = int(input("Enter password length: "))
            chars = string.ascii_letters + string.digits + string.punctuation
            pwd = ''.join(random.choice(chars) for i in range(length))
            print(f"Generated Password: {pwd}")
        elif choice == '4':
            otp = random.randint(100000,999999)
            print(f"Generated OTP: {otp}")
        elif choice == '5':
            break
        else:
            print("Invalid choice")

def uuid_menu():
    print("\nGenerate Unique Identifiers (UUID):")
    print(f"Generated UUID: {uuid.uuid4()}")

def file_ops_menu():
    while True:
        print("\nFile Operations (Custom Module):")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            filename = input("Enter file name: ")
            file_ops.create_file(filename)
        elif choice == '2':
            filename = input("Enter file name: ")
            data = input("Enter data to write: ")
            file_ops.write_file(filename, data)
        elif choice == '3':
            filename = input("Enter file name: ")
            file_ops.read_file(filename)
        elif choice == '4':
            filename = input("Enter file name: ")
            data = input("Enter data to append: ")
            file_ops.append_file(filename, data)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

def explore_menu():
    print("\nExplore Module Attributes (dir()):")
    module_name = input("Enter module name to explore: ")
    try:
        mod = importlib.import_module(module_name)
        attrs = dir(mod)
        print(f"Available Attributes in {module_name} module:")
        print(attrs)
    except ImportError:
        print("Module not found")

def main():
    print("\n==============================")
    print("Welcome to Multi-Utility Toolkit")
    print("================================")
    
    while True:
         
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("================================")

       
        choice = input("Enter your choice: ")
       
        if choice == '1':
            datetime_menu()
        elif choice == '2':
            math_menu()
        elif choice == '3':
            random_menu()
        elif choice == '4':
            uuid_menu()
        elif choice == '5':
            file_ops_menu()
        elif choice == '6':
            explore_menu()
        elif choice == '7':
            print("================================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("================================")

            break
        else:
            print("Invalid choice")
    print("================================")



if __name__ == '__main__':
    main()
