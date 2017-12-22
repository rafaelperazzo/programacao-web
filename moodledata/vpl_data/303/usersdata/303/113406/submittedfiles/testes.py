# -*- coding: utf-8 -*#notas=[]
#for i in range(0,50,1):
 #   notas.append(float(input('DIGITE A NOTA%d[%d]:' %(i+1 , i)))



#somatorio=0

#for i in range(0,500,1):
#    if i%2!=0 and i%3==0:
#        somatorio+=i
    
#print(somatorio)


matriz=[]

n=int(input('DIGITE A COLUNA:'))
m=int(input('DIGITE A LINHA:'))
for i in range(0,n,1):
    matriz_linha=[]
    for j in range(0,m,1):
        matriz_linha.append(int(input('DIGITE UM ELEMENTO:')))
    matriz.append(matriz_linha)
    
coluna_soma=[]
for j in range(0,m,1):
    soma_coluna=0
    for i in range(0,n,1):
        soma_coluna+=matriz[i][j]
    coluna_soma.append(soma_coluna)
    
linha_soma=[]
for i in range(0,n,1):
    soma_linha=0
    for j in range(0,m,1):
        soma_linha+=matriz[i][j]
    linha_soma.append(soma_linha)
    
    

print(matriz)
print(coluna_soma)
print(linha_soma)  
print(min(coluna_soma))


