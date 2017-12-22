# -*- coding: utf-8 -*-
a = [8.0, 5.0, 10.0, 5.0]
# 2.0 na posicao 2 (indice 1)
print(a)
print(len(a))
a.append(0.0)
print(len(a))
for i in range(len(a)-1,0,-1):
    if (i==1) :
        a[i] = 2.0
    else :
        a[i] = a[i-1]
    
print(a)
print(len(a))


#for i in range(2 , -1 , -1):
#    print(a[i])