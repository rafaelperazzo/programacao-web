# -*- coding: utf-8 -*-
A=80000
B=200000
pa= A*(3/100)
pb= B*(1.5/100)
while True:
    for i in range(0,8000000):
        pa= A*(3/100)
        pb= B*(1.5/100)
        anos=0
        if A != B:
            A+= pa
            B+= pb
            continue
            anos+=1
        else:
            print(anos)
            break

    