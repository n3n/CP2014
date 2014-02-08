message = open("../wordlist.txt")
string = "fracne"
word = "hello"
cnt = 0
for i in string:
	for j in message:
		#print "J: "
		for k in j:
			#print "K: "
			if i in j and k in string:
				cnt += 1
				if cnt == len(word):
					print "Was found! : " + j
					break
print "not found"
