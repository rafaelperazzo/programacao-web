# -*- coding: utf-8 -*-
n=int(input('numero: '))
n=str(n)
l=[]
s=0
for i in range(len(n)):
    l.append(int(n[i]))
    s+=l[i]
    
print (s)