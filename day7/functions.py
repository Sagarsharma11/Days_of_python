#simple function or methods
def ave(a , b):
    print((a+b)/2)

ave(2,5)

#default argumnets function
def add(a=10 , b=10):
    print(a+b)

add(2,5)
add()

def name(name , lastname="sharma"):
    print(name,lastname)

name("sagar")

#key word argument

def sub(a,b):
    print(b-a)

sub(b=100,a=20)

#take array type of argument 

def addnum(*num):
    sum=0
    for i in num:
        sum=sum+i
    print(sum)

addnum(1,2,3,4,5,6,7,8)

#with return statement

def givename(name):
    return name+" Sharma"

takename = givename("Sagar")
print(takename)