# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
q = int(input('Digite o Valor: '))
i=0
num = 2
den = 1
produto=1
while i <=(q-1):
    produto=produto*num/den
    if i%2 ==1:
        num = num+2
    else:
        den=den+2
    i=1+1
    produto=produto+2
    print (i)

print('%.5'%produto*2)
    