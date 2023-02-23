class Person:
    name = "sagar"
    #magic method
    def __len__(self):
        return len(self.name)

P1 = Person()
print(P1.name)
print(len(P1))
