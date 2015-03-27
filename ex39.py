states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'

}

cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
}

cities['NY'] = "New York"
cities["OR"] = 'Portland'

print ' -'*25
print "NY State has: ",cities['NY']
print "OR State has: ",cities['OR']

print ' -'*25
print "Michi abbr ", states['Michigan']
print "Florida abbr ", states['Florida']

print ' -'*25
print "Michigan has ",cities[states['Michigan']]
print "Florida has ", cities[states['Florida']]

print ' -'*25
for state, ab in states.items():
	print "%s is abb as %s" %(state,ab)

print ' -'*25
for ab,city in cities.items():
	print "%s has city %s" %(ab,city)

print ' -'*25
for st,ab in states.items():
	print "%s state is abb %s and has city %s" %(st,ab,cities[ab])

print ' -'*25
state = states.get('Texas')
if not state:
	print "Sorry"

city = cities.get('TX', 'Do Not Exists')

print "The city for the state 'TX' is: %s" %city
