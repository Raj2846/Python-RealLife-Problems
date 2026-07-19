
"""
You are given an immutable string, and you want to make changes to it.
one method :
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra

second method:
>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
"""


def mutate_string(string, position, character):
    ls=list(string)
    ls[position] = character
    st="".join(ls)
    return st
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)