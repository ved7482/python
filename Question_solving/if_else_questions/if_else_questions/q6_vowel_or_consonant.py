#JAI SIYARAM

#Q. Accept an Emglish alphabet from use and check if it is a consonant or vowel.
ch = input("Please enter an English alphabet: ")

# if (ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A" or ch == "E" or ch == "I"or ch == "O" or ch == "U"):
# or in simple way use a string
if ch in "aeiouAEIOU":
    print(f"'{ch}' is a vowel.")
else:
    print(f"'{ch}' is a consonant.")