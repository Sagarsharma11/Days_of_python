import os

if(not os.path.exists('./day20/customdir')):
    os.mkdir("./day20/customdir")

for i in range(1,10):
    os.mkdir(f'./day20/customdir{i}')
