# -*- coding: utf-8 -*-

def vida(a):
    soma=0
    for i  in range(entrada,saida+1,1):
        soma=soma+a[i]
    return(soma)

#Entrada
sala=int(input('Digite a quantidade de salas:'))
entrada=int(input('Digite a porta de entrada:'))
saida=int(input('Digite a porta de saída:'))

vida=[]
for i in range(0,sala,1):
    valor=int(input('Digite o valor da vida dessa sala:'))
    vida.append(valor)
    

print(vida(vida))