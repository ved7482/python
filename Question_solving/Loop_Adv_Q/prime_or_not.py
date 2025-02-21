#JAI SHREE RAM

# Q. Accept a number from user and check whether it is a prime number or not.

n = int(input("Please enter a number: "))

count = 0
for i in range(1, n+1):
    if n%i == 0:
        # print(i, end=" ")
        count = count + 1

print(f"The factors of {n} are: {count}.")

if count == 2:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is composite number.")