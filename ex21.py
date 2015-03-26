def add(a,b):
	print "Sum of %d and %d" %(a,b)
	return a+b

def sub(a,b):
	print "Sub of %d and %d" %(a,b)
	return a-b

def mult(a,b):
	print "Mult of %d and %d" %(a,b)
	return a*b

def div(a,b):
	print "Div of %d and %d" %(a,b)
	return a/b

print "Just doing sum math functions"

age = add(30,5)
height = sub(78,4)
weight = mult(90,2)
iq = div(100,2)

print "age %d height %d weight %d, iq %d " % (age,height,weight,iq)

print "That becomes: ", add(age, sub(height,mult(weight,div(iq,2))))