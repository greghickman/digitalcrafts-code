# totalbill = int(raw_input("Total Bill Amount?"))
# level = raw_input("Level of Service?")
# tip = 0
# if level == "good":
#     tip = totalbill * .20
    
# elif level == "fair":
#     tip = totalbill * .15
    
# elif level == "bad":
#     tip = totalbill * .10
    
# print "Tip Amount: %.2f" % (tip)
# print "Total Amount: %.2f" %(totalbill + tip)

def get_total_bill_from_user():
    return int(raw_input("Total Bill Amount?"))


def calc_tip(amount1):
    level = raw_input("Level of Service?")
    tip = 0
    if level == "good":
        tip = amount1 * .20
        
    elif level == "fair":
        tip = amount1 * .15
        
    elif level == "bad":
        tip = amount1 * .10

    return tip

def main():
    amount = get_total_bill_from_user() 
    tip = calc_tip(amount)
    return amount + tip

# def main():
#     total = tip_amount()

    
print main()