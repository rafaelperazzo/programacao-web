# -*- coding: utf-8 -*-
n=int(input())
m=[]
for i in range (0,n,1):
    l=[]
    for j in range(0,n,1):
        l.append(int(input())
def magica (M):
    x=[]
    for i in range (len(M)):
        s1=0
        s2=0
        for j in range(len(M[i])):
            s1=s1+M[i][j]
            s2=s2+M[i][j]
    s1=0
    s2=0
    c=1
    for i in range(len(M)):
        s1=s1+M[i][i]
        s2=s2+M[i][len(M)-c]
        c+=1
    x.append(s1)
    x.append(s2)
    for i in range(len(x)):
        if x[i]!=x[1]:
            return False
    return True
if magica(m):
    print('S')
else:
    print('N')
        

