#List is mutable

marks= [90,80,70, "oops"]
for mark in marks:
    print(mark)

print(marks[-3]) #negative
print(marks[len(marks)-3]) #positive

if 80 in marks:
    print("yes")
else:
    print("no")

if "oops" in marks:
    print("yes")
else:
    print("no")

if "80" in marks:
    print("yes")
else:
    print("no")

print(marks[:]) #print list
print(marks[::3]) #print with 3 jumps


#list comprehension

lst= [i for i in range(5)]
print(lst)

lst= [i*i for i in range(5)]
print(lst)

lst= [i*i for i in range(5) if i%2==0]
print(lst)

