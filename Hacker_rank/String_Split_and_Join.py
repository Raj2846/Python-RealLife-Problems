"""
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""

def split_and_join(line):
    st=line.split()
    out="-".join(st)
    
    print(out)
    
split_and_join(" a string of space-separated words")