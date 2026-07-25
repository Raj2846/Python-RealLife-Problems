"""
Max consecutive ones part 3
You can flip atmost k zero to figure the most contineous 1 in the list/array
"""

"""
#We can think t like finding the longest subarray with atmost of K zeroes
"""


arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

# brute force


def brute(arr, k):
    max_len = 0
    for i in range(0,len(arr)):
        zero = 0
        for j in range(i, len(arr)):
            if arr[j] == 0:
                zero += 1
            if zero <= k:
                len_ = j-i+1
                max_len = max(len_, max_len)

    return max_len
# print(brute(arr, k))


#time com : O(2n) space com:O(1)
def opti(arr,k):
    left_p=0
    zeroes=0
    max_l=0
    for right in range(len(arr)):
        if arr[right]==0:
            zeroes+=1
        
        while zeroes > k:
            if arr[left_p]==0:
                zeroes-=1
            left_p+=1
            
        if zeroes <=k:    
            max_l=max(max_l,(right-left_p+1))
    
    return (max_l)
    
print(opti(arr,k))

#time com : O(n) space com:O(1)
def opti(arr,k):
    left_p=0
    zeroes=0
    max_l=0
    for right in range(len(arr)):
        if arr[right]==0:
            zeroes+=1
        
        if zeroes > k:
            if arr[left_p]==0:
                zeroes-=1
            left_p+=1
            
        if zeroes <=k:    
            max_l=max(max_l,(right-left_p+1))
    
    return (max_l)
