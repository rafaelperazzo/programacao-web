# -*- coding: utf-8 -*-

n = int(input())

m = []

for i in range (0,n-1,1):
    l = []
    for j in range (0,n-1,1):
        l.append(int(input()))
    m.append(l)

def magica(m):
    x = []
    for i in range (0,len(m),1):
        s1 = 0
        s2 = 0
        for j in range (0,len(m[i]),1):
             s1 = s1 + m[i] [j]
             s2 = s2 + m[j] [i]
    s1 = 0
    s2 = 0
    c = 1
    for i in range (0,len(m),1):
         s1 = s1 + m[i] [i]
         s2 = s2 + m[i] [len(m)-c]
         c += 1
    x.append(s1)
    x.append(s2)
    for i in range (0,len(x),1):
        if x[i] != x[1]:
            return False
    return True
    
if magica(m):
    print('S')
else:
    print('N')