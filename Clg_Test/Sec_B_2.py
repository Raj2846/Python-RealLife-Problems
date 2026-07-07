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


# ipl_df = load_ipl(r"ipl_2026.csv")
# print(ipl_df.head())


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
                    
def dfs(graph, node, visited):

    if node in visited:
        return

    print(node)

    visited.add(node)

    for neighbour in graph[node]:
        dfs(graph, neighbour, visited)
# visited = set()
# dfs(graph, start_node, visited)

"""
🤼 PRO KABADDI + IPL — CROSS-SPORT PERFORMANCE MATRIX   SportzIQ is an Ahmedabad-based sports analytics startup (incubated at iHub Gujarat) that tracks athlete performance across 3 metrics: Attack Score, Defense Score, and Fitness Score — each on a scale of 0–10. They track 3 athletes across Kabaddi (Sachin, Pardeep, Pawan) and use a Weight Matrix to compute an Overall Performance Index for selection.
"""
# import numpy as np


# T = np.array([[8, 7, 9], [9, 6, 8], [7, 9, 7]])
# W = np.array([0.4, 0.35, 0.25]) 
# s = [[8, 7, 9], [9, 6, 8], [7, 9, 7]]
# p = [0.4, 0.35, 0.25]

# r=[((s[0][0]*p[0])+(s[0][1]*p[1])+(s[0][2]*p[2])),
#    ((s[1][0]*p[0])+(s[1][1]*p[1])+(s[1][2]*p[2])),
#    ((s[2][0]*p[0])+(s[2][1]*p[1])+(s[2][2]*p[2]))
#    ]

# print(r)

# p_norm=[]
# for i in s:
#     temp=[]
#     for j in i:
#         j=round(j/9,2)
#         temp.append(j)
#     p_norm.append(temp)
    
# print(p_norm)

# new_r=[((p_norm[0][0]*p[0])+(p_norm[0][1]*p[1])+(p_norm[0][2]*p[2])),
#    ((p_norm[1][0]*p[0])+(p_norm[1][1]*p[1])+(p_norm[1][2]*p[2])),
#    ((p_norm[2][0]*p[0])+(p_norm[2][1]*p[1])+(p_norm[2][2]*p[2]))
#    ]
# print(new_r)

"""
Sequence is a board game where players play cards from their hand to place chips on the corresponding squares on the board. A digital version is being built by MCA students. The board has 100 squares (10×10 grid) each with a card value. Players have a hand of 7 cards and need to find which board squares match their cards as quickly as possible. The game engine must also detect if any player has completed a 'Sequence' (5 chips in a row — horizontal, vertical, or diagonal).
"""

board = [
    12, 5, 7, 19, 25, 7, 34, 41, 2, 18,
    9, 27, 14, 7, 33, 45, 10, 22, 7, 50,
    3, 16, 29, 11, 7, 36, 48, 8, 20, 31,
    15, 24, 39, 7, 52, 6, 13, 30, 7, 44,
    21, 4, 17, 26, 35, 7, 40, 49, 23, 32,
    1, 28, 38, 7, 46, 51, 18, 5, 7, 12,
    34, 43, 16, 7, 25, 37, 47, 9, 14, 7,
    20, 33, 11, 24, 36, 50, 2, 7, 29, 42,
    8, 15, 27, 39, 7, 45, 19, 31, 52, 13,
    6, 17, 30, 7, 40, 48, 21, 35, 10, 7
]

inx=[]
def linear_search(board):
    for i in range(len(board)):
        if board[i]==7:
            inx.append(i)
    print(inx)
        
# linear_search(board)

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
            print(lst)
            # this will add the remaining list from i
            while i< len(left):
                lst[k]=left[i]
                i+=1
                k+=1 
            print(lst)

            while j<len(right):
                lst[k]=right[j]
                j+=1
                k+=1
            print(lst)

# print(board)

# sorting_method(board)
def binary_search_first(board, start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if board[mid] == target:
        # Check if this is the first occurrence
        if mid == 0 or board[mid - 1] != target:
            return mid
        # Otherwise, search on the left
        return binary_search_first(board, start, mid - 1, target)

    elif board[mid] < target:
        return binary_search_first(board, mid + 1, end, target)
    else:
        return binary_search_first(board, start, mid - 1, target)
    
# ans = binary_search_first(board, 0, len(board)-1, 7)

# if ans != -1:
#     print("First occurrence of 7 is at index:", ans)
# else:
#     print("Card not found")
    
lst=[45, 72, 38, 72, 91, 55]    
sorting_method(lst)
print(lst)



def check_horizontal_seq(board,player):
    row=len(board)
    col=len(board[0])
    
    for i in range(row):
        count=0
        for j in range(col):
            if board[i][j] == player:
                count+=1
                
                if count==5:
                    return True
            else:
                count=0
    return False

def check_vertical_seq(board,player):
    row=len(board) #10 as the list contain 10 rows
    col=len(board[0]) # 10 as the element in the sub list are 10
    
    for i in range(col):
        count=0
        for j in range(row):
            if board[i][j] == player:
                count+=1
                
                if count==5:
                    return True
            else:
                count=0
    return False