# -*- coding: utf-8 -*-
c=int(input('Digite a quantidade de consultas: '))
est=[]
cont=0
for i in range(0,c,1):
    tam=int(input('Digite o tamanho procurado: '))
    est.append(tam)
    
    if est.count(tam)==1:
        cont=cont+2

print(cont)
