"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
"""
class Solution(object):
    def moveZeroes(self, nums:list):
        # :type nums: List[int]
        # :rtype: None Do not return anything, modify nums in-place instead.
        for i in nums:
            if i==0:
                nums.append(i)
                nums.remove(i)
        return nums  
    
"""
    
class Solution(object):
    def moveZeroes(self, nums:list):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
         """
        # here we hace used two pointer approach where one keep track of non-zero elements and other of zero
        write=0
        #here read traverse through the list and find non-zero elements and write is other pointer which is moved when an zero is ancounter in the list
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write]=nums[read]
                write+=1
        while write <= read:
            # if write < read:
                nums[write]=0
                write+=1
        return nums   
        
nums=[0,1,0,3,12]
s=Solution()
s.moveZeroes(nums)