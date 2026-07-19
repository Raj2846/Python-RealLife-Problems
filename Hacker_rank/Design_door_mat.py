"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""

n = int(input("Enter odd number only :"))
m=n*3
# 1. Top Half
for i in range(1,n,2):
    pattern =".|."*i
    print(pattern.center(m,"-"))
    
# middle half
print("Wlecome".center(m,'-'))
    
#botttom half
for i in range(n-2,0,-2):
    pattern = ".|." * i
    print(pattern.center(m, '-'))

def print_triangle(rows, char='*', padding=' '):
    # Calculate the maximum width the bottom row will take
    max_width = (rows * 2) - 1
    
    # Loop through each row to build the triangle
    for i in range(1, rows + 1):
        # Calculate the number of characters for the current row
        num_chars = (i * 2) - 1
        pattern = char * num_chars
        
        # Center the pattern using the padding character
        print(pattern.center(max_width, padding))

# Example usage: A triangle with 5 rows
# print_triangle(5)

