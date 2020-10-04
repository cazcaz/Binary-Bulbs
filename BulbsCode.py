#Drivers in Blender in their most simple form are a single line of Python code
#The Python code only allows basic math functions in the single line
#Want the bulbs to last 20 frames each

#The fucntion takes the frame and the position, and returns 1 or 0 depending on whether the bulb is on or not

# Pos 0 : _ _ _ _ _ _ _ _
# Pos 1 :  __ __ __ __ __   
# Pos 2 :    ____    ____
# Pos 3 :        ________

#Each position represents that power of 2 (2^pos)

from math import floor, sin, pi

def BulbOn(f, n):
    return floor(sin(pi/(2**n)*(f/20 - 2**n))) + 1

#Testing

for i in range(320):
    print(str(BulbOn(i, 3)) + str(BulbOn(i, 2)) + str(BulbOn(i, 1)) + str(BulbOn(i, 0)))

#The result contains 2s, but this is not a problem as the result of BulbOn is a multiplier for the intensity of the light in blender