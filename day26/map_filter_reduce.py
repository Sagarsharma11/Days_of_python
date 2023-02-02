# Map


l = [1,2,3,4,5,6,7,8]
newlist = list(map(lambda x: x*x,l))
print(newlist)

# Filter

def filter_fun(x):
    return x>4

fil = list(filter(filter_fun,l))
print(fil)

# Reduce 

from functools import reduce

red = reduce(lambda x,y: x+y,l)
print(red)