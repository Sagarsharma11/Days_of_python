class Math:
    def __init__(self,num):
        self.num = num
    def show(self,x):
        print(self.num*x)
    @staticmethod
    def multiply(y,x):
        print(y*x)

obj = Math(20)
obj.show(20)
Math.multiply(10,20)

    