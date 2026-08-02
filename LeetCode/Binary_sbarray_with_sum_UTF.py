"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.
Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
"""

nums=[1,0,1,0,1];goal = 2
def optimal_solution(nums,goal):
    count=0;left=0;sum_s=0
    
    if goal < 0:
        return 
    for right in range(len(nums)):
        sum_s+=nums[right]
        
        if sum_s > goal:
            sum_s=sum_s-nums[left]
            left+=1
        count+=(right-left+1)
