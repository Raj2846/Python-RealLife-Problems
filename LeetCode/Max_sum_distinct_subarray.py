arr=[1,5,4,2,9,9,9]
k=3    

class Solution(object):
    def opt_maximumSubarraySum(eslf,arr,k):
        max_s=0
        left_p=0
        # right_p=0
        sum=0
        seen=dict()
        
        for right_p in range(len(arr)):
            seen[arr[right_p]] = seen.get(arr[right_p],0)+1
                        
            sum=sum+arr[right_p]
            
            if right_p-left_p+1 > k:
                seen[arr[left_p]]-=1   
                if seen[arr[left_p]]==0:
                    del seen[arr[left_p]]                
                
                sum-=arr[left_p]
                #increment left pointer
                left_p+=1
                
            if right_p - left_p + 1 == k and len(seen) == k:
                max_s = max(max_s, sum)
            
        return max_s
                            

                
    
s=Solution()
print(s.opt_maximumSubarraySum(arr,k))
