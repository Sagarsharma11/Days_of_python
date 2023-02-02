def readfile():
    f = open('./day22/file.txt','r')
    text = f.read()
    print(text)
    f.close()

def writefile():
    f = open('./day22/file2.txt','w')
    f.write('Hello, world!')
    f.close()

def appendfile():
    f = open('./day22/file2.txt','a')
    f.write(' Hello, world!')
    f.close()

with open('./day22/file3.txt','w') as f:
    f.write('hey this is with statement here no require to close the file')

if(__name__=="__main__"):
    readfile()
    writefile()
    appendfile()

