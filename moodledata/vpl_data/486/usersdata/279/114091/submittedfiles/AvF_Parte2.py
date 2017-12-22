# -*- coding: utf-8 -*-
idade=[]
altura=[]
a=0
while(True) :
    idade.append(int(input()))
    altura.append(int(input())) 
    if idade[a]==-1 :
        idade.remove(a)
        altura.remove(a)
        a=a-1
        break
    else:
        if idade[a]<18 or idade[a]<0 :
            idade.remove(a)
            altura.remove(a)
            a=a-1
    a=a+1    
b=0
for i in range(0,i,1) :
    if idade[i]>25 :
        if altura[i]<(sum(altura)/a) :
            b=b+1

print(b)





























