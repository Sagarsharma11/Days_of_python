print("............CALCULATOR..............\n\n")
a = int(input("Enter Num: "))
b = int(input("Enter Num: "))
print("press 1 to Add\n")
print("press 2 to Substract\n")
print("press 3 to multiply\n")
print("press 4 to division\n")
ch=int(input("Enter Choice"))

try:
    if(ch==1):
        print(a+b)
    elif(ch==2):
        print(a-b)
    elif(ch==3):
        print(a*b)
    elif(ch==4):
        print(a/b)
    else:
        print("wrong choice")
except:
    print("An exception occured")
