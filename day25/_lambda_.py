def apply(fx,val):
    return 6 + fx(val)

#lamda function
giveSquare = lambda x: x**3
sumoftwo = lambda x,y:(x+y)

if(__name__=="__main__"):
    print(giveSquare(3))
    print(sumoftwo(10,10))
    print(apply(giveSquare,7))