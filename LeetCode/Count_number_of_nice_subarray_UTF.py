"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
"""
nums = [1,1,2,1,1];k = 3
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):

        def atMost(goal):
            if goal < 0:
                return 0

            left = 0
            curr_sum = 0
            count = 0

            for right in range(len(nums)):
                curr_sum += (nums[right]%2)

                while curr_sum > goal:
                    curr_sum -= (nums[left]%2)
                    left += 1

                count += right - left + 1

            return count

        return atMost(goal) - atMost(goal - 1)