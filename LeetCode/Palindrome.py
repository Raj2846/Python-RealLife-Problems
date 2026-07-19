"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if str(x)==str(x)[::-1]:
            return True
        else:
            return False
            