#JAI SIYARAM

# Q. Accept the name and the age from the user.Check if the user is a valid voter or not.

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if (age >= 18):
    print(f"{name} is a valid voter.")
elif (age < 18 and age > 0):
    print(f"{name} is not a valid voter.")
else:
    print("Enter a valid age.")