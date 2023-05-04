# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

dic={
    "Pawan": "Coder",
    "Hobby": "Coding",
    123: "OneTwoThree",
}
print(dic)
print(dic["Pawan"])

# Accessing Dictionary items:

# I. Accessing single values:
# Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.

info = {'name':'Pawan', 'age':23, 'eligible':True}
print(info['name']) #if not found throws error
print(info.get('eligible')) #if not found result None

# II. Accessing multiple values:
# We can print all the values in the dictionary using values() method.

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

# III. Accessing keys:
# We can print all the keys in the dictionary using keys() method.

print(info.keys())
for key in info.keys():
    print(info[key])  #accessing values

for key in info.keys():
    print(f"The value correspond to the key {key} is {info[key]}")  #accessing values using f string

# IV. Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method.

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())

for key,value in info.items():
    print(f"The value correspond to the key {key} is {value}") 
