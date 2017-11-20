states={
    "anhui":"AH",
    "henan":"HN",
    "shandong":"SD",
    "jiangsu":"JS",
    "zhejiang":"ZJ"
}
cities={
    "AH":"hefei",
    "JS":"hangzhou",
    "ZJ":"nanjing"
}

cities["HN"]="zhengzhou"
cities["SD"]="jinan"

print "-"*10
print "anhui state has :",cities["AH"]

print "-"*10
print "henan state has:",cities[states["henan"]]

print "-"*10
for state,abbrv in states.items():
    print "%s is abbreviated %s."%(state,abbrv)

print "-"*10
for abbrv,city in cities.items():
    print "%s has the city %s." %(abbrv,city)

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print "-"*10
state=states.get("beijing",None)
if not state:
    print "Sorry,no beijing"

print "-"*10
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
