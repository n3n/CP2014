import sys
import itertools
import time
choices = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
start_Time = time.time()
for length in xrange(4,20):
   for entry in itertools.product(choices,repeat = length):
      password = ''.join(entry)
      print password
      if password == 'admin123':
         print 'I win'
         print "Time :",time.time() - start_Time
         sys.exit(0)
