#finally always runs not matter what is going on 

def myfun():
    try:
        list = [1,2,3,4,5,6]
        print(list[6])
    except:
        print('some error occured')
        return 0 
        print("this will'n run")
    finally:
        print("it will run in every aspect")

val = myfun()
print(val)