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

"""
The Knight's Journey   In chess, a Knight moves in an 'L' shape — 2 squares in one direction and 1 square perpendicular (or vice versa). On a standard 8×8 board, given the Knight's current position as (row, col), it can have up to 8 possible next moves. A Computer Science student is asked in a technical interview: 'Given a Knight at position (3,3) on a 4×4 board, use recursion to find all positions the Knight can reach in exactly 2 moves.'

(a) List all 8 possible move offsets for a Knight as (row_delta, col_delta) pairs. (b) Write a recursive Python function knight_moves(row, col, steps, board_size) that prints all valid positions the knight can reach in exactly 'steps' moves — validate board boundaries. (c) Trace the recursion for knight_moves(3, 3, 2, 4) — show the recursion tree for the first 2 branches only. What is the maximum number of leaf nodes in the full recursion tree and why?


#{(1,2),(2,1),(1,4),(4,1)}
this are the posibilities

Question to ask for recursion:
What does one function call represent?
What is the smallest problem? (Base case)
How can I reduce the problem? (Usually n-1, steps-1, index+1, etc.)
What are my choices? (Loop through all possibilities.)
When do I stop?
"""

moves = [
    (-2,-1),
    (-2,1),

    (-1,-2),
    (-1,2),

    (1,-2),
    (1,2),

    (2,-1),
    (2,1)
]

def knight_move(row,col,steps,board_size):
    
    #base condition
    if steps==0:
        print(row,col)
        return
    
    for dr,dc in moves:
        new_row = row + dr
        new_col = col + dc
        
        #checking wether the new row and column are on the board size or not    
        if 1 <= new_row <= board_size and 1 <= new_col <= board_size:
            knight_move(new_row,new_col,steps-1,board_size)
            
# knight_move(3,3,2,4)

