def greet(fx):
    def mfx():
        print('hey!')
        fx()
        print('Thanks for using this function')
    return mfx

@greet
def helloWorld():
    print('Hello, World!')

if(__name__=="__main__"):
    helloWorld()