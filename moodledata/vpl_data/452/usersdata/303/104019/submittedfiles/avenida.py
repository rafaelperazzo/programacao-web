# -*- coding: utf-8 -*-
M=int(input('Digite o número M:'))
while(True):
    if M<2 or M>1000:
        M=int(input('Digite o número M:'))
    else:
        break
      

N=int(input('Digite o número N:'))
while(True):
    if N<2 or N>1000:
      N=int(input('Digite o número N:'))  
    else:
         break

matriz=[]

for i in range(0,M,1):
    matriz_elemento=[]
    for j in range(0,N,1):
        elemento=int(input('Digite a valor :'))
        while(True):
            if elemento<1 or elemento>100:
               elemento=int(input('Digite a valor :'))
            else:
                break
            
        matriz_elemento.append(elemento)  
    matriz.append(matriz_elemento)
    
soma=[]

for j in range(0,N,1):
    soma.coluna=0
    for i in range(0,M,1):
        soma= soma.coluna + matriz[i][j]
    soma.append(soma.coluna)
menor_valor=[]
menor_valor.append(min(soma))
print(menor_valor)

        
  