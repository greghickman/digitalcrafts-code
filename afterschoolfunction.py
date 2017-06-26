

def increase_coins(num):
    return num + 1
def ask_user():
    return raw_input("another?")

def print_coins(coins):
    print "You have %d coins" % (coins,)

def main():
    answer = "yes"
    coins = 0
    print_coins(coins)
    answer = ask_user()
    
    while answer == "yes":
        coins = increase_coins(coins)
        print_coins(coins)
        answer = ask_user()
    print "Bye"  

main()

