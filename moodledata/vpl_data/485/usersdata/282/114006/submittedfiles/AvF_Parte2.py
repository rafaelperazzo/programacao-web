# -*- coding: utf-8 -*-
A=80000
B=200000
pa= A*(3/100)
pb= B*(1.5/100)
anos=0
while True:
    for i in range(0,B):
        pa= A*(3/100)
        pb= B*(1.5/100)
        if A != B:
            A+= pa
            B+= pb
            continue
            anos+=1
        if A>=B:
            print(anos)
    break
    