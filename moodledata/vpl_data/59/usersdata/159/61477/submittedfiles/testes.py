# -*- coding: utf-8 -*-
def magica (a):
    soma=0
    for j in range (0,len(a),1):
        for i in range (0,len(a),1):
            if j==a[i]:
                soma=soma+1
            if soma!=j:
                return False
    return True 

a=[]
n=int(input('Tamanho:'))
for i in range (0,n,1):
    valor=int(input('valor:'))
    a.append(valor)
print(a)

if magica(a):
    print('S')
else:
    print('N')