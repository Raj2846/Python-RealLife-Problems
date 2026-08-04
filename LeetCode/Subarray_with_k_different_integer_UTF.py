"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
"""

nums=[1,2,1,3,4];k=3
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
def brutal_force(nums,k):
    count=0
    for i in range(len(nums)):
        hash_h={}
        for j in range(i,len(nums)):
            if nums[j] not in hash_h:
                hash_h[nums[j]]=1
            else:
                hash_h[nums[j]]+=1
                
            if len(hash_h) == k:
                count+=1
            elif len(hash_h) > k:
                break
    return count

print(brutal_force(nums,k))