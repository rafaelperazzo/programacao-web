# -*- coding: utf-8 -*#notas=[]
#for i in range(0,50,1):
 #   notas.append(float(input('DIGITE A NOTA%d[%d]:' %(i+1 , i)))



#somatorio=0

#for i in range(0,500,1):
#    if i%2!=0 and i%3==0:
#        somatorio+=i
    
#print(somatorio)


matriz=[]

n=int(input('DIGITE A ORDEM DA MATRIZ:'))

for i in range(0,n,1):
    for j in range(0,n,1):
        matriz_linha=[]
        matriz_linha.append(int(input('DIGITE UM ELEMENTO:')))
    matriz.append(matriz_linha)
    
print(matriz)
        
    