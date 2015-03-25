def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese !" %cheese_count
	print "You have %d boxes of crackers" %boxes_of_crackers
	print "ok \n"

print "Giving function numbers directly"
cheese_and_crackers(20,30)

print "OR, we can use variables from our scripts:"
cheese_count = 10
boxes_of_crackers = 50

cheese_and_crackers(cheese_count,boxes_of_crackers)

print "We can even do the math inside too"
cheese_and_crackers(1000+2000,7+9)

print "combi of the two"
cheese_and_crackers(cheese_count+10101, boxes_of_crackers+11222)
