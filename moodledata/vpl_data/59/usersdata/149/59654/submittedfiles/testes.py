# -*- coding: utf-8 -*-
import itertools 
n=4
z=[]
for i in range(0,n,1):
    lista=int(input('digite o elemento desta lista:'))
    z.append(lista)
g=int(str(z[0])+str(z[1])+str(z[2])+str(z[3]))
permut=list(itertools.permutations(z))
cont=0
for i in range(0,23,1):
    p=int(str(permut[i][0])+str(permut[i][1]))*int(str(permut[i][2])+str(permut[i][3]))
    if p==g:
        cont=cont+1
if cont>=1:
    print('Sim, é um número vampiro')
else:
    print('Não é um número vampiro')

#entende-se que número vampiro, é um número com a quantidade de dígitos par. onde a multiplicação de todas as permutações
#possíveis de metade em metade, dará pelo menos um resultado igual ao número dado.

#como o professor pediu para testar se é um número vampiro de 4 dígitos apenas, eu estimulei logo n=4

#abrir uma lista vazia, chamando de z, para facilitar caminhar por estes elementos...

#usei um comando para permutar todas posições possíveis desta lista : permut=list(itertools.permutations(z))

#como eu precisava multiplicar de dois em dois de cada uma das permutações possíveis....fiz uma repetição de 0 à 23 (4!=24)
#assim....transforformei em texto a soma do indice 0 e 1

    

    
    
    
    
    
    
    
    

    