class Employ:
    company = 'AlphaWorldTech'
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f'Emply name is {self.name} company is {self.company}')

e1 = Employ('Sagar')
e1.show()

e2 = Employ('Vikash')
e1.company = "Apple"
# Employ.show(e1)
e1.show()