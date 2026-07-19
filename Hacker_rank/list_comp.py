"""
Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of i+j+k  is not equal to . Here, 0 <= i <= x ,0 <= j <= y,0 <= k <= z   
"""

def ls_com():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n])

if __name__ == '__main__':
   ls_com()