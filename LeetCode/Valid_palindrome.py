"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

"""


def validPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    left = 0
    right = len(s)-1
    while (left < right):
            if s[left] != s[right]:
                return ispalindrome(s,left+1,right) or ispalindrome(s,left,right-1)
            left+=1
            right-=1
    return True
    
def ispalindrome(s,left,right):
    while (left < right):
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True

    
    
