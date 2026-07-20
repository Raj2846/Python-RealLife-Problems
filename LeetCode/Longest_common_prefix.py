"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

"""
Approach is like :
take the shortest string from the list as there is not more to compare then the shortest string
after that run the loop till the length of the shortest string 
in the loop run the loop for every string in the list 
compare the shortest string 1st element with other string 1st element
break the loop if the values does not matche 
and return the shortest[:i] i.e till the i value in the loop as after the there is no common letter
"""

strs = ["flower","flow","flight"]    
def longest_common_prefix(strs):
    if not strs:
        return ""        
    shortest=min(strs,key=len)
    for i in range(len(shortest)):
        for word in strs:
            if word[i] != shortest[i]:
                return shortest[:i]
    return shortest


ans=longest_common_prefix(strs)
print(ans)