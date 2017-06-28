# -*- coding: utf-8 -*-
def jogo(a,e,s):
    cont=0
    if s>=e:
        for i in range (e,s+1,1):
            cont=cont+a[i]
    else:
        for i in range (e,s-1,1):
            cont=cont+a[i]
    return cont

n=int(input('Digite n:'))

a=[]
e=int(input('Digite a entrada:'))
s=int(input('Digite a saída:'))

for i in range (0,n,1):
    valor=int(input('Quantidade de vidas:'))
    a.append (valor)
    
print(jogo(a,e,s))    
        
