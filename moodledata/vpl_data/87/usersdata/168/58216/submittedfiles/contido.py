# -*- coding: utf-8 -*-
def iguais (c,d):
    iguais=0
    for i in range (0,len(d),1):
        for j in range (0,len(c),1):
            if (d[i]==c[j]):
                iguais=iguais+1
    return(iguais)

a=int(input('Digite a quantidade de elementos de a: '))  
b=int(input('Digite a quantidade de elementos de b: '))
c=[]
d=[]
for i in range (0,a,1):
    valor1=int(input('Digite os elementos da lista a: '))
    c.append(valor1)
for j in range (0,b,1):
    valor2=int(input('Digite os elementos da lista a: '))
    c.append(valor2)
print(iguais(c,d))    


