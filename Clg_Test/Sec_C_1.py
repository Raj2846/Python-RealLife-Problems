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
            
            
queue = OrderQueue()

queue.enqueue(Order(101, "CASH"))
queue.enqueue(Order(102, "PRE-PAID"))
queue.enqueue(Order(103, "PRE-PAID"))
queue.enqueue(Order(104, "CASH"))

print(queue.dequeue().order_id)
print(queue.dequeue().order_id)
print(queue.dequeue().order_id)