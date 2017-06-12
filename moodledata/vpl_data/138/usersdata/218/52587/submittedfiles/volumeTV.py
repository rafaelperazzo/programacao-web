#-*- coding: utf-8 -*-
v=int(input('digite o volume inicial de sua tv:'))
t=int(input('digite o numero de mudanças no volume:'))
nvalor=v
for i in range (0,t,1):
    mudança=int(input('digide a alteração no volume:'))
    if nvalor+(mudança)<100:
        nvalor=nvalor+(mudança)
    else:
        nvalor=100
print(nvalor)         
     