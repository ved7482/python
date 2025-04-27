a = "Coding is fun!"
print(f"Length of string is: {len(a)}")

print("Printing string using for loop:")

for i in range(len(a)):       #lenth itself is counted from 1, so only len(a) and not (len(a)+1)
    print(a[i], end='')