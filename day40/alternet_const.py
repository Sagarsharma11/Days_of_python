class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name : {self.name} \nAge : {self.age}")
    
    @classmethod
    def AlternerConstructor(cls,str):
        return cls(str.split(',')[0], str.split(',')[1])

p1 = Person('Anil',32)
p1.show()
p2 = Person.AlternerConstructor("Sagar,23")
p2.show()


