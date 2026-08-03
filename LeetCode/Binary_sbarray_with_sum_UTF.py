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
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):

        def atMost(goal):
            if goal < 0:
                return 0

            left = 0
            curr_sum = 0
            count = 0

            for right in range(len(nums)):
                curr_sum += nums[right]

                while curr_sum > goal:
                    curr_sum -= nums[left]
                    left += 1

                count += right - left + 1

            return count

        return atMost(goal) - atMost(goal - 1)