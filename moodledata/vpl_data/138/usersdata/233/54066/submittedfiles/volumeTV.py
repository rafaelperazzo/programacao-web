#-*- coding: utf-8 -*-
V=int(input('V: '))
T=int(input('P: '))
for i in range(1,T+1,1):
    a=int(input('a: ')) 
    if V+a<=0:
        V=V-V
    elif V+a>=100:
        b=V-100
        V=V-b
    else:
        V=V+a
print(V)
