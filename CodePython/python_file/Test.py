import urllib, urllib2, cookielib

username = raw_input('Username :')
password = raw_input('Password :')

def login_HTS():
	cj = cookielib.CookieJar()
	login_data = urllib.urlencode({'username':'lessibly','password':'FallEnGoiop1@#','submit':'Login'})
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	op = opener.open('https://www.hackthissite.org/',login_data)
	for i in op:
		print i.strip()
	
	
#~ def solving(cj):
	#~ opener = urllib2.build_opener(cookielib.CookieJar.add_header_cookie(cj))
	#~ opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	#~ a = opener.open('https://www.hackthissite.org/missions/prog/1/')
	#~ for i in b:
		#~ print i.strip()

login_HTS()
