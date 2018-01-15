print("Let's practice everything.")
print('You\'d need to know \'bout excapes with \\ that do \n newlines and\ttabs')

poem="""
\t the lovely world
with logical so firmly plantted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requries a explanation
\n\t where is none
"""

print("----------------")
print(poem)
print("----------------")

five=10-2+3-6
print(("This should be five:%d" %five))

def secrect_formula(started):
    jelly_beand=started*500
    jars=jelly_beand/1000
    crates=jars/100
    return jelly_beand,jars,crates

start_point=10000
beans,jars,crates=secrect_formula(start_point)

print(("With a starting point of:%d" %start_point))
print(("We'd have %d beans,%d jars and %d crates" %(beans,jars,crates)))
start_point=start_point/10
print("We can also do that this way")
print(("We'd have %d beans,%d jars and %d crates" %secrect_formula(start_point)))

