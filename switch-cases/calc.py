# Jai Shree Ram


# taking a no. from user
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")

# Checking the type of the entered no.
if num1 is int:
    num1 = int(num1)

if num2 is int:
    num2 = int(num2)

else:
    print("Invalid number")

# taking a operator from user
op = input("Enter an operator: ")



# Using switch case
match (op):
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    #  deafult case
    case _:                          
        print("Invalid operator")  
