#JAI SHREE RAM

str = "codetantra"

print(str[::])
print(str[5])

# print(str[start:stop:stride])
print(str[2:7])
#by defualt stride = 1 and it includes the start value and leaves the stop value(just same as range fun.)

print(str[2:7:1])
print(str[1:8:2])
print(str[1:8:3])

#if we donot mention the starting point it it print from start
print(str[:7])

#if we donot specifiy the ending index it will print upto end
print(str[2:])
print(str[2::2])

print("\nString(Negative indexing)")
print(str[-1:-5])         #both the indexing strats from the L.H.S only

print(str[:-7])

print(str[-9:-3:-2])     # since stride value is -ve, it does not print anything
print(str[-9:-3:2])      #stride vale should be always +ve
print("Revesing the string :- ",str[::-1])
print(str[::-2])



