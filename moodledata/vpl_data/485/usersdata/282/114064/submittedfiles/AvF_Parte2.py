# -*- coding: utf-8 -*-
A=80000
B=200000
anos=0
while True:
    if A != B:
        A+= A*(3/100)
        B+= B*(1.5/100)
        anos+=1
    else:
        print(anos)
    
    
    