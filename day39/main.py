class Employ:
    company = "Apple"
    def show(self):
        print(self.company)
    @classmethod
    def changeCompany(cls,comp):
        '''globaly change the varibale'''
        cls.company = comp
    
e1 = Employ()
e1.show()
e1.changeCompany("Tesla")
e1.show()

e2 = Employ()
e2.show()


