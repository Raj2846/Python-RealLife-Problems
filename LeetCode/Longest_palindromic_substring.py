"""
Given a string s, return the longest palindromic substring in s.
"""


def longestPalindrome(s):
    if len(s) < 2:
        return s

    start = 0
    end = 0

    for i in range(len(s)):

        # Odd-length palindrome
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left > end - start:
                start = left
                end = right

            left -= 1
            right += 1

        # Even-length palindrome
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left > end - start:
                start = left
                end = right

            left -= 1
            right += 1

    return s[start:end + 1]