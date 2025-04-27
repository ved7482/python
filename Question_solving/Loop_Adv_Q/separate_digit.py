#JAI SHREE RAM

#Q. Write a program to separate each digit of a number and print it on a new line.

n = int(input("Enter a Number: "))

while n > 0:
    print(n % 10)
    n = n // 10