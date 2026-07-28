array=[2,5,1,7,10]

"""
2.Longest Subarray /SubString where (condition)
"""

#better solution time com: O(2n) space com:O(1)
def longest_subarray(arr,k):
    l,r,sum,maxlen = 0,0,0,0
    
    while(r<len(arr)):
        sum=sum+arr[r]
        
        #to check the if the sum is > the k then we will move l front 
        while(sum > k):
            sum=sum-arr[l]
            l+=1
        
        # to update maxlen when ever the total sum is smaller then K until we find the longest length
        if sum <= k:
            maxlen=max(maxlen,r-l+1)
        #incrementing r to get the maxlength < k i.e comparing all posibilities
        r+=1
    print(maxlen)
            
    
def opti_longest_sunarray(arr,k):
    l,r,sum,maxlen = 0,0,0,0
        
    while(r<len(arr)):
        sum=sum+arr[r]
        
        #to check the if the sum is > the k then we will move l front . we use if here instead of while to that we dont have to every time shirnk the l to the satisfy teh condition we will just not let it decrease the it already is so i.e 2+5+1+10 is 18 so we will just increase l one time to make it to maxlen 3 so 5+1+10 then i will increase the r to go furthur and continue
        #this only work if we are said to find the length if told to find the subarray to then not.
        if(sum > k):
            sum=sum-arr[l]
            l+=1
        
        # to update maxlen when ever the total sum is smaller then K until we find the longest length
        if sum <= k:
            maxlen=max(maxlen,r-l+1)
        #incrementing r to get the maxlength < k i.e comparing all posibilities
        r+=1        
    print(maxlen)

#opti_longest_sunarray(array,14)

"""
3. No of subarray where (conditions) . Solve using the pattern 2
"""

# assume that the condition is to find sum no of subarray sum =k(any number)
#so here the condition is constant not greater to or less than it want exactly K 
# so here we will do two things 1. find (no of subarray where sum <= K)so this is X 2. find (no of subarray where sum <=(K-1) and this is Y
#now the ans will be X-Y always

"""
4. Finding the shortest or minimum where (condition)
"""
#l,r if we find valid window we will shrink ie increment l and se if that shrinked window is valid or not  and store it as an ans



