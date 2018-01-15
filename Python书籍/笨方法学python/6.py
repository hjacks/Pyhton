x='They are %d types of people' % 10
binary="binary"
do_not="don't"
y="Those who knows %s and those who %s." %(binary,do_not)

print x
print y

print 'I said:%r.'%x
print "I also said:'%s'"% y

hilarious=False
joke_evolution="Isn't that joke funny?! %r"

print joke_evolution %hilarious

w="This is left side of..."
e="A string with a right side."

print w+e