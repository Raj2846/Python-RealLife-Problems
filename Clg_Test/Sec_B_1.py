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
    

order1 = Order()
order1.add_item(Food("Paneer Tikka",500,True))
order1.add_item(Beverage("Coffee",150))

order2 = Order()
order2.add_item(Food("Pizza",1800))
order2.add_item(Beverage("Juice",300))

orders = [order1, order2]

save_day(orders,"orders.json")

loaded = load_day("orders.json")

for order in loaded:
    print("Bill =",order.bill_total())
    
    
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
