print("Welcome to Interactive Data collector!")
print("--------------------------------------")
print()

name=input("Enter your Name:")
name=str(name)

age=input("Enter your Age:")
age=int(age)

height=input("Enter your Height in cm:")
height=float(height)

fav_num=input("Enter your Favourite number:")
favnum=int(fav_num)
print()

print("Thank you! Here is the information we collected:")
print()

print("Name:",name,"( Type:",type(name),",Memory addr.:",id(name),")")
print("Age:",age,"( Type:",type(age),",Memory addr.:",id(age),")")
print("Height:",height,"( Type:",type(height),",Memory addr.:",id(height),")")
print("Favourite number:",fav_num,"( Type:",type(favnum),",Memory addr.:",id(fav_num),")")
print()

curryear=2025
birthyear= curryear-age

print("Your birth year is approx.:",birthyear,"( based on your age of",age,")")
print()

print("Thank you for using the Personal Data Collector. Goodbyee!")
print()





      
      




      
      
