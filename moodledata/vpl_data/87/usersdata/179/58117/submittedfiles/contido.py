# -*- coding: utf-8 -*-
def quantidade(c,d):
    cont=0
    for i in range(0,len(d),1):
        for z in range(0,len(c),1):
            if (d[i]==c[z]):
                cont=cont+1
    return(cont)
n=int(input('digite o valor de n :'))    
m=int(input('digite o valor de m :'))
a=[]
b=[]
for i in range(1,n+1,1):
    valorA=int(input('digite o valor de A :'))
    a.append(valorA)
for i in range(1,m+1,1):
    valorB=int(input('digite o valor de B :'))
    b.append(valorB)
print(quantidade(a,b))    
    
    

