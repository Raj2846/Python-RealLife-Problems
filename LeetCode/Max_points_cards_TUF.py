"""
maximum points you can obtain from cards
condition is either pick up from the front or from back not from middle and that to continuously not skipping cards
eg. 6,2,3,4 or 1,7,1,2 or 1,7,6,2 here 2 from back and 2 from front
k is the number of card to pick to find the max point
"""
arr=[6,2,3,4,7,2,1,7,1]
k=4

def max_point(arr,k):
    l_sum,r_sum,max_sum=0,0,0
    
    #this loop first takes the left side four element and add it and save it
    for i in range(0,k):
        l_sum=l_sum+arr[i]
        max_sum=l_sum
    
    #this loop remove 1 element from left side and minus it from the left side and then take an element from the right side and add it to the total sum until there is 0 element from the left side and k element from right side
    # time com : O(2K) space com :O(1)
    
    #r_idx to traverse from the right side 
    r_idx=len(arr)-1
    for i in range(k-1,0,-1):
        l_sum=l_sum-arr[i]
        r_sum=r_sum+ arr[r_idx]
        r_idx-=1
        
        max_sum=max(max_sum,(l_sum+r_sum))
    print(max_sum)
    
max_point(arr,k)


def opti_max_point(arr,k):
    left_s=sum(arr[:k])
    max_sum=left_s
    right_s=0
    
    right=len(arr)-1
    for i in range(k-1,0,-1):
        left_s-=arr[i]
        right_s+=arr[right]
        right-=1
        
        max_sum=max(max_sum,(left_s+right_s))
    print(max_sum)
    
opti_max_point(arr,k)