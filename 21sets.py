# Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

s= {2,4,2,"False", "Pawan",0}
d= {} 
print(type(d)) #dictionary
st= set()
print(type(st))
for item in s:
    print(item)