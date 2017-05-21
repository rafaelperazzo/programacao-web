# -*- coding: utf-8 -*-
n=int(input('digite o numero de competidores:'))
v=int(input('digite a pontuacao minima para ser convidado:'))

cont=0
for i in range (1,n+1,1):
    x=int(input('digite a nota na primeira fase:'))
    y=int(input('digite a nota na segunda fase:'))
    a=x+y
    if a>=v:
        cont=cont+1
    else:
        cont=cont
        
print(cont)        