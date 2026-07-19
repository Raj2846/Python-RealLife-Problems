"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2 
"""

def swap_case(s):
    out=[]
    for i in s:
        if i.islower():
            out.append(i.upper())
        elif i.isupper():
            out.append(i.lower())
        else:
            out.append(i)
    
    return "".join(out)


def opt_swap_case(s):
    return "".join([i.upper() if i.islower() else i.lower() for i in s])

if __name__ == '__main__':
    s = input()
    result = opt_swap_case(s)
    print(result)            