"""
🏏 IPL CRICKET — Dream11 Team Builder   You are building a mini Dream11-style app for the IPL. Every Player has a name, team, role (Batsman/Bowler/All-rounder/Wicketkeeper), credits (float), and points_scored (int). A Captain earns 2× points and a Vice-Captain earns 1.5× points. The app must also track how many total players have been added across all teams in the fantasy league.

Design a Python Player class and a Captain subclass to model the above. Include: a constructor for Player with all attributes, a method get_fantasy_points() that returns points_scored, override this method in Captain to return 2× points, a class variable total_players that increments with each object created, and a __str__ method that prints: 'Rohit Sharma (MI) — Batsman — 9.5 credits'. Write driver code creating 2 players and 1 captain, print their fantasy points
"""
class Player:
    total_players=0
    def __init__(self,name,team,role,credits:float,point_scored:int):
        self.name=name
        self.team=team
        self.role=role
        self.credits=credits
        self.point_scored=point_scored
        Player.total_players+=1
        
    def get_fantasy_points(self):
        return self.point_scored
        
        
class Captain(Player):
    def __init__(self,name,team,role,credits:float,point_scored:int):
        super().__init__(name,team,role,credits,point_scored)
        
    def get_fantasy_points(self):
        return ((super().get_fantasy_points())*2)
    
    def __str__(self):
        return f"{self.name} ({self.team}) - {self.role} - {self.credits} credits"
    
    
p1 = Player("Rajkumar","Gujarat","Captain",6.5,20)
p2 = Player("Raj","RCB","Bowler",6.0,10)
c1 = Captain("Rohit Sharma","MI","Batsman",9.5,20)

print(p1)
print(p2)
print(c1)

print(p1.get_fantasy_points())
print(p2.get_fantasy_points())
print(c1.get_fantasy_points())

print(Player.total_players)