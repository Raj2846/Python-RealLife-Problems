"""
Given a string with upper case letter and k 
k signifise that, at most  k character from the given string i can select atmost any k character and then convert them to any other possible letter 
once done we have to figure out the longest substring having all the charcter as equal

"""
s = 'AAAABBCCD'
k = 2


def brute_force(s, k):
    max_l = 0
    changes = 0
    for i in range(len(s)):
        hash = {}
        max_freq = 0
        for j in range(i, len(s)):
            if s[j] in hash:
                hash[s[j]] += 1
            else:
                hash[s[j]] = 1
            max_freq = max(max_freq, hash[s[j]])
            changes = (j-i+1) - max_freq
            if changes <= k:
                max_l = max(max_l, (j-i+1))
            else:
                break

    return (max_l)


print(brute_force(s, k))


def optimal_solution(s, k):
    left_p, max_l, max_f= 0, 0, 0
    hash_m = {}
    for right in range(len(s)):
        if s[right] in hash_m:
            hash_m[s[right]] += 1
        else:
            hash_m[s[right]] = 1
            
        max_f = max(max_f, hash_m[s[right]])
        
        if (right-left_p+1) - max_f <= k :
            max_l=max(max_l,right-left_p+1)
        else:
            hash_m[s[left_p]] = hash_m[s[left_p]] - 1
            left_p+=1
    return max_l

print(optimal_solution(s,k))
