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
    
    
# p1 = Player("Rajkumar","Gujarat","Captain",6.5,20)
# p2 = Player("Raj","RCB","Bowler",6.0,10)
# c1 = Captain("Rohit Sharma","MI","Batsman",9.5,20)

# print(p1)
# print(p2)
# print(c1)

# print(p1.get_fantasy_points())
# print(p2.get_fantasy_points())
# print(c1.get_fantasy_points())

# print(Player.total_players)


"""
⚽ FIFA WORLD CUP 2026 — Golden Boot Analytics   The FIFA 2026 analytics database has a table: GOALS(goal_id, player_name, country, match_id, minute_scored, goal_type ['Open Play'/'Penalty'/'Free Kick'/'Own Goal']). Tournament organizers need to find the Golden Boot winner (most goals, excluding own goals) and identify which country scores the most goals in the second half (minute > 45).

Write SQL queries for: (a) Find the Golden Boot winner — the player with the most goals excluding 'Own Goal' type. Handle ties by also showing the player with fewer penalty goals as the tiebreaker. (b) Find the country that scored the most goals in the second half (minute_scored > 45), excluding own goals. (c) Using a window function, rank all players by goal count within their country — so we can see the top scorer per country.


a.
select player_name,count(goal_type) as total_goals ,
sum(
    case
    when goal_type = "penalty" then 1
    else 0
    END
) as penalty_goal 
from GOALS where goal_type <> "Own Goal" group by player_name order by total_goals DESC, penalty_goal ASC
FETCH FIRST 1 ROW ONLY
;

b.
select country,count(goal_type) as total_goal from GOALS
where goal_type <> "Own Goal" and minute_scored > 45 group by country Order by total_goal DESC
FETCH FIRST 1 ROW ONLY;

OR

select * from (
select country,count(goal_type) as total_goal from GOALS
where goal_type <> "Own Goal" and minute_scored > 45 group by country Order by total_goal DESC )
where ROWNUM=1;

c.
select player_name,country,count(goal_type) as total_goal from GOALS
group by country,player_name Order by total_goal DESC;

or
difference is that question ask for showing ranking so we need to use rank() from windows function 
SELECT
    player_name,
    country,
    COUNT(*) AS total_goals,
    RANK() OVER (
        PARTITION BY country
        ORDER BY COUNT(*) DESC
    ) AS player_rank
FROM GOALS
WHERE goal_type <> 'Own Goal'
GROUP BY player_name, country;
"""


