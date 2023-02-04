class Person:
    name="Sagar Sharma"
    occupation="Javascript Developer"
    def info(self):
        print(f'{self.name} is a {self.occupation}')

obj1 = Person()
obj1.info()

obj2 = Person()
obj2.name="Mayank Saho"
obj2.occupation = "Bank Manager"
obj2.info()