from sys import argv
script,user_name=argv
prompt=">"

print ("hi %s,I am the %s script." %(user_name,script))
print ("I'd like to ask your some question.")
print ("Do you like me %s"% user_name)
likes=input(prompt)

print ("Where do you live?")
live=input(prompt)

print ("What kind of computer do you have?")
computer=input(prompt)

print ("""
Allright,so you said %r about like me.
You live in %r.Not sure where that is.
And you have a %r computer.Nice.
""" %(likes,live,computer))