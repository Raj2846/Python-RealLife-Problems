"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
#Brutal Force Method
def two_sum(nums,target):
    for i in range(len(nums)-1):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target:
                return ((i,j))
# ans=two_sum([3,3,4],6)
# print(ans)

#hash mapping
#enumerate() return the tuple of the index and value in the list
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
            
# ans=twoSum([3,2,4],6)
# print(ans)


def sec_high(nums):
    max_num=0
    sec_high_max=0
    
    for i in nums:
        if i > max_num:
            sec_high_max=max_num
            max_num=i
        elif i > sec_high_max and i != max_num:
            sec_high_max=i
    return sec_high_max        
    
nums=[10, 5, 20, 8, 20, 15]
print(sec_high(nums))