print "Let's say hi to everyone five times"
for n in range(5):   # this is a comment!
  print "Hello world! (x%i)" % (n+1)
from decimal import Decimal
from random import randint
print "Here's a random decimal number " + \
  "between 0 and 100 with resolution up " + \
  "to 1/100:"
print Decimal(randint(0, 10000)) / Decimal(100)