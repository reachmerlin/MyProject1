x = "There are %d types of people." % 10 # string into string 1
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # string into string 2
print x
print y
print "I said: %r." % x # string into string 3
print "I also said: '%s'." % y # string into string 4
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" 
print joke_evaluation % hilarious # string into string 5
w = "This is the left side of..."
e = "a string with a right side."
print w + e
