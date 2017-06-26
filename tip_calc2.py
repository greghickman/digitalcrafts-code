totalbill = int(raw_input("Total Bill Amount?"))
level = raw_input("Level of Service?")
people = int(raw_input("Split how many ways?"))
tip = 0
if level == "good":
    tip = totalbill * .20
    
elif level == "fair":
    tip = totalbill * .15
    
elif level == "bad":
    tip = totalbill * .10
    
print "Tip Amount: $%.2f" %(tip)
print "Total Amount: $%.2f" %(totalbill + tip)
print "Amount per Person: $%.2f" %(tip / people)