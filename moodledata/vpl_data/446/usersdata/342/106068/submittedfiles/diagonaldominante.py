# -*- coding: utf-8 -*-
n = int(input('digite a ordem da matriz'))

m = []
for i in range (0,n,1):
    l = []
    for j in range (0,n,1):
        val = int(input('digite os elementos'))
        l.append(val)
    m.append(l)
    
    
if m[0][0] > sum(m[0]) or m[1][1] > sum(m[1]) or m[2][2] > sum(m[2]):
    print ('SIM')
else:
    print ('NAO')

