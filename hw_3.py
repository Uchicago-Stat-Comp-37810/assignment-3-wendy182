# Name: Wenjing Xu
# hw3.py

import math
import random
#%%
# ********** Exercise 1 **********

# Define is_divisible function here
def is_divisible(m,n):
    if n ==0:
        return("The denominator should be non-zero." )
    else:
        if m % n == 0:
            return True
        else:
            return False

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print (is_divisible(10, 5))  # This should return True
print (is_divisible(18, 7))  # This should return False
print (is_divisible(42, 0))  # What should this return?

#%%
# ********** Exercise 2 **********

# Define not_equal function here
def not_equal(a,b):
    return False if a == b else True

# Test cases for not_equal
print(not_equal(3,2))
print(not_equal(3,3))
print(not_equal("three","two"))
print(not_equal("three","three"))
print(not_equal([1,2],[1,2]))
print(not_equal([],[]))

#%%
# ********** Exercise 3 **********

## 1 - multadd function
def multadd(a,b,c):
    return a*b+c

## 2 - Equations
angle_test = multadd(math.cos(math.pi/4), 0.5, math.sin(math.pi/4))
ceiling_test = multadd(math.log(12,7), 2, math.ceil(276/19))

# Test Cases
print ("sin(pi/4) + cos(pi/4)/2 is:")
print (angle_test)

print ("ceiling(276/19) + 2 log_7(12) is:")
print (ceiling_test)

#%%
# ********** Exercise 4 **********

## 1 - rand_divis_3 function
def rand_divis_3():
    rand = random.randint(0,100)
    return True if rand%3 ==0 else False

# Test Cases
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())
