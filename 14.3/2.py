import random
print ()
print ("This prints random numbers between ?? and ??:")
for i in range(10):
    x = 10 * random.random() - 5 # between ?? and ??
    print (x)

# The general form of the equation above is:
# y = range * random.random() + lowest value

# For example, if you want to generate numbers between 90 and 100, the range is 10 (since 100-90)
# and the lowest value is 90, so:
# y = 10*random.random() + 90

# This is very similar in form to a familiar math formula for linear equations:
# y = mx + b
# where b is the initial value and m is the slope.