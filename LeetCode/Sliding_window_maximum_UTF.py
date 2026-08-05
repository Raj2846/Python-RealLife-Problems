"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

def maxSlidingWindow( nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        left=0
        max_v=0
        lst=list()
        for right in range(len(nums)):
            
            print("l , r",nums[left],nums[right])
            
             #as we are travesing from left to right , right pointer will be used to find the largest value
            if nums[right] > max_v:
                max_v=nums[right]
                    
                print("max :",max_v)
            
            
            #checking wether left and right are at the distance of k only 
            if (right-left+1) > k:
                left+=1
            
            lst.append(max_v)
            
            print(lst)
 
nums = [1,3,-1,-3,5,3,6,7]; k = 3       
maxSlidingWindow(nums,k)
            
            