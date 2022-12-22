import random
print ("The weather radar reports that ", end = "")
f = random.randint(1,3)

if f == 1:
    print("Today will be below freezing with overcast weather.")

elif f == 2:
    print("Today will be above 0 with rainy weather.")

else:
    print("Today will be around 35 with sunny weather.")