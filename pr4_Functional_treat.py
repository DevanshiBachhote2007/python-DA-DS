print("\nWelcome to Data Analyzer and Transformer Program.")
print("-"*49)

data=[]
while True:

    print("""\nMain Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recurission)
4. Filter Data by Thteshold (Lamda Function)
5. Sort Data
6. Display Dataset (Return Multiple Values)
7. Exit Program""")

    x=int(input("Please Enter your choice: "))

    if x==1:
        a=input("Enter data for a 1d array (seprated by spaces):")
        b= a.split()
        data=[int(x) for x in b]

        print("\nData has been stored successfully!")


    elif x==2:
        print("\nData summary:")
        
        print("- Total elements: ",len(data))

        print("- Minimum value: ",min(data))
        
        print("- Maximum value: ",max(data))
        
        print("- Sum of all values: ",sum(data))

        ave= sum(data)/len(data)
        print("- Average value: ",ave)


    elif x==3:
        n=int(input("\nEnter a number to calculate its factorial: "))

        def fact(n):                         
                            # use of doc string
            """\nThis Question finds the Factorial of a given number.
    Parameters:
        n (int): Take input of number from user.
    Returns:
        int: Factorial of number."""
            
            if n==1:
                return 1
            else:
                return n*fact(n-1)

        print(f"\nFactorial of {n} is: {fact(n)}")
        print(fact.__doc__)
    
    
    elif x==4:

        f=int(input("\nEnter a threshold value to filter out data above this value:"))

        filt=list(filter(lambda m: m>=f,data))
        print(f"\nFilter Data (value >= {f}): {filt}")


    elif x==5:
        if not data:
            print("\nEnter list of data first and than choose 5.")
    
        else:
            print("\nChoose sorting option:")
            print("1. Ascending")
            print("2. Descending")

            m=int(input("\nEnter your choice:"))
            if m==1:
                asc= sorted(data)
                print(f"Sorted Data in Ascending Order: \n{asc}")
            
            elif m==2:
                dsc= sorted(data, reverse=True)
                print(f"Sorted Data in Descending Order: \n{dsc}")
            
            else:
                print("Invalid option..")


    elif x==6:
        print("\nDataset Statistics:")
        
        def mi():
                    # use of doc string
            """\nThis Question finds Minimum, Maximum, Sum and Average of a Data  given by user.
    Parameters:
        Data(int): Take list input from user.    
    Returns:    
        int: Returns result of different equations."""        
            
            mini = data[0]
            for x in data:
                if x < mini:
                    mini = x
            print("- Minimum value: ",mini)
        mi() 
        
        def mx():
            maxi = data[0]
            for x in data:
                if x > maxi:
                    maxi = x
            print("- Maximum value: ",maxi)
        mx()    

        def sum():
            global s            # use of Global
            s=0
            for x in data:
                s+=x
            print("- Sum of all values: ",s)
        sum() 

        def ave():
            c=0
            for x in data:
                c+=1
            
            a = s/c
            print("- Average value: ",a)
        ave() 

        print(mi.__doc__)   


    elif x==7:
        print("\nThank you for using the Data Analyzer and Transformer Program. \nGoodbye! ")
        print("-"*62)
        break                     

    
    else:
        print("Invalid Option choice.")
