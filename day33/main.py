class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showdetails(self):
        print(f'The Employee : {self.id} and {self.name}')

class Message:
    def message(self):
        print('Thankyou for using Message class')


class Programmer(Employee,Message):
    def greeting(self):
        print('Python is High Level Language')

e1 = Employee('Sagar Sharma',21)
e1.showdetails()
e2 = Programmer('Shymal das',23)
e2.showdetails()
e2.message()