#Default Arguments

def average(a=9, b=5):
    print("a is:", a, "b is:", b)
    print("The avergae is:", (a+b)/2)

average()

def average(a=9, b=5):
    print("a is:", a, "b is:", b)
    print("The avergae is:", (a+b)/2)

average(10,2) #10,2 overrides 9,5

def average(a=9, b=5):
    print("a is:", a, "b is:", b)
    print("The avergae is:", (a+b)/2)
average(4) #4 overrides 9

def average(a=9, b=5):
    print("a is:", a, "b is:", b)
    print("The avergae is:", (a+b)/2)
average(b=4) #4 overrides 5

#Keyword arguements: order doesnt matter
def average(a, b):
    print("a is:", a, "b is:", b)
    print("The avergae is:", (a+b)/2)

average(b=10, a=23)


# Required arguements
def average(a, b):
    print("a is:", a, "b is:", b)
    print("The avergae is:", (a+b)/2)

average(10, 23)

#Variable-length arguments

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("Pawan", "Vivek", "Kiran")

#Keyword Arbitrary Arguments

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Dholu", lname = "Ram", fname = "kalia")

# return Statement

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("Bheem", "Raju", "Chutki"))





