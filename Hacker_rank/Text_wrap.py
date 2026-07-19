"""
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
"""

import textwrap

def wrap(string, max_width):
    out=""
    for i in range(0,len(string),max_width):
        out +=string[i:i+max_width]+"\n" 
    return out.rstrip()

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
