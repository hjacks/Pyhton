# 习题19：函数和变量

def cheese_and_crackers(chesse_count,boxes_of_crackers):
    print(("you have %d cheeses!" % chesse_count))
    print(("you have %d boxes of crackers!" % boxes_of_crackers))
    print("Man,that's enough for a party")
    print("Get a blanket.\n")

print("We can just give the functions numbers directly!")
cheese_and_crackers(20,30)

print("Or,we can use variables for our scripts:")
amount_of_cheese=40
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)
print("We can even do math inside too:")
cheese_and_crackers(10+19,30+44)
print("We can combine the two,variables and math:")
cheese_and_crackers(amount_of_cheese+1222,amount_of_crackers+888)
