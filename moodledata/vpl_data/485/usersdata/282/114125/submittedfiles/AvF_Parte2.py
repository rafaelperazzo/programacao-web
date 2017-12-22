# -*- coding: utf-8 -*- 
A=80000
B=200000
anos=0
while (True):
    if A!=B:
        A= A+A*(3/100)
        B= B+B*(1.5/100)
        anos= anos +1
        continue
    else:
        print(anos)
        break
    

    
    
    