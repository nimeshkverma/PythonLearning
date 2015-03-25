from sys import argv
script, filename = argv

print "We are going to erase %r" % filename
print "If you dont want Hit CTRL-C (^C)"
print "Else press Return"

raw_input("?")

print "Opening File..."
target = open(filename, 'w')
print "truncating the file"
target.truncate()

print "Now give 3 lines"

line1 = raw_input("line1")
line2 = raw_input("line2")
line3 = raw_input("line3")

print "I'm going to write these files to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Closing"
target.close()