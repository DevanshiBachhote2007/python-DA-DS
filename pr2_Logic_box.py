print()
print("Welcome to the Pattern Generator and Number Analyzer.")
print("-----------------------------------------------------")


while True:
    print()
    print ("Select an option:")

    print("1. Generate a pattern.")
    print("2. Analyze a Range of number.")
    print("3. Exit.")
    print()

    n=int(input("Enter your choice:"))
    

    if n==1:
        m=int(input("Enter the number of rows for the pattern:"))
        
        for i in range(1,m+1):
            for j in range (i):
                print("*",end="")
            print()
            
    elif n==2:
        print()
        a=int(input("Enter the Start of Range:"))
        b=int(input("Enter the end of Range:"))
        sum=0

        for i in range(a,b+1):
            if i%2==0:
                print(f"Number {i} is even.")
            else :
                print(f"Number {i} is odd.")
            
            sum+=i
        print()
        print(f"Sum of numbers from {a} to {b}= {sum}")

    elif n==3:
        print("Exiting the program. Goodbyee!")
        break

    else:
        print("Invalid option . Please select only given options.")
        


