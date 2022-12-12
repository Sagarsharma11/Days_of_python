import time;

t = time.localtime();
H = int(time.strftime("%H",t))
M = int(time.strftime("%M",t))
S = int(time.strftime("%S",t))

if(H>=4 and H<12):
    print("Good Morning Uncle")
elif(H>=12 and H<16):
    print("Good Afternoon Uncle")
elif(H>=16 and H<20):
    print("Good Evening Uncle")
else:
    print("Good Night Uncle")

