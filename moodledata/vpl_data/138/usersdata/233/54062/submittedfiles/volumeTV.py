#-*- coding: utf-8 -*-
V=int(input('V: '))
T=int(input('P: '))
for i in range(1,T+1,1):
    while V>0:
        a=int(input('a ')) 
        V=V+a
print(V)
