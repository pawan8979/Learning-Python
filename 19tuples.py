# LIst are unmutable

tup= (1,)
print(type(tup), tup) #int; include , after 1
tup= (1,5,6, "green", True)
print(type(tup), tup)

print(tup[-1])

if 6 in tup:
    print("Yes")

tup2= tup[1:4]
print(tup2)