l1 = raw_input()
l2 = raw_input()
l3 = raw_input()

# ตรงนี้ใครจะรับ input เก็บท่าไหนก็ได้ตามสบายแล้วแต่ชอบ
ox = [ list(l1), list(l2), list(l3) ]

# ข้อนี้เราต้องจิ้นให้ได้ก่อนว่าถ้าเราเล่น OX เราจะชนะได้แบบไหนมั่ง (จิ้นๆไปเหอะตารางเท่าขี้มด 3x3 เอง)
# เราจะจิ้นได้ว่ามันจะมี 4 case และอีก case ที่เสมอ

# case |
if ox[0][0] == ox[1][0] == ox[2][0]:
	print ox[0][0] + ' |'
elif ox[0][1] == ox[1][1] == ox[2][1]:
	print ox[0][1] + ' |'
elif ox[0][2] == ox[1][2] == ox[2][2]:
	print ox[0][2] + ' |'
# case -	
elif ox[0][0] == ox[0][1] == ox[0][2]:
	print ox[0][0] + ' -'
elif ox[1][0] == ox[1][1] == ox[1][2]:
	print ox[1][0] + ' -'
elif ox[2][0] == ox[2][1] == ox[2][2]:
	print ox[2][0] + ' -'
# case \\\\\\\\\\\\\\\\
# ตรงนี้ระวังนิดนึง Python มันมอง \\ เป็น \ ทำให้เราต้องเบิ้ล \ เป็น 2 เท่าของโจทย์ (มันคือเรื่อง escape char พวก \n \t บลาๆ)
elif ox[0][0] == ox[1][1] == ox[2][2]:
	print ox[0][0] + ' \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'
# case /
elif ox[0][2] == ox[1][1] == ox[2][0]:
	print ox[0][2] + ' /'
# other case
else:
	print 'Draw'