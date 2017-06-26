print "You have 0 coins."
num_coins = 0
answer = raw_input("Do you want another?")
while answer == "yes":
    num_coins = num_coins + 1
    print "You have %s coins." % num_coins
    answer = raw_input("Do you want another?")
    
    if answer == "no": print "Bye"


