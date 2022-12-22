# Random Other Things

# Sometimes you want random… other things. In that case you can use IF statements to convert from an
# integer to whatever you need. For example if your best friend to change randomly:

import random
print ("My best friend is ", end = "")
f = random.randint(1,3) # pick a number between 1 and 3
if f == 1:
    print ("Larry")
elif f == 2:
    print ("Mary")
else:
    print ("Gary")