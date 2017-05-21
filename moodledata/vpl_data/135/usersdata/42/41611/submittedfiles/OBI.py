# -*- coding: utf-8 -*-
n=int(input('competidores: '))
p=int(input('nota: '))
cont=0
for i in range(1,n+1,1):
    p1=int(input("primeira nota do competidor %i: "%i))
    p2=int(input("segunda nota do competidor %i: "%i))
    if p1+p2>=p:
        cont+=1
print ('cont')