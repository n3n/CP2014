cryptmessage = raw_input()
char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
compare = ['the','be','to','of','and','in','that','have','it','for','not','on','with','he','as','you','do','at','this','but','his','by','from','they','we','say','her','she','or','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','go','me','when','make','can','like','time','no','just','him','know','take','people','into','year','your','good','some','could','them','see','other','than','then','now','look','only','come','its','over','think','also','back','after','use','two','how','our','work','first','well','way','even','new','want','because','any','these','give','day','most','us','time','person','year','way','day','thing','man','world','life','hand','part','child','eye','woman','place','work','week','case','point','government','company','number','group','problem','fact','be','have','do','say','get','make','go','know','take','see','come','think','look','want','give','use','find','tell','ask','work','seem','feel','try','leave','call','good','new','first','last','long','great','little','own','other','old','right','big','high','different','small','large','next','early','young','important','few','public','bad','same','able','to','of','in','for','on','with','at','by','from','up','about','into','over','after','beneath','under','above','the','and','a','that','I','it','not','he','as','you','this','but','his','they','her','she','or','an','will','my','one','all','would','there','their']
# compare = ['this','the','was','were','am','who','where','what','when','why','lazy','cat','dog','man','kmitl','shana','user','data','logic','host','lorem','ipsum','not','raw','imput','caesar','username','password','kafra','server','python','grader','rapter','mix5003','isirbank','host','vps','hack','case','output','time','list','dict','tuple','array','sheet','work','ing','ed','er','es','than','ies','more','less','flow','think','correct','in','out','re','result','folder','file','quick','fox','brown','red','blue','green','yellow','gold','dark','black','pink','facebook','shit','fuck','god','damn','judge','youtube','google','yahoo','chrome','firefox','safari','explorer','ubuntu','centos','window','find','replace','split','append','submission','text','raw','code','junk','php','dork','name','surname','win','lose','suck','dummy','stand','walk','run','fly','dig','swam','load','bit','wifi','lan','like','share','love','program','self','parent','construct','for','loop','while','int','str','agi','dex','luk','vit','neko','chotipat','pornavalai','brute','force','sublime','out','is','am','are','he','she','it','you','we','us','login','logout','psit','pre','search']
match = {}
for brute in xrange(27):
	message = ''
	shift = brute
	for let in cryptmessage:
		up = False
		if let.isupper():
			up = True
			let = let.lower()
		if let in char:
			if up == True:
				message += char[(char.index(let) - shift) % 26].upper()
			else:
				message += char[(char.index(let) - shift) % 26]
		else:
			message += let
	for com in compare:
		if com in message.lower():
			match[message] = 0
for msg in match:
	level = 0
	for com in compare:
		if com in msg:
			level += msg.count(com)
	match[msg] = level
val = match.values()
val.sort()
for msg in match:
	if match[msg] == val[-1]:
		print msg