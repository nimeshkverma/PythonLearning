print "Let's practise  everything."
print "You \'d need to know \'bout escapes with \\  that do \n newlines and \t\t"

poem = """
\t The lovely world
bhasdbcd
bhcjsDVc
zjgc zx
\n\t kjbedfklvdf
"""

print "-----------------"
print poem
print "-----------------"

five = 10-2+3-6

print "This should be five %s " % five

def sec_for(started):
	j = started*500
	ja = j/1000
	c = ja/100
	return j,ja,c

sp = 10000
b,j,c = sec_for(sp)

print "With starting point of %d" % sp
print "We will have %d beans, %d jars, and %d crates" % sec_for(sp)
