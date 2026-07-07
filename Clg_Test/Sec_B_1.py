"""Q7. Building the Order Engine at ‘The Spice Route’  (Python — OOP & Persistence)	
The Spice Route’s dinner rush peaks at 300 orders per hour and the hand-written KOT (Kitchen Order Ticket) system has collapsed. You are hired to build the core order engine in Python. Business rules: every menu item has a name and base price; Food items attract 5% GST; Beverage items attract 12% GST; any item flagged as a ‘Chef’s Special’ carries a 10% premium on the base price before tax. At closing time, the day’s orders must be saved to disk so accounts can audit them the next morning.
"""

from abc import ABC,abstractmethod

class MenuItem(ABC):
    def __init__(self,name,base_price,chef_special=False):
        self._name=name
        self._base_price=base_price
        self._chef_special=chef_special
    
    @property
    def name(self):
        return self._name
    
    @property
    def base_price(self):
        return self._base_price
    
    @property
    def chef_special(self):
        return self._chef_special
    
    @abstractmethod
    def final_price(self):
        pass
    

class Food(MenuItem):
    def __init__(self,name,base_price,chef_special=False):
        super().__init__(name,base_price,chef_special)
        
    def final_price(self):
        price=self.base_price
        
        if self.chef_special:
            price*=1.10
        price*=1.05
        
        return round(price,2)

class Beverage(MenuItem):
    def __init__(self,name,base_price,chef_special=False):
        super().__init__(name,base_price,chef_special)
        
    #overrides the final_price in the parent class to specific requirement in this class
    def final_price(self):
        price=self.base_price
        
        if self.chef_special:
            price*=1.10
        price*=1.12
        
        return round(price,2)
    
    
    
class Order:
    def __init__(self):
        self.__items=[]
        
    def add_item(self,item):
        self.__items.append(item)
        
    @property
    def items(self):
        return self.__items
    
    def __apply_discount(self,total):
        if total > 2000:
            return total *0.90
        return total
    
    def bill_total(self):
        total=0
        
        for item in self.__items:
            total+= item.final_price()
        
        return round(self.__apply_discount(total),2)
    
    
import json 

def save_day(orders,filepath):
    data=[]
    for order in orders :
        items=[]
        for item in order.items:
            items.append({
                "type":item.__class__.__name__,
                "name":item.name,
                "base_price":item.base_price,
                "chef_special":item.chef_special
            })
        data.append(items)
    
    with open(filepath,"w") as file:
        json.dump(data,file,indent=4)
        
        

def load_day(filepath):
    orders=[]
    try:
        with open(filepath,"r") as file:
            data=json.load(file)
            
            for order_data in data:
                order=Order()
                
                for item in order_data:
                    if item["type"]=="Food":
                        obj=Food(
                            item["name"],
                            item["base_price"],
                            item["chef_special"]
                        )
                    else:
                        obj=Beverage(
                            item["name"],
                            item["base_price"],
                            item["chef_special"]
                        )
                    order.add_item(obj)
            orders.append(order)
            
    except FileNotFoundError:
        return []
    
    return orders  
    

# 40
    
    
"""
The Scoreboard Backbone of Rannbhoomi 2026  (SQL — Schema, Joins & Optimization)
Rannbhoomi 2026 is an inter-university sports tournament: 64 universities, 12 sports, 900+ matches over 10 days. You are the database lead. The live scoreboard portal is expected to serve 50,000 concurrent viewers, and organizers want instant answers to questions such as ‘current points table per sport’ and ‘leading scorer of the tournament’.
"""

"""
Team:
team_id int primary key,
team_name varchar(50) not null,
university_name varchar(100) not null,
team_member_count int not null,


Player:
pl_id int primary key,
pl_name varchar(50) not null,
pl_age int check pl_age >= 18,
team_id foreign key reference Team,

Match:
mt_id int primary key,
sport varchar(25) not null,
mt_time int not null,
mt_date date not null,
team1_id int foreign key reference Team,
team2_id int foreign key reference Team,
winner_team_id int foreign key reference Team,


MatchScore:
mts_id int primary key,
team_id int foreign key reference Team,
player_id int foreign key reference Player,
match_id int foreign key reference match,
score int chech(score>=0),



select t.team_name,count(m.m_id) as matched_played,
    sum(CASE
        when m.winner_team_id = t.team_id THEN 1
        ELse 0
        END
    ) as wins,
    sum(CASE
        when m.winner_team_id <> t.team_id THEN 1
        ELSE 0
        END
    ) as losses,
    sum(CASE
        when m.winner_team_id = t.team_id THEN 2
        ELSE 1
        END
    ) as points
From Team t Join Match m on t.team_id = m.team1_id or t.team_id = m.team2_id

When m.sport ="Basketball"
Group by t.team_is,t.tea_name
Order by points DESC;

"""


"""
Q9
Three Branches, One Balance Sheet  (Linear Algebra — Matrix Operations)
ChaiCode, a bootstrapped startup, runs three campus kiosks: LJ Campus, GU Campus, and PDEU Campus. It sells three products: Masala Chai, Cold Coffee, and Brownie. Yesterday’s unit sales and the unit-price list are given below.

"""
s=[
    [120,80,40],
    [90,110,30],
    [150,60,50]
]

p=[20,60,50]

r=[(s[0][0]*p[0])+(s[0][1]*p[1])+(s[0][2]*p[2]),
   (s[1][0]*p[0])+(s[1][1]*p[1])+(s[1][2]*p[2]),
   (s[2][0]*p[0])+(s[2][1]*p[1])+(s[2][2]*p[2])
   ]

print(f"LJ Campus net sale is {r[0]}\nGu Campus net sale is {r[1]}\nPDEU Campus net sale is {r[2]}")

r_s=[((0.9*s[0][0])*p[0])+((0.9*s[0][1])*p[1])+((0.9*s[0][2])*p[2]),
   (0.9*(s[1][0])*p[0])+(0.9*(s[1][1])*p[1])+(0.9*(s[1][2])*p[2]),
   (0.9*(s[2][0])*p[0])+(0.9*(s[2][1])*p[1])+(0.9*(s[2][2])*p[2])
   ]

print(f"LJ Campus net sale is {r_s[0]}\nGu Campus net sale is {r_s[1]}\nPDEU Campus net sale is {r_s[2]}")

r_p=[(s[0][0]*(0.9*p[0]))+(s[0][1]*(0.9*p[1]))+(s[0][2]*(0.9*p[2])),
   (s[1][0]*(0.9*p[0]))+(s[1][1]*(0.9*p[1]))+(s[1][2]*(0.9*p[2])),
   (s[2][0]*(0.9*p[0]))+(s[2][1]*(0.9*p[1]))+(s[2][2]*(0.9*p[2]))
   ]

print(f"LJ Campus net sale is {r_p[0]}\nGu Campus net sale is {r_p[1]}\nPDEU Campus net sale is {r_p[2]}")


"""
Q10
The Server Room Gamble at Meridian Corp  (Probability — Bayes & Binomial)
"""


"""
Q11
Spreading the Word at Kshitij Fest  (DSA — Graph Modelling & BFS)SCENARIO:  At Kshitij Fest, an urgent venue change must reach 800 student volunteers. There is no broadcast channel; messages travel person-to-person through a ‘buddy network’ — each volunteer has a known list of buddies they can instantly reach. The core organizing team (3 members) starts the relay. Every ‘hop’ takes roughly one minute. The control room wants the message to reach everyone in the minimum number of hops, and wants to know in advance who will be unreachable.

1:
Vertices: 800 volunteers.
Edges: Buddy connections between volunteers.
Graph Type: Undirected graph.
Representation: Adjacency List.
Justification: An adjacency list uses O(V + E) space and is ideal for a sparse graph, whereas an adjacency matrix requires O(V²) space (640,000 entries for 800 volunteers), making it much less memory-efficient.

2:
Depth-First Search (DFS) explores one path as deeply as possible before backtracking. It does not guarantee the shortest path (minimum hops), so it is not suitable for this problem.
"""
#2
#with Impotrs one
from collections import deque

def multi_source_bfs(graph, sources):
    
    queue = deque()

    distance = {}

    #inInitially nobody has received the message. so mark every vertex as -1
    for vertex in graph:
        distance[vertex] = -1

    #sourece means the orginazer who already know the message before circulation
    for source in sources:
        queue.append(source)
        distance[source] = 0

    while queue:
        #femoving the first from the queue
        #how many hoos did it take to reach the current element
        current = queue.popleft()

        #visiting the neighbour fo the first element in the queue
        for neighbour in graph[current]:
            #checking if the element is already visited oe not
            if distance[neighbour] == -1:
                #if not visited then we increase the number of hops sa it shows that, that element is how many hops away from the source
                distance[neighbour] = distance[current] + 1
                queue.append(neighbour)

    return distance

#without imports one

def bfs(graph,sources):
    queue=[]
    distance={}
    
    for vertex in graph:
        distance[vertex]=-1
        
    for source in sources:
        queue.append(source)
        distance[source]=0
        
    while len(queue)>0 :
        current=queue.pop(0)
        
        for neighbour in graph[current]:
            if distance[neighbour] == -1:
                distance[neighbour] = distance[current]+1
                queue.append(neighbour)
                
    return distance


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}
source=['A','D']
hops=bfs(graph,source)
print(hops)

"""
Q3
Detection: After BFS, any volunteer whose distance remains -1 is unreachable and will not receive the message.
Graph Property: Their existence indicates that the graph is disconnected, meaning some volunteers are in separate connected components with no path from the three core-team members.
"""

"""
Q12
Round Two: Sorting a Million Candidates  (DSA + Architecture — Sorting, Searching, Memory Hierarchy)	[10 Marks]
SCENARIO:  You have cleared Round One. The interviewer at the ticketing startup now hands you a systems-flavoured problem: ‘Our national hiring drive produced 1 million candidate records, each with a composite score. We must (i) rank all candidates, (ii) repeatedly answer queries like “does any candidate have exactly score X?”, and (iii) — the twist — the full dataset does not fit in the RAM of our evaluation machine.’


1.
It guarantees O(n log n) performance even in the worst case, which is important when sorting 1 million candidate records.
It is stable, meaning if two candidates have the same score, their original order is preserved. This is useful if there is a secondary ranking criterion (e.g., application time).
Although it requires O(n) extra memory, its predictable performance makes it suitable for large datasets

2.
Since the candidate scores are already sorted, Binary Search is the most efficient algorithm to search for a particular score.
After approximately 20 halvings, only one record remains.

3.
External Merge Sort is used when the dataset is larger than the available RAM. The file is divided into smaller chunks that fit into RAM, each chunk is sorted and stored back on the disk, and finally all sorted chunks are merged into one sorted file. It exploits the memory hierarchy by using fast RAM for computation and slower disk for storage. Sequential disk access is preferred because it is much faster than random access, reducing disk seek time and improving overall performance.
"""

