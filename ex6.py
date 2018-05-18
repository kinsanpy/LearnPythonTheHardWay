x = "There are %d types of people." % 10 # define formatted strings
binary = "binary" # define strings
do_not = "don't" # define strings
y = "Those who know %s and thos who %s." % (binary, do_not) # define formatted strings

print x
print y

print "I said: %r." % x # print formatted strings with strings inside
print "I also said: '%s'." % y # same as above

hilarious = False # define a boolean value
joke_evaluation = "Isn't that joke so funny?! %r"# formatted strings can be a boolean value

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
print w + e # "+" can also link things together
