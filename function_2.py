# print "You have 0 coins."
# num_coins = 0
# answer = raw_input("Do you want another?")
# while answer == "yes":
#     num_coins = num_coins + 1
#     print "You have %s coins." % num_coins
#     answer = raw_input("Do you want another?")
    
#     if answer == "no": print "Bye"

print "You have 0 coins."
def choose_coins():
    return int(raw_input("Do you want another?"))

def addthem(final):
    num_coins = 0
    while choose_coins() == "yes":
        num_coins = num_coins + 1
        #print "You have %s coins." % num_coins
        answer = raw_input("Do you want another?")
        if answer == "no": print "Bye"

    return answer

def final():
