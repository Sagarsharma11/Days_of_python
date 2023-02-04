class Person:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f'{self.name} is a {self.occ}')

obj1 = Person('Sagar Sharma', 'Python Developer')
obj1.info()

obj2 = Person('Saurya Bhardwaj', 'Sales Manager')
obj2.info()