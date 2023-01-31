f = open('./day23/file.txt','w')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

lines = ['line1','line2','line3']
for i in range(0,len(lines)):
    f.writelines(f'{lines[i]}\n')

