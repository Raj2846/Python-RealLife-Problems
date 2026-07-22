"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        #Iterate the array counting number of 0's, 1's, and 2's.
        dt={}
        for i in nums:
            if i in dt:
                dt[i]+=1
            else:
                dt[i]=1
                
        arr = []
        # for key in sorted(dt):
        #     arr.extend([key] * dt[key])
        for i in range(0,len(dt)):
            if i in dt:
                arr.extend([i] * dt[i])
        return arr
    
"""
class Solution(object):
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
"""    
nums=[2,0,2,1,1,0]
s=Solution()
s.sortColors(nums)