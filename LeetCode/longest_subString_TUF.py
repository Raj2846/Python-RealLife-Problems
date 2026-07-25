"""
Longest substring without repeating the charcter
"""

s='cadbzewcd'

#this is the first approach Brutal force not so efficient as the time com is O(n^2)
def longest_subString(s):
    s_len=len(s)
    max_len=0
    for i in range(s_len):
        hash={}
        for j in range(i,s_len):
            if s[j] in hash:
                break
            len_=j-i+1
            max_len=max(len_,max_len)
            hash[s[j]]=1
            
    print(max_len)
# longest_subString(s)

def opti_solution(s):
    left_p=0
    right_p=0
    max_len=0
    hash={}
    for i in range(len(s)):
        if s[i] in hash:
            left_p=hash[s[right_p]]+1
            break
        hash[s[i]]=i
        right_p+=1
        max_len=max(right_p-left_p+1,max_len)
    print(max_len-1)
    
opti_solution(s)