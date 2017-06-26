max_height = 0
max_height = int(raw_input("How high do you want it?"))

height = 0
while height < max_height:
    height = height + 1
    
    width = 0
    
    row = ""
    while width < max_height:
        row = row + "*"
        width = width + 1
        
    print row
    
print "done!"