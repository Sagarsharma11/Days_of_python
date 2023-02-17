class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'Name : {self.name}\n Age : {self.age}')

list = [1,2,3]
print(dir(list))
print(list.__add__)

P1 = Person('sagar',23)
print(P1.__dict__)
print(help(Person))

