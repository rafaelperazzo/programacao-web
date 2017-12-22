# -*- coding: utf-8 -*-
#ENTRADA
n = int(input('Digite a quantidade de valores : '))
a = []
somapar = 0
somaimpar = 0
contpar = 0
contimpar = 0
#PROCESSAMENTO
for i in range(0,n,1) :
    valor = int(input('Digite o valor : '))
    a.append (valor)
    if (valor%2==0) :
        somapar = somapar + valor
        contpar = contpar + 1
    else :
        somaimpar = somaimpar + valor
        contimpar = contimpar + 1
print(somaimpar)
print(somapar)
print(contimpar)
print(contpar)
print(a)
    



