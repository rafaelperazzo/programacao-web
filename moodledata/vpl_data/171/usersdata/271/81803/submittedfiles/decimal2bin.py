# -*- coding: utf-8 -*-
#ENTRADA
bin=int(input('Digite a entrada em 0s e 1s: '))
soma = 0
cont = 0
#PROCESSAMENTO
while (bin>0) :
    ultimo = bin%10
    num = ultimo*(2**cont)
    soma = soma + num
    cont = cont + 1
    
print(soma)
    


