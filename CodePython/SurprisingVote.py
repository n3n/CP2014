import math
score = input()
top_score = input()
score_O = abs(score-top_score-top_score-top_score)
if score_O > 2 and top_score > 2:
    print 'surprising'
else:
    print 'not surprising'
