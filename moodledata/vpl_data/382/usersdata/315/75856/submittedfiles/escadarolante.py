# -*- coding: utf-8 -*-

n = int(input('numero de pessoas: '))
tem = 0
T = [0]*n

for i in range(n):
    b =i+1
    T[i] = int(input('tempo da pessoa %d: '%b))
    if i!=0:
        if T[i]-T[i-1]>=10:
            tem = tem + 10
        else:
            tem = tem+T[i]-T[i-1]
    else:
        tem = tem+10
print ('tempo de funcionamento = %d'%tem)







