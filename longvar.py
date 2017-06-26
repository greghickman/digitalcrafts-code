longvow = "Cheese"  #declaring variable that has word in it from example
savedvowel = ""  #declaring variable that is needed to check if vowels repeat and double going left to right
s = "" # at end to have variable to pass at end to print and be final longvow result ?
for vowel in longvow: # loop to run through all possible vowels and do most of work - for every vowel or letter even in no vowel run through this loop the variable longvow
    vowel = vowel.upper()  #change to uppercase on all to make sure it isn't lowercase or upper to do check not really necessary. thinking webform but carl and I kept it in
    if vowel == "A": # if first vowel then nested loop inside main loop above
        
        if savedvowel == vowel: # if second letter in longvow is equal to prior like in cheese with two e's then
            s = s + vowel*4 # s which is nothing becomes instead of nothing the same as vowel (uppercase) and then does it 5 times. four numbers and 0 counts as 1
        else: # or if not a vowel that repeats, just a normal vowel
            s = s + vowel # if not repeathing vowel then take nothing and just make it pass it though I think? since not repeating then pass it as normal vowel.?
        savedvowel = vowel #savedvowel1 becomes the thing to pass into loop again to start again but saving it to pass if it repeats?


    elif vowel == "E": # loop part to check for another vowel
        
        if savedvowel == vowel:
            s = s + vowel*4
        else:
            s = s + vowel
        savedvowel = vowel


    elif vowel == "I":
        
        if savedvowel == vowel:
            s = s + vowel*4  
        else:
            s = s + vowel
        savedvowel = vowel


    elif vowel == "O":
        
        if savedvowel == vowel:
            s = s + vowel*4
        else:
            s = s + vowel
        savedvowel = vowel


    elif vowel == "U":
        
        if savedvowel == vowel:
            s = s + vowel*4
        else:
            s = s + vowel 
        savedvowel = vowel # stops checking for vowels in whole loop


    else: # to make a loop handle no vowels at all if nothing found as it cycles through for statement
        s = s + vowel # pass variable to longvow make it do letter not vowel and continue to cycle and check and have something to print to s?
        savedvowel="" # save nothing if not repeating? NOT Sure why. I can't follow logic. I am trying.


print s # print out total output after running loops