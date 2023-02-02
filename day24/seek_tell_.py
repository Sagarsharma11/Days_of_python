def seektell():
    with open('./day24/file.txt','r') as f:
        print(type(f))
        f.seek(10)
        print(f.tell())
        data = f.read(5)
        print(data)

def truncat():
    with open('./day24/file.txt','w') as f:
        f.write('hey programmers')
        f.truncate(5)
    
if(__name__=="__main__"):
    truncat()
    seektell()