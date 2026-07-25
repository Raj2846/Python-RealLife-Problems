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
            #we are making L jump to direct to the index where the duplicate is found so that we skip the string if this max_len is smaller then the max_len calculated 
            left_p=max(left_p,hash[s[i]]+1)

        #here we are inserting the element we have visited into the hash for future reference
        hash[s[i]]=i

        #finding the max len from the previous calculated and the one now
        max_len=max(right_p-left_p+1,max_len)
        #incrementing the right if no duplicate found
        right_p+=1
        
    print(max_len)
    
opti_solution(s)

#More Pythonic way to the solution of above 
def lengthOfLongestSubstring(s):
    left = 0
    seen = {}
    ans = 0

    #enumerate gives both the value and the index of the element makes the work easy ,first index then value
    for right, ch in enumerate(s):
        if ch in seen:
            #if ch in hash update the left to the ch index
            left = max(left, seen[ch] + 1)

        #if not insert into hash
        seen[ch] = right
        #find max from the length calculated
        ans = max(ans, right - left + 1)

    return ans