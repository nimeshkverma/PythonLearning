from sys import argv
script, user_name = argv
prompt = "> "

print "Hi %s, I'm %s" %(user_name,script)
print "Few Questions"
print "Do you like me %s" %user_name
likes = raw_input(prompt)
print "Hey %s You live in" %user_name
lives = raw_input(prompt)
print "Which comp do you use"
comp = raw_input(prompt)

print '''
Alright, so you said %r about liking me.
You live in %r 
You have %r computer
''' % (likes,lives,comp)

