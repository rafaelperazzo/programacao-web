# -*- coding: utf-8 -*-
while True:
    A=80000
    B=200000
    anos=0
    if A != B:
        A+= A*(3/100)
        B+= B*(1.5/100)
        anos+=1
        continue
    else:
        print(anos)
        break
print(142)
    
    
    