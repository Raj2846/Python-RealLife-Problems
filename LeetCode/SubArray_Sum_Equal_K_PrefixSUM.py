"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
"""


def subarraySum( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    count=0
    prefix_sum=0
    hash_m=dict({0:1})
    for i in range(len(nums)):
        prefix_sum+=nums[i]
        target=prefix_sum-k
        
        if target in hash_m:
            count+=hash_m.get(target)
        
        hash_m[prefix_sum] = hash_m.get(prefix_sum,0)+1
        
    return count


nums=[1,2,3];k=3
print(subarraySum(nums,k))