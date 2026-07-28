"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
"""
arr = [686, 28, 455, 675, 605, 29, 942, 48, 502, 889, 854, 206,
       231, 796, 272, 565, 887, 969, 558, 13, 22, 455, 145, 804, 15]
k = 515854
# arr=[1,2,3,4,5,6,7,8,9,10]


def brutForce(arr, k):
    count = 0
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product = product * arr[j]
            if product < k:
                count += 1
    return (count)


brutForce(arr, k)


def opti_code(nums, k):
    if k <= 1:
        return 0
    count = 0
    product = 1
    left = 0
    for right in range(len(nums)):
        product *= nums[right]
        while product >= k:
            product //= nums[left]
            left += 1
        count += right - left + 1
    return count


print(opti_code(arr, k))
