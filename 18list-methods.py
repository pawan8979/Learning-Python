l= [21,17,13,15, 13]
print(l)

l.append(20)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(21))

print(l.count(13))

#referncing list

m=l
m[0]=0
print(l)

#copying a list

m= l.copy()
m[0]=0
print(l)

l.insert(1, 899)
print(l)

m=[900,1000,1100]
k= l+m
l.extend(m)
print(l)
print(k)

