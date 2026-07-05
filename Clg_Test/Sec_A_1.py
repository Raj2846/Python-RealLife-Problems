"""Q1. The Midnight Crash at NimbusPay  (Python — File Handling & Exceptions)

TXN4521 | 2026-07-02 23:41:07 | 1499.00 | FAILED
"""

import os
def crash_report(filepath):
    count=0
    total_amount=0
    corrupted_count=0
    try:
        if os.path.exists(filepath):
            with open(filepath,"r") as fp:

                try:
                    for i in fp:
                        lines=i.strip().split("|")
                        if len(lines) != 4:
                            raise ValueError("Missing fields")
                        if lines[3]=="FAILED":
                            count+=1
                            total_amount+=float(lines[2])
                        # print(count,total_amount)
                    # output=tuple((count,total_amount))
                except (ValueError,IndexError):
                    corrupted_count += 1
        else:
            raise FileNotFoundError
    except FileNotFoundError :
        print("File not found at the current directory")
    except ValueError :
        print("value are missing in the files")
        
    return (count,total_amount,corrupted_count)
  
# ans=crash_report("sample_log.txt")
# print(ans)



"""Q2. Pricing Strategy at ‘The Spice Route’  (SQL — Subqueries & Ranking)
The Spice Route’, a high-volume restaurant chain, wants to reprice its menu. Management needs to identify the second-most expensive dish within every culinary category (Starters, Mains, Desserts, Beverages) — not overall — so category managers can adjust anchor pricing.

MenuItem :table
m_id int pk
m_name varchar
m_price float check(price > 0)
category varchat(50)


create table MenuItem(
    m_id int primary key,
    m_name varchar(100) not null,
    category varchar(50) not null,
    m_price decimal(10,2) not null,
    check(m_price > 0)  
)

query :
select m1.m_name,m1.category,m1.m_price from menuitem m1
where 1 = (select count(distinct m2.m_price) from menuitem m2
            where m2.category = m1.category and m2.m_price > m1.m_price
            );
            
            
Easy version first find the max from the table and then find the less than max i.e second highest price 

select m1.m_name,m1.m_price,m1.category from MenuItem m1 
where m1.m_price = (
    select max(m2.price) from MenuItem m2 where m2.category = m1.category and m2.m_price <(
        select max(m3.m_price) from MenuItem m3
        where m3.category = m2.category
    ) 
);

"""

"""The Footfall Debate at Kshitij Fest  (Descriptive Statistics)	[5 Marks]
SCENARIO:  The organizing committee of Kshitij, an inter-university cultural festival, recorded hourly footfall at the main gate on Day 1 (10 a.m.–7 p.m.):
420, 380, 450, 400, 410, 390, 430, 440, 3200
The 6 p.m. spike of 3,200 occurred because a celebrity performer arrived. The sponsorship team wants to quote ‘average hourly footfall’ to sponsors; the audit team objects.
"""
"(a)"
import pandas as pd
df=pd.DataFrame([420,380,450,400,410,390,430,440,3200])
def mean_medina():
    print("\n")
    print("Mean of the Festival is:")
    mean_df=df.mean()
    print(mean_df)

    print("\n")
    print("Median of the Festival is:")
    median_df=df.median()
    print(median_df)

    std_df=df.std()
    print(std_df)

"""(b) Which measure should be reported?

The committee should report the Median.

Justification:

The value 3200 is an outlier caused by the celebrity's arrival.
This outlier makes the distribution positively (right) skewed.
The mean (724.44) is pulled upward by the outlier and does not represent a typical hourly footfall.
The median (420) is not affected by the outlier and better represents the normal hourly attendance."""




"""Round One: The Duplicate Ticket Problem  (DSA — Complexity Trade-offs)	[5 Marks]
SCENARIO:  You are in the first technical round of a campus placement interview at a ticketing startup. The interviewer says: ‘Our tournament app issued n digital ticket IDs (unsorted integers). A bug may have issued one ID twice. Detect whether any duplicate exists.’ She then adds: ‘Give me three different approaches — I care about how you reason about trade-offs, not just the answer.’
"""

lst=[420,380,450,400,410,390,430,440,3200,440]

def brutal_force(lst):
    count=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            count+=1
            if lst[i] == lst[j]:
                print(lst[i])
    print(count)
    
# brutal_force(lst)            

def binary_sort(start,stop,lst,target):
    if stop < start:
        return -1
    
    mid=(start+stop)//2
    if target == lst[mid]:
        return mid
    elif target < lst[mid]:
        return binary_sort(start,mid-1,lst,target)
    elif target > lst[mid]:
        return binary_sort(mid+1,stop,lst,target)        

    
def sorting_method(lst):
        #merge sort
        if len(lst)> 1:
            mid=len(lst)//2
            left= lst[:mid]
            right=lst[mid:]
            
            sorting_method(left)
            sorting_method(right)
            i=j=k=0
            
            while i<len(left) and j<len(right):
                if left[i] < right[j]:
                    lst[k]=left[i]
                    i+=1
                else:
                    lst[k] = right[j]
                    j+=1
                k+=1
            # this will add the remaining list from i
            while i< len(left):
                lst[k]=left[i]
                i+=1
                k+=1 

            while j<len(right):
                lst[k]=right[j]
                j+=1
                k+=1
                

def sorting_based(lst):
    sorting_method(lst)
    for i in range(len(lst)-1):
        if lst[i]==lst[i+1]:
            print(lst[i])
            
# sorting_based(lst)



#hashing based
def hashing_based(lst):
    visited=set()
    for i in lst:
        if i in visited:
            print(i)
        else:
            visited.add(i)
            
hashing_based(lst)