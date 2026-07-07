"""
Q6.
SYSTEM   BCCI's data team has a CSV file ipl_2026.csv with columns: match_id, team1, team2, venue, city, winner, player_of_match, team1_score, team2_score, season. An MCA intern is asked to build a Python analytics script on Day 1 of their internship. The script must clean the data, compute season statistics, and export a summary report — all before the evening press conference
"""
import pandas as pd
# file=input("Enter the file location :")
# filepath=f"r{file}"


def load_ipl(filepath):
    df = pd.read_csv(filepath)
    print(df.shape)

    df = df.dropna(subset=['winner'])
    # print(df)

    df['team1_score'] = pd.to_numeric(
        df['team1_score'], errors='coerce').fillna(0).astype(int)
    # print(df['team1_score'])

    df['team2_score'] = pd.to_numeric(
        df['team2_score'], errors='coerce').fillna(0).astype(int)
    # print(df['team2_score'])

    print(df.shape)

    return df


ipl_df = load_ipl(r"ipl_2026.csv")
print(ipl_df.head())


"""
Q7.
FIFA 2026 is hosted across USA, Canada, and Mexico — 48 teams, 104 matches, 1,200+ players. The tournament's IT team needs a normalized database to track: teams and their group assignments, players with their team and position, matches with venue, date, referee, and scores, and individual goal events per match.

1. TEAM
Attribute	Data Type	Constraint
team_id	INT	Primary Key
team_name	VARCHAR(50)	UNIQUE, NOT NULL
group_name	CHAR(1)	NOT NULL
coach	VARCHAR(50)	
fifa_rank	INT

2. PLAYER
Attribute	Data Type	Constraint
player_id	INT	Primary Key
player_name	VARCHAR(50)	NOT NULL
team_id	INT	Foreign Key → TEAM(team_id)
position	VARCHAR(20)	NOT NULL
jersey_no	INT	
age	INT

3. VENUE
Attribute	Data Type	Constraint
venue_id	INT	Primary Key
venue_name	VARCHAR(60)	NOT NULL
city	VARCHAR(50)	
country	VARCHAR(30)	
capacity	INT

4. MATCH
Attribute	Data Type	Constraint
match_id	INT	Primary Key
team1_id	INT	FK → TEAM(team_id)
team2_id	INT	FK → TEAM(team_id)
venue_id	INT	FK → VENUE(venue_id)
match_date	DATE	
referee	VARCHAR(50)	
team1_score	INT	
team2_score	INT

5. GOAL_EVENT
Attribute	Data Type	Constraint
goal_id	INT	Primary Key
match_id	INT	FK → MATCH(match_id)
player_id	INT	FK → PLAYER(player_id)
goal_minute	INT	
goal_type	VARCHAR(20)


1.
Difference exactly one goal.
SELECT *
FROM MATCHES
WHERE ABS(team1_score-team2_score)=1;

2.
SELECT
    p.player_name,
    t.country,
    COUNT(g.goal_id) AS total_goals

FROM PLAYER p

JOIN TEAM t
ON p.team_id=t.team_id

JOIN GOAL_EVENT g
ON p.player_id=g.player_id

GROUP BY
p.player_name,
t.country

HAVING COUNT(DISTINCT g.match_id)>2;

3.
SELECT *
FROM(

SELECT
v.venue_name,

COUNT(DISTINCT m.match_id) AS total_matches,

COUNT(g.goal_id) AS total_goals

FROM VENUE v

JOIN MATCHES m
ON v.venue_id=m.venue_id

LEFT JOIN GOAL_EVENT g
ON m.match_id=g.match_id

GROUP BY
v.venue_name

ORDER BY total_matches DESC

)
WHERE ROWNUM=1;

(i)
CREATE INDEX idx_player_name
ON PLAYER(player_name);
(ii)

A B-Tree index stores values in sorted order using a balanced tree structure. During a search, the database traverses the tree from the root to the appropriate leaf node instead of scanning every row. This reduces the search complexity from O(n) to approximately O(logn), making lookups much faster.

(iii)

Adding many indexes increases the cost of INSERT, UPDATE, and DELETE operations because every index must be updated whenever the table changes. It also increases storage requirements. Thus, indexes improve read performance but reduce write performance.
"""

"""
In a chess endgame, only a Bishop and the King remain on the board. A computer chess engine needs to map all squares the Bishop can attack from its current position — this is modeled as a graph problem where each board square is a node and diagonal moves are edges. The engine also needs to find the shortest path for the King to reach a target square, treating the board as an unweighted grid graph.
"""


def bfs():
    queue = [(1, 1)]
    visited = [(1, 1)]

    while queue:
        row, col = queue.pop(0)

        if (row, col) == (4, 4):
            print("Reched ")
            return
        moves = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 1), (1, 0), (1, -1)
        ]
        
        for dr,dc in moves:
            new_r=row+dr
            new_c=col+dc
            
            if 1<= new_r <=4 and 1<= new_c <=4:
                if (new_r,new_c) not in visited:
                    visited.append((new_r,new_c))
                    queue.append((new_r,new_c))
                    
