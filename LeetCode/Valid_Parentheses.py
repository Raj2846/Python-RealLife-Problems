"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    #if there is till element left in the stack then its will return direct false as its not the correct parentheses
    return len(stack) == 0


s = "([])"
ans = isValid(s)
print(ans)
