# -*- coding: utf-8 -*-
# p menor
# q maior
#ENTRADA
p = int(input('Digite o valor de p: '))
q = int(input('Digite o valor de q: '))

#PROCESSAMENTO

cont = 0
while (p>0):
    p = p//10
    cont = cont + 1
    
print(cont)
