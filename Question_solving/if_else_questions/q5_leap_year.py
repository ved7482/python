#JAI SIYARAM

#Q. Accept the year and check if it is a leaf yaer or not.

year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0):           #to be a leap year it has to be divisible by 4 and shouldn't be a centuary year(e.g. 2000, 1900, 1800, 1700, 1600, etc.)
    print(f"{year} is a leap yaer.")
elif (year % 100 == 0 and year % 400 == 0):       # their is catch here : {those centuary years(divisible by 100) must be divisible by 400.}
    print(f"{year} is a leap yaer.")
else:
    print(f"{year} is not a leap year.")