"""Merge Sort – The IRCTC Waitlist Merger
IRCTC has two separately sorted waitlists — one from its mobile app, one from railway counters. To produce a final unified waitlist, they don't re-sort from scratch. They merge both sorted lists in one pass — compare the front of each list, pick the smaller token, advance. This is exactly merge sort's merge step."""


mobile_app=[101,103,105,107,112]
counter=[102,104,106,108,115]

merged_list=[]

i=0
j=0

# merge logic : this will add the smallest from each into the new list
while i<len(mobile_app) and j<len(counter):
    if mobile_app[i] < counter[j]:
        merged_list.append(mobile_app[i])
        i+=1
    else:
        merged_list.append(counter[j])
        j+=1
        
# this will add the remaining list from mobile_app
while i< len(mobile_app):
    merged_list.append(mobile_app[i])
    i+=1 

while j<len(counter):
    merged_list.append(counter[j])
    j+=1
    
print("Merged list is : ")
print(merged_list)