# -*- coding: utf-8 -*-
idade=[]
altura=[]
i=0
while(True) :
    idade.append(int(input()))
    altura.append(int(input())) 
    if idade==-1 :
        idade.remove(i)
        break
    else:
        if idade<18 or idade<0 :
            idade.remove(i)
            i=i-1
    i=i+1    

































