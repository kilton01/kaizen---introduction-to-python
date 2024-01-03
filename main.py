from mathlib import add, subtraction, multiplication, division
# from mathlib import *

a = 2
b = 3
c = 4
d = 5

# add up all variables
sum = add(a, b, c, d)

# subtract c and d from the result above
diff = subtraction(c, d, first_num=sum)

# multiple your new result by b
prod = multiplication(diff, b)

# divide your new results by a
quotient = division(prod, a)

print(f"{sum = }")
print(f"{diff = }")
print(f"{prod = }")
print(f"{quotient = }")
