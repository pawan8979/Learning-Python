# TYPECASTING

"""
a= "pawan"
b = 10

 print(a+b) Sorry! I give error please typecast me
"""

a = "17"
b = "5"
# Explicit Typecasting

print("Final Result:", int(a) + int(b))


Fa = 3.7
print("Float: ", type(Fa), "\n")

Ib = 5
print("int: ", type(Ib), "\n")

# Implicit Typecasting
Tc = Fa + Ib
print("Total:", type(Tc), "\n")

print("Final Result:", Tc)
