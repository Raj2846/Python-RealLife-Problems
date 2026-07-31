"""
number of substring contining all the 3 character 
"""


s = 'bbacba'
# ord('a') convert charcter into int ascii value
#one way for brutal
def brute(arr, k):
    count = 0
    for i in range(len(arr)):
        hash = {}
        for j in range(i, len(arr)):
            hash[ord(arr[j])-ord('a')] = 1
            if hash.get(0, 0) + hash.get(1, 0) + hash.get(2, 0) == 3:
                # count += 1
                
                #this method is little bit good as we get a substring where we get all the chracter then the next all the element that is going to the substring are going to be valid , like bbac now left is ba so i know that if i add ba its still going to be valid so what do we do is we count+ len(arr) - j i.e 6-3=3 and add it to the count and break 
                count=count+ (len(arr)-j)
                break
    print(count)

#second way of brutal more pythonic
def brutal_sec(arr,k="abc"):
    count=0
    for i in range(len(arr)):
        hash={}
        for j in range(i,len(arr)):
            hash[arr[j]]=1
            
            if all(ch in hash for ch in k):
                count+=(len(arr)-j)
                break
    return (count)
