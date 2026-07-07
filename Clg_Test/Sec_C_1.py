"""
Project ‘CampusBite’ — From Incubator Pitch to Festival Launch	[20 Marks]
SCENARIO:  Your four-member MCA team has been selected by the university incubator to build CampusBite — a food-ordering platform that will launch live during Kshitij Fest. Twelve food stalls, roughly 8,000 students, and a fleet of 25 student delivery runners on bicycles. Orders spike violently during event breaks (up to 40 orders per minute). The incubator jury will evaluate not just the product but the engineering judgement behind it.
The festival ground is mapped as 30 zones connected by walkable paths of known lengths (some paths close temporarily during events). A runner picks up from a stall’s zone and must reach the customer’s zone as fast as possible.
Answer the five parts below. Consistency across parts carries credit — your schema in Part 1 should support the code in Part 2 and the analytics in Part 4.
"""

"""
Q1
Students :
st_id int primary key,
st_name varchar(25) not null,
phone int(10) not null,
zone_no int not null

Stall:
sl_id int primary key,
sl_name varchar(25) not null,
zone_no int not null

MenuItem :
mn_id int primary key,
mn_name varchar(35) not null,
nm_price decima(8,2) not null,
stall_id int,
FOREIGN KEY(stall_id)
REFERENCES Stall(stall_id)

Order :
ord_id int primary key,
stu_id int,
order_time DATETIME,
order_date Date,
payment_type varchar(20),
FOREIGN KEY(stu_id)
REFERENCES Student(st_id)

Order_item :
ord_item_id int primary key,
order_id int,
item_id int,
quantity int check(quantity >0),

FOREIGN KEY (order_id)
REFERENCES Order(ord_id),

FOREIGN KEY (item_id)
REFERENCES MenuItem(mn_id)


Runner :
runner_id INT PRIMARY KEY,
runner_name VARCHAR(50),
phone VARCHAR(15)

Delivery:
delivery_id INT PRIMARY KEY,
order_id INT,
runner_id INT,
pickup_time DATETIME,
delivery_time DATETIME,
status VARCHAR(20),

FOREIGN KEY(order_id)
REFERENCES Orders(order_id),

FOREIGN KEY(runner_id)
REFERENCES Runner(runner_id)


Queries :
we will use left join so no stall remain into consideration
SELECT stall_name,
       COALESCE(SUM(mi.price * oi.quantity), 0) AS revenue
FROM Stall s
LEFT JOIN MenuItem mi
    ON s.stall_id = mi.stall_id
LEFT JOIN OrderItem oi
    ON mi.item_id = oi.item_id
LEFT JOIN Orders o
    ON oi.order_id = o.order_id
GROUP BY s.stall_name
ORDER BY revenue DESC
FETCH FIRST 3 ROWS ONLY;
OR
SELECT *
FROM (
    SELECT stall_name,
           COALESCE(SUM(mi.price * oi.quantity), 0) AS revenue
    FROM Stall s
    LEFT JOIN MenuItem mi
        ON s.stall_id = mi.stall_id
    LEFT JOIN OrderItem oi
        ON mi.item_id = oi.item_id
    LEFT JOIN Orders o
        ON oi.order_id = o.order_id
    GROUP BY stall_name
    ORDER BY revenue DESC
)
WHERE ROWNUM <= 3;

"""
import json
class Order:
    def __init__(self,order_id,payment_type):
        self.order_id=order_id
        self.payment_type=payment_type
        
    def to_dict(self):
        return {
            "order_id":self.order_id,
            "payment_type":self.payment_type
        }

class OrderQueue :
    def __init__(self):
        self.Priority=[]
        self.Normal=[]
    
    def enqueue(self,order):
        if order.payment_type =="PRE-PAID":
            self.Priority.append(order)
        else:
            self.Normal.append(order)
            
    def dequeue(self):
        if self.Priority:
            return self.Priority.pop(0)
        elif self.Normal:
            return self.Normal.pop(0)
        
        return None
            
        # Save queue
    def snapshot(self, filepath):

        data = []

        for order in self.Priority:
            data.append(order.to_dict())
        print(data)
        for order in self.Normal:
            data.append(order.to_dict())
        print(data)

        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
            
            
# queue = OrderQueue()

# queue.enqueue(Order(101, "CASH"))
# queue.enqueue(Order(102, "PRE-PAID"))
# queue.enqueue(Order(103, "PRE-PAID"))
# queue.enqueue(Order(104, "CASH"))

# print(queue.dequeue().order_id)
# print(queue.dequeue().order_id)
# print(queue.dequeue().order_id)

"""
Model the 30-zone festival map as a weighted graph. Name and outline the algorithm that finds the fastest route from stall zone to customer zone, state its complexity with a binary heap, and explain in two lines how your system should react when an event temporarily closes a path (edge deletion — recompute vs. precompute trade-off).

Since a runner can usually travel in both directions, this is an undirected weighted graph.

Use Dijkstra's Algorithm.

Why?
It finds the shortest (fastest) path from one source to all other vertices.
All path lengths (weights) are positive, so Dijkstra is the correct choice.
Steps of Dijkstra's Algorithm
Assign distance 0 to the source (stall zone).
Assign ∞ (infinity) to all other zones.
Insert the source into a min-priority queue (binary heap).
Repeatedly remove the vertex with the smallest distance.
Update (relax) the distances of its neighboring zones if a shorter path is found.
Continue until the destination (customer zone) is reached or all reachable zones are processed.


Time Complexity

Using a Binary Heap:

Time Complexity: 
O((V+E)logV)

where:

V = Number of zones
E = Number of paths

The binary heap efficiently retrieves the next closest zone.


Temporary Path Closure

Suppose this path is closed:

Zone A -----X----- Zone B

The graph changes because one edge is removed.

What should the system do?

Remove the corresponding edge from the graph and run Dijkstra's Algorithm again to compute a new shortest route.

Why not precompute all routes?
Recompute: Suitable when path closures are rare. It always provides the latest shortest path.
Precompute: Faster for answering queries, but every path closure requires updating many stored routes, making maintenance expensive.

Since the festival has only 30 zones, recomputing with Dijkstra is fast and practical.
"""
import pandas as pd
df=pd.DataFrame([6, 7, 5, 9, 6, 22, 7, 8, 6, 7])
mean_df=df.mean()
print(mean_df)

print(df.std())

print(df.median())
"""
The 22-minute delivery is an outlier caused by a temporary path closure. It pulls the mean upward, while the median (7 minutes) better represents the typical delivery time. Therefore, the sponsor claim should mention the exceptional delay rather than ignore it.


Probability That None of 20 Deliveries Is Late

Probability that a delivery is late:

P(Late)=0.05

Probability that a delivery is not late:

P(Not Late)=1−0.05=0.95

For 20 independent deliveries,

P(None Late)=(0.95)
20
(0.95)
20
≈0.3585
or
35.85%
"""


