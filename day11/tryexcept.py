try:
    x = int(input('enter a number '))
    list = [1,2,3,4]
    print(list[4])
except ValueError:
    print('number enterd is not integer')
except IndexError:
    print('index not avilable')
except Exception as e:
    print(f'error {e}')

print("this is important lines")