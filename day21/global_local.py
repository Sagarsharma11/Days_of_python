x=10
def increment():
    global x
    x=5
    print(f'The local x is {x}')

increment()
print(f'The global x is {x}')