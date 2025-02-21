#JAI SHREE RAM

# Q. Print aall the factors of a number

n = int(input("Please enter a number: "))

print(f"The factors of {n} are: ", end="")

for i in range(1, n+1):
    if n%i == 0:
        print(i, end=" ")

# Output:

# Please enter a number: 19
# The factors of 19 are: 1 19   