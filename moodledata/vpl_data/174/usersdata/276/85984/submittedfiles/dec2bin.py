# -*- coding: utf-8 -*-
# p menor
# q maior
#ENTRADA
p = int(input('Digite o valor de p: '))
q = int(input('Digite o valor de q: '))

#PROCESSAMENTO
#QUANTIDADE DE DIGITOS DE P
cont = 0

while (p>0):
    p = p//10
    cont = cont + 1
    
if p == 0:
    cont = cont + 1
    
#SUBNUMERO
i = 0
while (q>0):
    ultimos_q = q%(10**cont)
    if (ultimos_q == p):
        print ('S')
    else:
        i = i+1
    q = q//10
    
if (i!=0):
    print ('N')
    

