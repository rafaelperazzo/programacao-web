from __future__ import division
import numpy
qf=int(input('digite o numero de quadrados:'))
fita=[]

for i in range(1,qf+1,1):
    fita.append(input('digite se esta colorido:'))
c=[]
i=0
cont=0
for j in range(0,len(fita),1):
    if fita[j]!=0:
        cont=cont+1
        if cont>=9:
            c.append(9)

    c.append(cont)
    if fita[j]==0:
        c.append(0)

        
print(c)
        
    
    