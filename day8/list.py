l = [64,9,3,12,5,6,7,8]
print(l)
# l.append('hello')
# print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
x=l.index(64)
print(x)
print(l.count(64))

#copy list 
m=l.copy()

print(l)