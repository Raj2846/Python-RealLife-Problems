"""

"""

s = 'aaabbccd'
k = 2


def brutal(s, k):
    max_l = 0
    for i in range(len(s)):
        dt = set()
        for j in range(i, len(s)):
            dt.add(s[j])

            if len(dt) <= k:
                max_l = max(max_l, j-i+1)
            else:
                break
    return max_l


# print(brutal(s, k))


def opti(s, k):
    left_p = 0
    max_l = 0
    dt = {}

    for right in range(len(s)):
        if s[right] not in dt:
            dt[s[right]] = 1
        else:
            dt[s[right]] += 1
            
        if len(dt) > 2:
            dt[s[left_p]]= dt[s[left_p]]-1
            
            if dt[s[left_p]]==0:
                dt.pop(s[left_p])
                
            left_p+=1
            
        max_l=max(max_l,right-left_p+1)
        
    return max_l

print(opti(s,k))
