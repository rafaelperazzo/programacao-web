from __future__ import division
#ENTRADA

P=input('Digite o valor de P:')
i=input('Digite o valor de i:')
n=input('Digite o valor de n')

#PROCESSAMENTO

v=(P*((1.00+i)**n)/float(i))

#SAIDA

print('O valor de v é %.2f' % v)