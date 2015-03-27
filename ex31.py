print "Door 1 or Door 2 ??"
door = raw_input(">>> " )

if door == "1":
	print "1 or 2"

	bear = raw_input(">>> ")

	if bear == "1":
		print "1 and 1"
	elif bear == "2":
		print "1 and 2"
	else:
		"1 and %s " % bear

elif door == "2":
	print "1 or 2 or 3"
	i = raw_input(">>> ")
	if i == "1" or i == "2":
		print "1 or 2"
	else:
		print "3"
else:
	print "Bye Bye"

