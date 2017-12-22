# -*- coding: utf-8 -*-

ordem=int(input("Digite a ordem da matriz: "))

matriz=np.zeros((ordem,ordem))
for i in range(0,ordem,1):
    for j in range(0,ordem,1):
        matriz[i,j]=int(input('Digite os numeros da matriz: "))
cont=0 
soma=0
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.sahape[1],0):
        if i!=j:
            soma=soma+matriz[i,j]
        else:
            numdiagonal=matriz[i,j]
            
    if numdiagonal>soma:
        cont=cont+1
        
if cont=ordem:
    print('SIM')
else:
    print('NÃO')
            