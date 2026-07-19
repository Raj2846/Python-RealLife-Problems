"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.


Solution :
Find the length of the substring.
Move through the string one character at a time.
At each position, extract a piece of the string having the same length as the substring.
Compare it with the substring.
If they are equal, increase the count.
"""

def count_substring(string,sub_string):
    count=0
    len_sub=len(sub_string)
    for i in range(0,len(string)):
        if string[i:i+len_sub]== sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)