i = 0
numbers = []

while i<6:
	print "At the top i is %d" %i
	numbers.append(i)

	i += 1
	print "Numbers Now: ", numbers
	print "At the bottom i is %d" %i

	print "---------------------------"

print numbers
for num in numbers:
	print "*****************"
	print num

def print_times(times):
	n = []
	i=1
	while i<times:
		n.append(i)
		print n
		i+= i

inp = raw_input("Give the number >>>" )
print_times(int(inp))