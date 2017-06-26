coins = 0

print "You have %d coins" % (coins,)

answer = raw_input("do you want another?")

while answer == "yes":
    coins = coins + 1
    print "You have %d coins" % (coins,)
    answer = raw_input("another?")
print "Bye"