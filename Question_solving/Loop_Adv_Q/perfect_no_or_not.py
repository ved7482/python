#JAI SHREE RAM

# Q. Accept a number from user and check whether it is a perfect number or not.

# { Perfect number is a number which is equal to the sum of its factors except itself.}
# Eg. 6 is a perfect number because 1+2+3 = 6

n = int(input("Please enter a number: "))
sum = 0

for i in range(1, n):              # We are taking n because we don't want to include the number itself
    if n%i == 0:
        # print(i, end=" ")
        sum = sum + i

print(f"The sum of factors of {n} is {sum}.")

if sum == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")