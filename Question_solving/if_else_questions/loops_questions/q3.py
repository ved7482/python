#JAI SHREE RAM

# Q: sum upto n terms

n = int(input("Enter the number of terms: "))
sum = 0
for i in range(1, n+1):
    sum += i
print(f"Sum upto {n} terms is {sum}")