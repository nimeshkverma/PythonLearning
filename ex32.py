the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears', 'apricots']
change = [1,'pennies',2,3,2,'yellow',7]

for num in the_count:
	print "This is the count %d" % num

for fruit in fruits:
	print "A fruit of type: %s" % fruit

for i in change:
	print "I have got %r" %i

ele = []
ele + range(11,20)
for i in range(1,10):
	ele.append(i)

for x in xrange(1,10):
	print "xrange %d" %x
	print "ele %d" %ele[x-1]
