"""
CricketIQ   CricketIQ is a startup founded by 3 MCA students from LJU, currently incubated at iHub Gujarat. They have built an IPL match outcome predictor. Their database stores historical IPL data (2008–2026): 900+ matches, 10,000+ player innings, 200,000+ ball-by-ball records. They are preparing for Demo Day where they must present a live prediction for an upcoming Mumbai Indians vs Chennai Super Kings match at Wankhede Stadium.  KEY DATA: In 18 years of IPL, MI has won 58% of matches at Wankhede. CSK has won 42% of their away matches. In day matches, the team batting first wins 55% of the time. Today's match is a day match and MI is batting first

1.
Probability that MI wins using only the venue statistic
Given:
MI wins 58% of matches at Wankhede.
Therefore,
P(MI wins)=
100
58
=0.58
or
58%

Probability that CSK wins as the away team
Given:
CSK wins 42% of their away matches.
Therefore,
P(CSK wins)=
100
42
=0.42
or
42%

Do they add up to 1?
0.58+0.42=1.00

Yes,

0.58+0.42=1
However, this is only a coincidence.

Explanation

These two probabilities come from different datasets:

58% is MI's historical win rate at Wankhede.
42% is CSK's historical away win rate across all away grounds.

They are not complementary probabilities from the same sample space.

Therefore, they do not necessarily have to add up to 1. In this particular question, they do because the given percentages happen to sum to 100%.


The model combines three probabilities:

Home advantage = 58%
Batting first advantage = 55%
Head-to-head = 52%

Using a simple average:

58+55+52/3= 165/3 =55
Therefore,
P(MI wins)=55.00%
or
0.55

Sum:

∑(x−
x
ˉ
)
2
=976.40
Sample Standard Deviation

Variance:

s^2=976.40/10−1 = 976.40/ 9 =108.49
Standard deviation:
s= underroot (108.49)
≈10.42
Sample Standard Deviation≈10.42 runs


Empirical Probability that MI wins by more than 15 runs
Margins greater than 15:
22, 31, 17
Number of favorable outcomes: 3

Total matches: 10
P(margin>15)=3/10
=0.3
P=0.3=30%


Probability MI wins all 3 matches

From the sample:

MI wins whenever the margin is positive.

Winning matches:

14, 5, 22, 8, 31, 17, 9

MI won:

7 out of 10

Historical win probability:

P(MI wins)= 7/10 =0.7

Assuming the next 3 matches are independent,

P(wins all 3)=(0.7)^3
=0.343
P=0.343=34.3%

"""



