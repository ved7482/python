#Program to illustrate divmod() function

a = int(input("num1: "))
b = int(input("num2: "))

# use divmod() and store results in 2 variables x, and y
x, y = divmod(a, b)


print(f"{a} // {b} = {x}")
print(f"{a} % {b} = {y}")



"""

The divmod(dividend,divisor) function returns a tuple containing the quotient and the remainder, when argument1 (dividend) is divided by argument2 (divisor).

The syntax of the divmod() function is :
divmod(x, y)

x - a non-complex number (numerator)
y - a non-complex number (denominator)

The divmod() returns (q, r) - a pair of numbers (a tuple) consisting of quotient q and remainder r
Note:
If x and y are integers, the return value from divmod() is same as (x // y, x % y).
If either x or y is a float, the result is (q, x%y). Here, q is the whole part of the quotient.

Understand the working of divmod() by the following examples :
Statement						Result
print(divmod(8, 3))				(2, 2)
print(divmod(3, 8))				(0,3)
print(divmod(5, 5))				(1,0)
print(divmod(0,9))				(0,0)
print(divmod(3,0))				ZeroDivisionError: integer division or modulo by zero
print(divmod(8.0, 3))			(2.0,2.0)
print(divmod(3, 8.0))			(0.0,3.0)
print(divmod(7.5, 2.5))			(3.0,0.0)
print(divmod(2.6, 0.5))			(5.0, 0.10000000000000009)
print(divmod(2.6, 0))			ZeroDivisionError: float divmod()
print(divmod(0.0,8.0))			(0.0,0.0)
Note:
If the second argument is 0, it returns Zero Division Error.
If the first argument is 0, it returns (0, 0).

"""