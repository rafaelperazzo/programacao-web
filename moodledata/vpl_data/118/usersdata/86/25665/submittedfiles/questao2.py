from __future__ import division
import numpy
qf=int(input('digite o numero de quadrados:'))
fita=[]
c=[]
for i in range(1,qf+1,1):
    fita.append(input('digite se esta colorido:'))

i=0
while fita[i]==0:
    cont=0
    for j in range(0,len(fita),1):
        if fita[j]!=fita[i]:
            cont=cont+1
        else:
            c.append(0)
    c.append(cont)
    
    i=i=1    

print(c)
        
    
    