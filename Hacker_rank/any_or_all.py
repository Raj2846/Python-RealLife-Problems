"""
You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
"""

n=int(input())
num_sep=list(map(int,input().split()))
def check(n,num_sep):
    is_pali=False
    for i in num_sep:
        i_s=str(i)
        if i < 0:
            return False
        if i_s == i_s[::-1]:
            is_pali= True    
    return is_pali
out=check(n,num_sep)
print(out)
