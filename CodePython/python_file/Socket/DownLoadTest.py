import urllib2, time
a = urllib2.urlopen("http://vmg.pp.ua/books/%D0%9A%D0%BE%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D1%8B%D0%98%D1%81%D0%B5%D1%82%D0%B8/hack/engl/security/")
print "a.code =",a.code
print "info =",a.info()
#html = a.read()
#print len(html)
for line in a:
    print line.rstrip()
    
