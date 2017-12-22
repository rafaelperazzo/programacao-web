# -*- coding: utf-8 -*-
#FUNÇÃO
def total(a,b,nota):
    cont=0
    for i in range(0,len(a),1):
        if((a[i]+b[i])>=nota):
            cont=cont+1
    return(cont)

#PROGRAMA PRINCIPAL
n=int(input('Número de competidores: '))
p=int(input('Nota de corte: '))
a=[]
b=[]
for i in range(0,n,1):
    a.append(float(input('Digite a nota da 1ª fase do competidor %d: ' %(i+1))))
    b.append(float(input('Digite a nota da 2ª fase do competidor %d: ' %(i+1))))
print(total(a,b,p))