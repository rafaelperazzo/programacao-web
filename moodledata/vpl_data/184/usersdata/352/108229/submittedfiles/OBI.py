# -*- coding: utf-8 -*-

def total (a,b,nota):
    cont=0
    for i in range(0,len(a),1):
        if((a[i]+b[i])>=nota):
            cont=cont+1
    return(cont)

n=int(input('Quantidade de competidores: '))
p=int(input('Nota de corte: '))
a=[]
b=[]

for i in range(0,n,1):
    a.append(float(input('Digite a nota da primeira fase: ')))
    b.append(float(input('Digite a nota da segunda fase: ')))
print(total(a,b,
