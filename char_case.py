# Problem statement
# Write a program that takes a character as input and prints 1, 0, or -1 according to the following rules.



# 1, if the character is an uppercase alphabet (A - Z).
# 0, if the character is a lowercase alphabet (a - z).
# -1, if the character is not an alphabet.

## Read input as specified in the question.
## Print output as specified in the question.

inp = input()
if ord(inp)>64 and ord(inp)<91:
    print("1")
elif ord(inp)>96 and ord(inp)<123:
    print("0")
else:
    print("-1")