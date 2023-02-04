import random as r
class customerror(Exception):
    'pass value must be 1 or 2 or 3'
    pass

num = 3
print("\n_____Snake__Water__Gun_____\n")
print("\n 1.snake \n 2.water \n 3.gun \n")
user_choice = int(input('enter your choice: '))
gameList = {1:'snake',2:'water',3:'gun'}

try:
    if(user_choice>3 or user_choice<=0):
        raise customerror
    else:
        comp = r.choice(list(gameList.keys()))
        print(user_choice,' ',comp)
        print(f'user select {gameList[user_choice]} and computer select {gameList[comp]}')
        if((gameList[user_choice]=='snake' and gameList[comp]=='water')or
            (gameList[user_choice]=='water' and gameList[comp]=='gun')
        ):
            print('user win')
        elif(user_choice==comp):
            print('draw')
        else:
            print('computer wins')
except customerror:
    print('Invalid number')
