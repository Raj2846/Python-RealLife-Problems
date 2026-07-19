"""
Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
"""
st = input()
lower = list(x for x in st if x.islower())
upper = list(x for x in st if x.isupper())
even = list(x for x in st if x.isnumeric() and int(x) % 2 == 0)
odd = list(x for x in st if x.isnumeric() and int(x) % 2 != 0)

output="".join(sorted(lower)+sorted(upper)+sorted(odd)+sorted(even))
print(output)
# print(lower, upper, even, odd)
