"""
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print
"""



def print_formatted(number):

    width = len(format(number, 'b'))

    for i in range(1, number + 1):

        decimal = str(i)
        octal = format(i, 'o')
        hexa = format(i, 'X')
        binary = format(i, 'b')

        print(decimal.rjust(width),
              octal.rjust(width),
              hexa.rjust(width),
              binary.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    