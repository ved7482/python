#JAI SIYARAM

# Q. Accept the gender from the user as char and print the resp. greatting message.

gender = input("Please enter your gender as 'M' and 'F' :")

if (gender == 'M'or  gender == 'm'):
    print("Good Morning Sir!")
elif (gender == 'F'or gender == 'f'):
    print("Good Morning Madam!")
else:
    print("You've entered the wrong character.")
