"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

#1st solution
"""
class Solution(object):
    def threeSum(self, nums):
        
        # :type nums: List[int]
        # :rtype: List[List[int]]
        
        nums.sort()
        result=[]
        for i in range(len(nums)):
            #Through this condition we are going to the 1st element so we used nums[i-1] to compare it with the previous element
            if i > 0 and nums[i]==nums[i-1]:
                continue
            
            #setting the pointer in each direction
            left=i+1
            right=len(nums)-1
            
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    #we will skip all the duplicate values from the left and right side so the output never repeats itself
                    while left <right and nums[left] == nums[left+1]:
                        left+=1
                        
                    while left <right and nums[right] == nums[right-1]:
                        right-=1
                        
                    left+=1
                    right-=1
                    
                #as we have negative values on left side so when total < 0 so we will increment the left side to we minus less valued number
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result   
"""
  
# 2nd solution optimized                        
# """  
class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        count = {}
        unique = []
        
        for num in nums:
            if num not in count:
                count[num] = 1
                unique.append(num)
            elif count[num] < 3:
                count[num] += 1

        result = []
        u = len(unique)
        
        for i in range(u):
            a = unique[i]

            # if the ith element is >0 means 3 so after that ther is 4 so there are no chances to make it 0
            if a > 0:
                break
            
            #if there are 0 3times then this is the one set of output
            if a == 0:
                if count[0] >= 3:
                    result.append([0, 0, 0])
                break  

            # if both condition not right then 
            for j in range(i, u):
                b = unique[j]
                #instead on finding all the number we will find the number needed so a+b+c=0 then c=-(a+b)
                c = -(a + b)
                
                #it is to optimize it so c can be never smaller then b or else its wont give the output
                if c < b:
                    break
            
                if c in count:
                    #here we used count[a] < 2 so that if that number is only less than 2 in the hash map its can be only used once and same for count[b] < 2 . we need atleast 2 copies of the number
                    if a == b and count[a] < 2:
                        continue
                    if b == c and count[b] < 2:
                        continue 
                    if a <= b <= c:
                        result.append([a, b, c])
        
        return result   
    # """ 

num=[-1,0,1,2,-1,-4]
s=Solution()
ans=s.threeSum(num)
print(ans)