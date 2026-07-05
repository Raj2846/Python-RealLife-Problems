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
import pandas as pd
df=pd.DataFrame([420,380,450,400,410,390,430,440,3200])
print(df)


