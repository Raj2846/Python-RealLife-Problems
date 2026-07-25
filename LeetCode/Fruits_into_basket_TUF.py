"""
Fruite into the baskets
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
"""
# number are the type like number 3 indicates apple , 2 =orange 1=chickoo
arr = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]

# We can think it like max length subarray with at most 2 types of numbers.


def brute(arr):
    max_l = 0
    for i in range(len(arr)):
        abc = set()
        for j in range(i, len(arr)):
            abc.add(arr[j])

            if (len(abc)) <= 2:
                max_l = max(max_l, j-i+1)
            else:
                break
    return (max_l)

# print(brute(arr))


def opti(arr):
    left_p=0
    max_l=0
    st=dict()
    
    for right in range(len(arr)):
        
        #inserting into dictionaary all the element and ints frequency
        if arr[right] not in st:
            st[arr[right]] = 1
        else:
            st[arr[right]] += 1
            
            
        #we are checking that the if the length is greater then 2 then we increment the left_p and decrease the frequency of that element in the dictionary and contiue if the frequency becomes 0 pop that item so that the length of the dictionary decreases and satisfy the condition
        if len(st) > 2:
            # while len(st)>2:
                #decreasing frequency
                st[arr[left_p]]=st[arr[left_p]]-1
                
                #if frequency 0 then pop that element
                if st[arr[left_p]]==0:
                    st.pop(arr[left_p])
                
                #increment left pointer
                left_p+=1
            
        #if within length then calculate max length
        if (len(st)) <= 2:
            max_l = max(max_l,right-left_p+1)
    return max_l

print(opti(arr))