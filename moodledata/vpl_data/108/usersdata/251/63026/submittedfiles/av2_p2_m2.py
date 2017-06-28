# -*- coding: utf-8 -*-
salas=int(input('Digite a quantidade de salas: '))
vidas=[]
for i in range(0,salas,1):
    valor=float(input('Digite o valor de vida da sala '+str(i)+': '))
    vidas.append(valor)

entrada=int(input('Digite o número da porta de entrada: ')
saida=int(input('Digite o número da porta de saída: ')

def vidaMaxima(vidas,entrada,saida):
    soma=0
    for i in range(entrada,saida+1,1):
        soma=soma+vidas[i]
    
    return(soma)
    
vidaTotal=(vidaMaxima(vidas,entrada,saida))
print(vidaTotal)